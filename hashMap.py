"""
🟢 Hash Map Practice — Problem 2 (Easy)

Problem: First Repeating Character

You are given a string s.

Return the first character that appears more than once in the string.

If no character repeats, return None.

You should use a hash map to track what you’ve seen.

⸻
s: leetcode
output e
"""

s = "leetcode"

def hashMap(s):
  map = {}
  for char in s:
    if char in map:
      return char
    map[char] = 1
  return []
print(hashMap(s))
