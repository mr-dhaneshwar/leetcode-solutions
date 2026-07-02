# LeetCode Problem: Maximum Number of Vowels in a Substring of Given Length
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Difficulty: Medium
# Language: python3

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        current_vowels = 0

        # first window
        for char in s[:k]:
            if char in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Move the window
        for i in range(k, len(s)):
            new_char = s[i]
            old_char = s[i - k]

            if new_char in vowels:
                current_vowels += 1

            if old_char in vowels:
                current_vowels -= 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
