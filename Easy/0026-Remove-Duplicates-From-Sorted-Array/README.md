# Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Topics:** Array, Two Pointers  
**LeetCode URL:** [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem Description

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>
<p>Consider the number of <em>unique elements</em> in <code>nums</code> to be <code>k<strong>​​​​​​​</strong></code>​​​​​​​. <meta charset="utf-8"/>After removing duplicates, return the number of unique elements <code>k</code>.</p>
<p><meta charset="utf-8"/>The first <code>k</code> elements of <code>nums</code> should contain the unique numbers in <strong>sorted order</strong>. The remaining elements beyond index <code>k - 1</code> can be ignored.</p>
<p><strong>Custom Judge:</strong></p>
<p>The judge will test your solution with the following code:</p>
<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>
<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

## Solution

```python
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

```
