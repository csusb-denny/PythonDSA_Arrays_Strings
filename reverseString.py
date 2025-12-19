"""
given a string s:
return the reverse of the string

simplify problem:
  could iterate backwards and store into a list and print the list as a string

"""

s = "hello"

def revString(s):
  ans = []
  i = 0
  for char in s[::-1]:
    ans.append(char)
  return str(ans)

print(revString(s))
