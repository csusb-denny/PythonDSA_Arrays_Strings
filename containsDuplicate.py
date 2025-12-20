nums = [1, 2, 2, 4, 4, 4, 5]
"""
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
"""
def hashDupes(nums):
  exist = {}
  for num in nums:
    exist[num] = exist.get(num, 0) + 1
    if exist[num] > 1:
      return True
  return False