""
🔹 Problem 2: Longest Repeating Character Replacement
📌 Problem statement

You are given:

a string s

an integer k

You may replace at most k characters in the string.

Return the length of the longest substring that can be made of all the same character after at most k replacements.
"""

"""
Test Cases:
Input:  s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'B's → "AAAA"

Input:  s = "AABABBA", k = 1
Output: 4
Explanation: "AABA" or "BABB"
"""
from collections import defaultdict

def longestRepeats(s, k):
  left = 0
  map = defaultdict{}
  max_window = 0
  largest = 0
  for i in range(len(s)):
    map[s[i]] += 1
     