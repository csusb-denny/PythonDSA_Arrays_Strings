"""
Docstring for moveZeros

Question 7 — Move Zeros
Problem (fully stated)

You’re given an integer array nums.
Move all 0s to the end of the array while maintaining the relative order of the non-zero elements.

You must do this in-place.

"""

nums = [0, 1, 0, 3, 12]

def movezeros(nums):
  write = 0 #starting at the 0 index, it should be non zeros ->

  for read in range(len(nums)):
    if nums[read] != 0: 
      nums[write], nums[read] = nums[read], nums[write]
      write += 1
  return nums
  
print(movezeros(nums))
