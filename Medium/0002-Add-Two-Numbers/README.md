# Add Two Numbers

**Difficulty:** Medium  
**Topics:** Linked List, Math, Recursion  
**LeetCode URL:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Problem Description

<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.</p>
<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;"/>
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>
<p> </p>

## Constraints

<ul>
<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
<li><code>0 &lt;= Node.val &lt;= 9</code></li>
<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

## Solution

```python
# LeetCode Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Language: python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

        return dummy.next

```
