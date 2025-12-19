def solve(nums, target):
    """
    Problem-solving function
    """
    seen = {}
    for index, value in enumerate(nums):
      complement = target - value    

      if complement in seen:
         return [seen[complement], index]
      seen[value] = index
    return []


if __name__ == "__main__":
    # local testing
    nums = [2, 7, 11, 15] 
    target = 9
    print(solve(nums, target))