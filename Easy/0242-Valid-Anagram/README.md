# Valid Anagram

**Difficulty:** Easy  
**Topics:** Hash Table, String, Sorting  
**LeetCode URL:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Problem Description

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "anagram", t = "nagaram"</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>
<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "rat", t = "car"</span></p>
<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>
<p> </p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

## Solution

```python
# LeetCode Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Language: python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}

        for ch in s:
            mapping[ch] = mapping.get(ch, 0) + 1

        for ch in t:
            if ch not in mapping:
                return False

            mapping[ch] -= 1

            if mapping[ch] < 0:
                return False

        return True

```
