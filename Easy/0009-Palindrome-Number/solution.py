# LeetCode Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Language: python

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
