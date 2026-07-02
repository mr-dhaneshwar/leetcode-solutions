# Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium  
**Topics:** String, Sliding Window  
**LeetCode URL:** [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

## Problem Description

<p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the maximum number of vowel letters in any substring of </em><code>s</code><em> with length </em><code>k</code>.</p>
<p><strong>Vowel letters</strong> in English are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "abciiidef", k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring "iii" contains 3 vowel letters.
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "aeiou", k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Any substring of length 2 contains 2 vowels.
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "leetcode", k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> "lee", "eet" and "ode" contain 2 vowels.
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
<li><code>s</code> consists of lowercase English letters.</li>
<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>

## Solution

```python
# LeetCode Problem: Maximum Number of Vowels in a Substring of Given Length
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Difficulty: Medium
# Language: python3

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        current_vowels = 0

        # first window
        for char in s[:k]:
            if char in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Move the window
        for i in range(k, len(s)):
            new_char = s[i]
            old_char = s[i - k]

            if new_char in vowels:
                current_vowels += 1

            if old_char in vowels:
                current_vowels -= 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels

```
