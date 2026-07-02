# LeetCode Problem: Find the Difference
# Link: https://leetcode.com/problems/find-the-difference/
# Difficulty: Easy
# Language: python3

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for ch in s + t:
            result ^= ord(ch)

        return chr(result)
        
