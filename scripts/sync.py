"""
LeetCode sync logic module.
Coordinates detecting new accepted submissions, fetching details, and writing local files.
"""

import os
from typing import Dict
import api

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
        
        # 1. Fetch question details (difficulty, ID)
        try:
            question = api.get_question_details(title_slug)
            difficulty = question.get("difficulty", "Unknown")
            question_id = question.get("questionId", "")
        except Exception as e:
            # Log warning, fallback but continue syncing other problems if possible
            print(f"Warning: Failed to fetch question details for {title_slug}: {e}")
            difficulty = "Unknown"
            question_id = ""
            
        # Define output directory and file path
        # Question numbers must always be zero padded to 4 digits (e.g. 14 -> 0014)
        padded_id = str(question_id).zfill(4) if question_id else "0000"
        title_folder = title_from_slug(title_slug)
        folder_name = f"{padded_id}-{title_folder}"
        
        problem_dir = os.path.join(output_dir, difficulty, folder_name)
        filepath = os.path.join(problem_dir, f"solution.{ext}")
        
        if os.path.exists(filepath):
            # Already synced, skip
            continue
            
        print(f"Syncing new accepted solution: {title_slug} ({lang})...")
        
        # 2. Fetch code details
        code = api.get_submission_code(sub_id)
        
        # Ensure target directories exist
        os.makedirs(problem_dir, exist_ok=True)
        
        # 3. Save file
        header = get_comment_header(ext, sub.get("title", ""), title_slug, difficulty, lang)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(header + code + "\n")
            
        print(f"Saved: {filepath}")
        synced_count += 1
        
    return synced_count
