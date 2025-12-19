"""
Problem

You’re given an integer array nums.
Return True if the array is sorted in non-decreasing order, otherwise return False.

Non-decreasing means: each element is greater than or equal to the previous one.

nums = [1,2,3,4,5]
return True

nums[3,2,4] return false

simplify:
if the next index is less than the previous index than return false
otherwise return True

"""
nums = [1,2,4]
def checkSorted(nums):
  i = 0
  while i < len(nums) - 1:
    if nums[i] > nums[i+1]:
      return False
    i += 1
    return True
  
print(checkSorted(nums))
