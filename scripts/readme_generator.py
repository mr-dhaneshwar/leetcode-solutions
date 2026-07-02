"""
README generation module for LeetCode solutions.
Responsible for rendering problem README.md files using templates.
Independent of LeetCode API.
"""

import os
from typing import Dict

def generate_problem_readme(problem_dir: str, metadata: dict, solution_path: str) -> None:
    """
    Renders and saves README.md for a specific problem folder using the template.
    
    :param problem_dir: The directory of the problem.
    :param metadata: The dictionary metadata for the problem.
    :param solution_path: The file path to the solution code.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    template_path = os.path.join(root_dir, "templates", "problem_readme.md")
    readme_path = os.path.join(problem_dir, "README.md")
    
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Problem README template not found at {template_path}")
        
    if not os.path.exists(solution_path):
        raise FileNotFoundError(f"Solution file not found at {solution_path}")
        
    # Read solution code directly from solution_path
    with open(solution_path, "r", encoding="utf-8") as f:
        solution_code = f.read()
        
    # Map extension to markdown code language identifier
    _, ext_raw = os.path.splitext(solution_path)
    language_ext = ext_raw.lstrip(".").lower()
    
    ext_to_lang: Dict[str, str] = {
        "py": "python",
        "cpp": "cpp",
        "java": "java",
        "c": "c",
        "cs": "csharp",
        "js": "javascript",
        "ts": "typescript",
        "go": "go",
        "kt": "kotlin",
        "rs": "rust",
        "swift": "swift",
        "rb": "ruby",
        "scala": "scala",
        "php": "php",
        "sql": "sql",
        "sh": "bash"
    }
    markdown_lang = ext_to_lang.get(language_ext, "text")
    
    # Load template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
        
    # Format tags/topics
    topics = ", ".join(metadata.get("tags", []))
    
    # Fill placeholders
    rendered = (
        template
        .replace("{{TITLE}}", metadata.get("title", ""))
        .replace("{{DIFFICULTY}}", metadata.get("difficulty", ""))
        .replace("{{TOPICS}}", topics)
        .replace("{{URL}}", metadata.get("url", ""))
        .replace("{{DESCRIPTION}}", metadata.get("description", ""))
        .replace("{{EXAMPLES}}", metadata.get("examples", ""))
        .replace("{{CONSTRAINTS}}", metadata.get("constraints", ""))
        .replace("{{LANGUAGE}}", markdown_lang)
        .replace("{{SOLUTION}}", solution_code)
    )
    
    # Ensure folder directory exists
    os.makedirs(problem_dir, exist_ok=True)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(rendered)
        
    print(f"Generated README: {readme_path}")
