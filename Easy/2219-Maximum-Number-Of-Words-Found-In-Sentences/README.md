# Maximum Number of Words Found in Sentences

**Difficulty:** Easy  
**Topics:** Array, String  
**LeetCode URL:** [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)

## Problem Description

<p>A <strong>sentence</strong> is a list of <strong>words</strong> that are separated by a single space with no leading or trailing spaces.</p>
<p>You are given an array of strings <code>sentences</code>, where each <code>sentences[i]</code> represents a single <strong>sentence</strong>.</p>
<p>Return <em>the <strong>maximum number of words</strong> that appear in a single sentence</em>.</p>
<p> </p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> sentences = ["alice and bob love leetcode", "i think so too", <u>"this is great thanks very much"</u>]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> sentences = ["please wait", <u>"continue to fight"</u>, <u>"continue to win"</u>]
<strong>Output:</strong> 3
<strong>Explanation:</strong> It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
</pre>
<p> </p>

## Constraints

<ul>
<li><code>1 &lt;= sentences.length &lt;= 100</code></li>
<li><code>1 &lt;= sentences[i].length &lt;= 100</code></li>
<li><code>sentences[i]</code> consists only of lowercase English letters and <code>' '</code> only.</li>
<li><code>sentences[i]</code> does not have leading or trailing spaces.</li>
<li>All the words in <code>sentences[i]</code> are separated by a single space.</li>
</ul>

## Solution

```python
# LeetCode Problem: Maximum Number of Words Found in Sentences
# Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Difficulty: Easy
# Language: python3

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(sentence.count(" ") + 1 for sentence in sentences)

```
