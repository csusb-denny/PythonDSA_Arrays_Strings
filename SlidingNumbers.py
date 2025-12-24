"""
(Foundational & confidence-building)
📌 Problem: Maximum Sum Subarray of Size K
Problem statement

You are given:

an array of integers nums

an integer k

Return the maximum sum of any contiguous subarray of size k.

nums = [2, 1, 5, 1, 3, 2]
k = 3


valud subarrays of size 3:
2 1 5 = 8
1 5 1 = 7 
5 1 3 = 9
1 3 2 = 6
"""
nums = [2, 1, 5, 1, 3, 2]
k = 3

def maxSum(nums, k):
  if len(nums) < k:
    return 0
  
  current_sum = sum(nums[:k])
  max_sum = current_sum

  for i in range(k, len(nums)):
    
    current_sum += nums[i] #add element to the right
    current_sum -= nums[i - k] #remove element to the left
    max_sum = max(max_sum, current_sum)

  return max_sum
print(maxSum(nums, k))