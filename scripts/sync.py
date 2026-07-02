"""
LeetCode sync logic module.
Coordinates detecting new accepted submissions, fetching details, and writing local files.
"""

import os
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from bs4 import BeautifulSoup, Tag
import api
import readme_generator

# Map language to file extension
LANG_MAP: Dict[str, str] = {
    "cpp": "cpp",
    "java": "java",
    "python": "py",
    "python3": "py",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "kotlin": "kt",
    "rust": "rs",
    "swift": "swift",
    "ruby": "rb",
    "scala": "scala",
    "php": "php",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "postgresql": "sql",
    "bash": "sh"
}

def get_comment_header(ext: str, title: str, title_slug: str, difficulty: str, lang: str) -> str:
    """
    Generates a styled comment header for the solution file depending on its extension.
    
    :param ext: File extension of the solution.
    :param title: Clean title of the problem.
    :param title_slug: Slug of the problem title.
    :param difficulty: Problem difficulty level.
    :param lang: LeetCode submission language.
    :return: A formatted header comment string.
    """
    comment_char = "#"
    if ext in ["cpp", "java", "js", "ts", "cs", "go", "kt", "rs", "swift", "scala"]:
        comment_char = "//"
    elif ext in ["sql"]:
        comment_char = "--"
        
    return (
        f"{comment_char} LeetCode Problem: {title}\n"
        f"{comment_char} Link: https://leetcode.com/problems/{title_slug}/\n"
        f"{comment_char} Difficulty: {difficulty}\n"
        f"{comment_char} Language: {lang}\n\n"
    )

def title_from_slug(slug: str) -> str:
    """
    Converts a slug like 'longest-common-prefix' to 'Longest-Common-Prefix'.
    
    :param slug: The problem title slug.
    :return: A capitalized title string with words joined by hyphens.
    """
    return "-".join(word.capitalize() for word in slug.split("-") if word)

def parse_leetcode_html(html_content: str) -> tuple[str, str, str]:
    """
    Parses LeetCode HTML content using BeautifulSoup and splits it into
    description, examples, and constraints sections.
    
    :param html_content: Raw HTML content from LeetCode API.
    :return: A tuple of (description_html, examples_html, constraints_html).
    """
    if not html_content:
        return "", "", ""
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    description_elements = []
    example_elements = []
    constraints_elements = []
    
    current_state = "description"  # Can be: "description", "examples", "constraints"
    
    # Loop through top-level elements or direct children of the soup
    for element in soup.contents:
        if not isinstance(element, Tag):
            # For NavigableString or other non-tag content, append to current state
            if current_state == "description":
                description_elements.append(str(element))
            elif current_state == "examples":
                example_elements.append(str(element))
            elif current_state == "constraints":
                constraints_elements.append(str(element))
            continue
            
        element_text = element.get_text().strip().lower()
        
        # Check for state transitions
        # 1. Check if it's the constraints header
        is_constraints_header = False
        if "constraints" in element_text:
            if element.name in ["p", "h3", "h4", "div", "ul"] and (
                element.find("strong") or element.name in ["h3", "h4"]
            ):
                if len(element_text) < 30:  # Constraints header text is short
                    is_constraints_header = True
                    
        if is_constraints_header:
            current_state = "constraints"
            # Skip the HTML constraints header to let our markdown template header show
            continue
            
        # 2. Check if it's an example header
        is_example_header = False
        if "example" in element_text:
            has_example_class = False
            strong_tags = element.find_all("strong")
            for strong in strong_tags:
                if "example" in strong.get("class", []) or "example" in strong.get_text().lower():
                    has_example_class = True
            if element.name in ["h3", "h4"] or has_example_class or element_text.startswith("example"):
                if len(element_text) < 30:
                    is_example_header = True
                    
        if is_example_header:
            current_state = "examples"
            
        # Append element string to the corresponding section
        element_str = str(element)
        if current_state == "description":
            description_elements.append(element_str)
        elif current_state == "examples":
            example_elements.append(element_str)
        elif current_state == "constraints":
            constraints_elements.append(element_str)
            
    description_html = "".join(description_elements).strip()
    examples_html = "".join(example_elements).strip()
    constraints_html = "".join(constraints_elements).strip()
    
    return description_html, examples_html, constraints_html

