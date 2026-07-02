# LeetCode Problem: Final Value of Variable After Performing Operations
# Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Difficulty: Easy
# Language: python3

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if "+" in op:
                res += 1
            else:
                res -= 1
        return res
        
