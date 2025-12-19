"""
Problem

You’re given a string s.
Return the number of vowels in the string.

For this problem, vowels are:
a e i o u


input : s = "leetcode"
output : 4

simplify: we have a list of our vowels and we iterate through the string: if the string char is in our list then we increment our count by 1


"""

s = "leetcode"
vowels = ['a', 'e', 'i', 'o', 'u']
def numVowels(s):
  ans = 0
  for char in s:
    if char in vowels:
      ans += 1
  return ans

print(numVowels(s))