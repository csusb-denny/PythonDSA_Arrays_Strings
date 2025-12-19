"""
Docstring for validPalindrome
Question 12 — Valid Palindrome (Ignore Case & Non-Alphanumeric)

Problem

You’re given a string s.
Return True if it is a palindrome, otherwise return False.

This time:
	•	Ignore case
	•	Ignore non-alphanumeric characters
  s = "A man, a plan, a canal: Panama"
  output: True

simplify the problem:
check if the string is a palindrome, ignore the spaces and special characters...
i can use two pointers and skip if the pointers ever touch a non alphabetical character.
"""

s = "A man, a plan, a canal: Panama"

def validPalin(s):
  s = s.lower()
  l = 0
  r = len(s) - 1
  while l < r:
    while not s[l].isalnum():
      l += 1
    while not s[r].isalnum():
      r -= 1
    if s[l] == s[r]:
      l+=1
      r-=1
    else:
      return False
  return True

print(validPalin(s))