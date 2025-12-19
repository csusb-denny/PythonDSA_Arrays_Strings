"""
Question 11 — Reverse Array In-Place

Problem

You’re given an array nums.
Reverse the array in place.

That means:
	•	❌ No extra arrays
	•	❌ No slicing helpers like [::-1]
	•	✅ Modify nums itself
  
  
  nums = [1, 2, 3, 4, 5]
  output = [5, 4, 3, 2, 1]


  simplify problem: turn the string around, swap index 0 and last index and leave middle  
  """

nums = [1, 2, 3, 4, 5]

def revArray(nums):
  left = 0
  right = len(nums) - 1
  while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
  return nums

print(revArray(nums))