"""
🔹 Next Problem: Longest Substring Without Repeating Characters
Problem statement (read carefully)

Given a string s, find the length of the longest substring
that contains no repeating characters.

Input:  "abcabcbb"
Output: 3
Explanation: "abc"

Input:  "bbbbb"
Output: 1
Explanation: "b"

Input:  "pwwkew"
Output: 3
Explanation: "wke"
dry run pwwkew
p w w k e w
l
r
  r
    r
remove p
  l r
  largest(0, 2 - 1 + 1)
  largest = 2
  remove w
    l
    r
    largest = 1, 1
     l

dry run abcabcbb

a b c a b c b b
l
r
  r
    r
      r
      
remove a
  l r r #shift l + 1
  largest = max(0, 3 - 0 + 1)
  largest = 4 


"""
s = "bbbbb"

def longest_sub(s):
  left = 0
  largest = 0
  seen = set()
  for i in range(len(s)):
    while s[i] in seen:
      seen.remove(s[left])
      left += 1
      largest = max(largest, i - left + 1)
    seen.add(s[i])

  return largest

print(longest_sub(s))