# LeetCode Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Language: python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_map:
                return [num_map[complement], i]

            num_map[nums[i]] = i