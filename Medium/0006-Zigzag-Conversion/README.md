# Zigzag Conversion

**Difficulty:** Medium  
**Topics:** String  
**LeetCode URL:** [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)

## Problem Description

<p>The string <code>"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>
<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>
<p>And then read line by line: <code>"PAHNAPLSIIGYIR"</code></p>
<p>Write the code that will take a string and make this conversion given a number of rows:</p>
<pre>
string convert(string s, int numRows);
</pre>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "PAYPALISHIRING", numRows = 3
<strong>Output:</strong> "PAHNAPLSIIGYIR"
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "PAYPALISHIRING", numRows = 4
<strong>Output:</strong> "PINALSIGYAHRPI"
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "A", numRows = 1
<strong>Output:</strong> "A"
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= s.length &lt;= 1000</code></li>
<li><code>s</code> consists of English letters (lower-case and upper-case), <code>','</code> and <code>'.'</code>.</li>
<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>

## Solution

```python
# LeetCode Problem: Zigzag Conversion
# Link: https://leetcode.com/problems/zigzag-conversion/
# Difficulty: Medium
# Language: python

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = -1  # 1 = down, -1 = up

        for char in s:
            rows[current_row] += char

            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            current_row += direction

        return "".join(rows)

```
