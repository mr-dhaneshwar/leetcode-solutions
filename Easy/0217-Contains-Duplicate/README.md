# Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Sorting  
**LeetCode URL:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Problem Description

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1]</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
<p><strong>Explanation:</strong></p>
<p>The element 1 occurs at the indices 0 and 3.</p>
</div>
<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>
<p><strong>Output:</strong> <span class="example-io">false</span></p>
<p><strong>Explanation:</strong></p>
<p>All elements are distinct.</p>
</div>
<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,3,3,4,3,2,4,2]</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## Solution

```python
# LeetCode Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Language: python3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        

```
