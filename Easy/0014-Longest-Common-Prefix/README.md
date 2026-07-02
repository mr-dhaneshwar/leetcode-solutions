# Longest Common Prefix

**Difficulty:** Easy  
**Topics:** Array, String, Trie  
**LeetCode URL:** [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Problem Description

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>
<p>If there is no common prefix, return an empty string <code>""</code>.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= strs.length &lt;= 200</code></li>
<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>

## Solution

```python
# LeetCode Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Language: python3

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            i = 0

            while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
                i += 1

            prefix = prefix[:i]

            if not prefix:
                return ""

        return prefix

```
