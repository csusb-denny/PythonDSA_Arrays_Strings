"""
return sum of elements from the list:
nums = [4, 1, 7, 3]
15

simplify problem
its asking us to add up all the items in the list
and return total

pattern recog
single pass add
implement
"""

nums = [4, 1, 7, 3]
def sumElements(nums):
  ans = 0
  for value in nums:
    ans += value
  return ans

print(sumElements(nums))