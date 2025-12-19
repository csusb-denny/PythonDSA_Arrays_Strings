"""
Next Problem — Question 10: Remove Duplicates (Sorted Array)

Problem

You’re given a sorted integer array nums.
Remove duplicates in-place and return the new length.

The first k elements of nums should contain the unique values.

⸻
"""

nums = [1, 1, 2, 2, 3]

def removeDupes(nums):
  prev = 0
  for i in range(1, len(nums)):
    if nums[prev] !=  nums[i]:
      prev += 1 
      nums[prev] = nums[i]
  return prev + 1
    
print(removeDupes(nums))