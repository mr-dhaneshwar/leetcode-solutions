# LeetCode Problem: Maximum Number of Words Found in Sentences
# Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Difficulty: Easy
# Language: python3

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(sentence.count(" ") + 1 for sentence in sentences)
