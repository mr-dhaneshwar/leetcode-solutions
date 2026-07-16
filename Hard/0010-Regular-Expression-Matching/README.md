# Regular Expression Matching

**Difficulty:** Hard  
**Topics:** String, Dynamic Programming, Recursion  
**LeetCode URL:** [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

## Problem Description

<p>Given an input string <code>s</code> and a pattern <code>p</code>, implement regular expression matching with support for <code>'.'</code> and <code>'*'</code> where:</p>
<ul>
<li><code>'.'</code> Matches any single character.​​​​</li>
<li><code>'*'</code> Matches zero or more of the preceding element.</li>
</ul>
<p>Return a boolean indicating whether the matching covers the entire input string (not partial).</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "aa", p = "a"
<strong>Output:</strong> false
<strong>Explanation:</strong> "a" does not match the entire string "aa".
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "aa", p = "a*"
<strong>Output:</strong> true
<strong>Explanation:</strong> '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "ab", p = ".*"
<strong>Output:</strong> true
<strong>Explanation:</strong> ".*" means "zero or more (*) of any character (.)".
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= s.length &lt;= 20</code></li>
<li><code>1 &lt;= p.length &lt;= 20</code></li>
<li><code>s</code> contains only lowercase English letters.</li>
<li><code>p</code> contains only lowercase English letters, <code>'.'</code>, and <code>'*'</code>.</li>
<li>It is guaranteed for each appearance of the character <code>'*'</code>, there will be a previous valid character to match.</li>
</ul>

## Solution

```python
# LeetCode Problem: Regular Expression Matching
# Link: https://leetcode.com/problems/regular-expression-matching/
# Difficulty: Hard
# Language: python

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern exhausted
            if j == len(p):
                return i == len(s)

            # Current characters match?
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # Next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = (
                    dp(i, j + 2) or              # Skip x*
                    (first_match and dp(i + 1, j))  # Use x*
                )
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

```
