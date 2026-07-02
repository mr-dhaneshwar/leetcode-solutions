# Reverse Integer

**Difficulty:** Medium  
**Topics:** Math  
**LeetCode URL:** [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

## Problem Description

<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>
<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>
<p> </p>

## Constraints

<ul>
<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## Solution

```python
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

```
