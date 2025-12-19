
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
"""
def rotate(nums, k):
  l = 0
  r = len(nums) - 1
  def reverse(l, r):

  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

  i = 0
  j = k - 1
  while i < j:
    nums[i], nums[j] = nums[j], nums[i]
    i += 1
    j -= 1

  final = len(nums) - 1
  while k < final:
    nums[k], nums[final] = nums[final], nums[k]
    k += 1
    final -= 1
  
  return nums

#print(rotate(nums, k))

"""

def rotatev2(nums, k):
  n = len(nums)
  k = k % n
  def reverse(l, r):
    while l < r:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1 
  reverse(0, n-1) #reverse entire array
  reverse(0, k-1) #reverse first k # elements
  reverse(k, n-1) #reverse remaining elements
  return nums

print(rotatev2(nums, k))