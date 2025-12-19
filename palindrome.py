"""
Question 8 — Palindrome String (Basic)

Problem

You’re given a string s.
Return True if the string is a palindrome, otherwise return False.

A palindrome reads the same forward and backward.

⸻
input : racecar
return True

input : hello
return False

simplify problem:

what is a palindrome? a word that can be read from backwards to forward:
how can i check if a word is a palindrome:
well i can just return if string == reversed.string
i can also use two pointers ?
left = 0
right = len(string) - 1
while left < right:
  if left == right:
    left +=1
    and right -=1
  return false
return true

"""


string = "h"

def isPalindrome(string):
  if len(string) == 1:
    return True

  left = 0
  right = len(string) - 1
  while left < right:
    if string[left] == string[right]:
      left += 1
      right -= 1
    else:
      return False
    return True

print(isPalindrome(string))
