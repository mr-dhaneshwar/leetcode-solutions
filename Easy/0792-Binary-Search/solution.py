# LeetCode Problem: Binary Search
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Language: python

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low+(high-low)/2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                low = mid+1
            else:
                high = mid-1

        return -1

        
