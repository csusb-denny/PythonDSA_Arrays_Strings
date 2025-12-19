"""
input : nums 1 2 3 4 5 6
output evens: 3

simplify problem:
its basically asking if any number % 2 = 0 increment count by 1
return count
"""

nums = [1, 2, 3, 4, 6]
def returnEven(nums):
  ans = 0
  for value in nums:
    if value % 2 == 0:
      ans += 1
  return ans

print(returnEven(nums))