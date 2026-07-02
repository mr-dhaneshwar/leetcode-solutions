# LeetCode Problem: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Language: python3

class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**31 - 1

        negative = False
        if x < 0:
            negative = True
            x = -x

        ans = 0

        while x > 0:
            last = x % 10
            x = x // 10

            if ans > limit // 10 or (ans == limit // 10 and last > 7):
                return 0

            ans = ans * 10 + last

        if negative:
            ans = -ans

        return ans
