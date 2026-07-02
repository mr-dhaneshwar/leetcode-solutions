# LeetCode Problem: Ransom Note
# Link: https://leetcode.com/problems/ransom-note/
# Difficulty: Easy
# Language: python3

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}

        for ch in magazine:
            char_count[ch] = char_count.get(ch, 0) + 1

        for ch in ransomNote:
            if char_count.get(ch, 0) == 0:
                return False

            char_count[ch] -= 1

        return True

        
