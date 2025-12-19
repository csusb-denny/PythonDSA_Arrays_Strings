"""
Alright — Question 1 (Easy)

Problem: Find the Maximum

You’re given an integer array nums.
Return the largest value in the array.

Input

nums = [3, 7, 2, 9, 5]

Output

9

Another example

nums = [-8, -3, -10, -2]

Output: -2
"""

"""
simplify the problem:
Its asking us to return the largest int inside the list of ints
input will be a list of ints
output will be the largest number in the list

pattern recognition:
this will be done in one loop through the list
store the largest number in a variable, return that ans at end

implementation plan
set our ans = the first index so nums[0]
start our loop from nums[1:]
if index value is > than ans then update ans until end of list,
return ans
"""

def returnLargest()