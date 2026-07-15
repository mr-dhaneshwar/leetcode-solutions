# Search Insert Position

**Difficulty:** Easy  
**Topics:** Array, Binary Search  
**LeetCode URL:** [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

## Problem Description

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>
<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution

```python
# LeetCode Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Language: python

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

```
