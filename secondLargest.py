"""
Youre given an integer array nums with at least 2 elements.
Return the second largest value in the array.

The array is not guaranteed to be sorted

Duplicate values do count

You must do this in one pass

nums = [5, 1, 9, 3, 7]
expected output: 7

simplify problem:
first we can sort the array, and return the 2nd to last index
or
i can have a current, and maxLargest, and previousLargest
ill set max Largest to index0, 
if current is larger than max largest ill set:
previousLarge = maxLarg
and MaxLarg = current
"""

nums = [5, 1, 9, 3, 7]

def secondLargest(nums):
  Largest = nums[0]
  second = nums[1]
  if second > Largest:
    Largest, second = second, Largest
  for value in nums[2:]:

    if value > Largest:
      second = Largest
      Largest = value
    if value < Largest and value > second:
      second = value
  return second

print(secondLargest(nums))