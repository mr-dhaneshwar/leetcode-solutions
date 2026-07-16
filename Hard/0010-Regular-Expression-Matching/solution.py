# LeetCode Problem: Regular Expression Matching
# Link: https://leetcode.com/problems/regular-expression-matching/
# Difficulty: Hard
# Language: python

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern exhausted
            if j == len(p):
                return i == len(s)

            # Current characters match?
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # Next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = (
                    dp(i, j + 2) or              # Skip x*
                    (first_match and dp(i + 1, j))  # Use x*
                )
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
