"""
Hash Map Practice — Problem 3 (Easy → Medium)

Problem: First Unique Character

You are given a string s.

Return the index of the first character that appears exactly once in the string.

If no such character exists, return -1.

You should use a hash map.

s = "leetcode"
output: 0

l appears once and is the first such character
"""

s = "leetcode"
def uniqueChar(s):
  ans = {}
  for char in s:
    ans[char] = ans.get(char, 0) + 1
  for i in range(len(s)):
    if ans[s[i]] == 1: 
      return i
  return -1

print(uniqueChar(s))