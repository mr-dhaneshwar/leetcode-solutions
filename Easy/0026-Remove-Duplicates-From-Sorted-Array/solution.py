# LeetCode Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Language: python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