def generate_metadata(
    problem_dir: str,
    question_id: str,
    title: str,
    title_slug: str,
    difficulty: str,
    language: str,
    tags: List[str],
    description: str = "",
    examples: str = "",
    constraints: str = ""
) -> bool:
    """
    Creates or updates the metadata.json file inside the problem folder.
    Updates the file only if the data has changed.
    
    :param problem_dir: Target directory path for the problem.
    :param question_id: LeetCode question ID.
    :param title: Clean title of the problem.
    :param title_slug: Slug of the problem title.
    :param difficulty: Difficulty level.
    :param language: Language of the solution.
    :param tags: Topic tags associated with the question.
    :param description: HTML description of the problem.
    :param examples: HTML examples of the problem.
    :param constraints: HTML constraints of the problem.
    :return: True if the metadata file was written/updated, False otherwise.
    """
    filepath = os.path.join(problem_dir, "metadata.json")
    url = f"https://leetcode.com/problems/{title_slug}/"
    
    new_data = {
        "question_id": question_id,
        "title": title,
        "title_slug": title_slug,
        "difficulty": difficulty,
        "language": language,
        "url": url,
        "tags": tags,
        "description": description,
        "examples": examples,
        "constraints": constraints
    }
    
    should_write = True
    existing_data = {}
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
            
            # Compare all keys in new_data to check for changes
            all_match = True
            for key, val in new_data.items():
                if existing_data.get(key) != val:
                    all_match = False
                    break
            
            if all_match:
                should_write = False
        except Exception as e:
            print(f"Warning: Failed to parse existing metadata.json at {filepath}: {e}")
            
    if should_write:
        # Preserve synced_at if metadata didn't actually change other fields
        new_data["synced_at"] = existing_data.get(
            "synced_at", 
            datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        )
        non_timestamp_diff = False
        for key in new_data:
            if key != "synced_at" and existing_data.get(key) != new_data[key]:
                non_timestamp_diff = True
                break
        if non_timestamp_diff or "synced_at" not in existing_data:
            new_data["synced_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            
        os.makedirs(problem_dir, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=2)
        print(f"Saved metadata: {filepath}")
        return True
        
    return False

def find_problem_dir(output_dir: str, title_slug: str) -> Optional[str]:
    """
    Finds the problem directory in output_dir if it exists.
    
    :param output_dir: Output directory to search.
    :param title_slug: The LeetCode problem title slug.
    :return: Absolute folder path if found, otherwise None.
    """
    title_folder = title_from_slug(title_slug)
    for difficulty in ["Easy", "Medium", "Hard", "Unknown"]:
        difficulty_dir = os.path.join(output_dir, difficulty)
        if not os.path.exists(difficulty_dir):
            continue
        try:
            for name in os.listdir(difficulty_dir):
                if name.endswith(f"-{title_folder}") and os.path.isdir(os.path.join(difficulty_dir, name)):
                    return os.path.join(difficulty_dir, name)
        except Exception:
            pass
    return None

def sync_solutions(username: str, output_dir: str = "solutions") -> int:
    """
    Syncs the latest accepted submissions for a given user.
    
    :param username: The LeetCode username.
    :param output_dir: The directory to save solutions into.
    :return: The number of new solutions synced.
    :raises Exception: Any unexpected or API-related exception.
    """
    print(f"Fetching recent submissions for user: {username}...")
    submissions = api.get_recent_submissions(username)
    print(f"Found {len(submissions)} recent submissions.")
    
    synced_count = 0
    for sub in submissions:
        if sub.get("statusDisplay") != "Accepted":
            continue
            
        title_slug = sub.get("titleSlug")
        sub_id = int(sub.get("id"))
        lang = sub.get("lang")
        ext = LANG_MAP.get(lang, "txt")
        
        # 1. Check if problem is already fully synced on disk (fast path)
        problem_dir = find_problem_dir(output_dir, title_slug)
        solution_path = None
        if problem_dir:
            try:
                for filename in os.listdir(problem_dir):
                    if filename.startswith("solution."):
                        solution_path = os.path.join(problem_dir, filename)
                        break
            except Exception:
                pass
                
            metadata_filepath = os.path.join(problem_dir, "metadata.json")
            readme_filepath = os.path.join(problem_dir, "README.md")
            
            if (
                solution_path 
                and os.path.exists(solution_path) 
                and os.path.exists(metadata_filepath) 
                and os.path.exists(readme_filepath)
            ):
                try:
                    with open(metadata_filepath, "r", encoding="utf-8") as f:
                        meta = json.load(f)
                    if meta.get("description"):
                        # Already fully synced with description and README, skip!
                        continue
                except Exception:
                    pass

        # 2. Fetch question details from LeetCode (difficulty, ID, content HTML, tags)
        try:
            question = api.get_question_details(title_slug)
            difficulty = question.get("difficulty", "Unknown")
            question_id = question.get("questionId", "")
            content_html = question.get("content", "")
            tags = [tag["name"] for tag in question.get("topicTags", [])] if question else []
        except Exception as e:
            print(f"Warning: Failed to fetch question details for {title_slug}: {e}")
            difficulty = "Unknown"
            question_id = ""
            content_html = ""
            tags = []
            
        # Parse content HTML into description, examples, and constraints
        desc, examples, constraints = parse_leetcode_html(content_html)
            
        # Define output directory and file path if it was not resolved
        if not problem_dir:
            padded_id = str(question_id).zfill(4) if question_id else "0000"
            title_folder = title_from_slug(title_slug)
            folder_name = f"{padded_id}-{title_folder}"
            problem_dir = os.path.join(output_dir, difficulty, folder_name)
            solution_path = os.path.join(problem_dir, f"solution.{ext}")
        elif not solution_path:
            solution_path = os.path.join(problem_dir, f"solution.{ext}")
            
        # 3. Check if solution file needs to be created/written
        new_solution_synced = False
        if not os.path.exists(solution_path):
            print(f"Syncing new accepted solution: {title_slug} ({lang})...")
            
            # Fetch submission code
            code = api.get_submission_code(sub_id)
            
            # Ensure target directories exist
            os.makedirs(problem_dir, exist_ok=True)
            
            # Save solution code file
            header = get_comment_header(ext, sub.get("title", ""), title_slug, difficulty, lang)
            with open(solution_path, "w", encoding="utf-8") as f:
                f.write(header + code + "\n")
                
            print(f"Saved: {solution_path}")
            new_solution_synced = True
            
        # 4. Generate and save metadata.json
        metadata_written = generate_metadata(
            problem_dir=problem_dir,
            question_id=question_id,
            title=sub.get("title", ""),
            title_slug=title_slug,
            difficulty=difficulty,
            language=lang,
            tags=tags,
            description=desc,
            examples=examples,
            constraints=constraints
        )
        
        # 5. Generate and save README.md
        readme_filepath = os.path.join(problem_dir, "README.md")
        should_generate_readme = metadata_written or not os.path.exists(readme_filepath)
        
        if should_generate_readme:
            try:
                # Load metadata to ensure it is the single source of truth
                metadata_filepath = os.path.join(problem_dir, "metadata.json")
                with open(metadata_filepath, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                    
                readme_generator.generate_problem_readme(
                    problem_dir=problem_dir,
                    metadata=meta,
                    solution_path=solution_path
                )
            except Exception as e:
                print(f"Warning: Failed to generate README for {title_slug}: {e}")
                
        if new_solution_synced:
            synced_count += 1
            
    return synced_count
