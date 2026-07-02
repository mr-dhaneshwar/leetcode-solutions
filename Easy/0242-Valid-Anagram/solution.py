# LeetCode Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Language: python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}

        for ch in s:
            mapping[ch] = mapping.get(ch, 0) + 1

        for ch in t:
            if ch not in mapping:
                return False

            mapping[ch] -= 1

            if mapping[ch] < 0:
                return False

        return True
