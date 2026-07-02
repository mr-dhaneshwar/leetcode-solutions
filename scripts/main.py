"""
LeetCode sync entry point.
Loads configuration, triggers the sync module, and manages top-level error handling.
"""

import os
import json
import sys
import sync
import api

# Robust path resolution relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_FILE = os.path.join(ROOT_DIR, "config.json")
OUTPUT_DIR = ROOT_DIR


def load_config(config_path: str) -> dict:
    """
    Loads and returns config.json data.
    
    :param config_path: Path to the config file.
    :return: Loaded configuration dictionary.
    :raises FileNotFoundError: If config file is missing.
    :raises ValueError: If config file contains invalid JSON.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
        
    with open(config_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse config.json: {e}")

def main() -> None:
    """Main execution function."""
    try:
        # Load configuration
        config = load_config(CONFIG_FILE)
        
        # Verify required keys in config
        leetcode_config = config.get("leetcode", {})
        username = leetcode_config.get("username")
        
        if not username:
            raise ValueError("Username must be defined under 'leetcode.username' in config.json")
            
        # Verify credentials and check connectivity
        print("Checking LeetCode authentication status...")
        user_status = api.get_user_status()
        print(f"Logged in successfully as: {user_status['username']}")
        
        # Verify configured username matches session
        if username.lower() != user_status["username"].lower():
            print(
                f"Warning: Configured username '{username}' does not match "
                f"authenticated user '{user_status['username']}'"
            )
        
        # Execute the sync
        synced_count = sync.sync_solutions(username=username, output_dir=OUTPUT_DIR)
        print(f"Sync complete. Synced {synced_count} new solution(s).")
        
    except FileNotFoundError as e:
        print(f"Configuration Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Invalid Config/Input: {e}", file=sys.stderr)
        sys.exit(1)
    except api.AuthenticationError as e:
        print(f"Authentication Error: {e}", file=sys.stderr)
        sys.exit(1)
    except api.LeetCodeAPIError as e:
        print(f"LeetCode API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during sync: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
