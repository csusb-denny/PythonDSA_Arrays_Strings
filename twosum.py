"""
dry run:
ans = empty, complement = 7, 
ans[2] = 0

ans = [2:0, ]
complement = 2
if complement in ans: return
return [0,1]
"""
def twosum(nums, target):
  ans = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in ans:
      return [ans.get(complement, 0), i]
    ans[nums[i]] = i
  return []

def run_tests():
  tests = [
    ([2, 7, 11, 15], 9, [[0, 1]]),
    ([1, 2, 3], 7, [[]]),
    ([3, 3], 6, [[0, 1]]),
    ([1, 2, 3, 4, 5], 6, [[0, 4], [1, 3]]),
    ([0, 4, 3, 0], 0, [[0, 3]]),
    ([-1, -2, -3, -4, -5], -8, [[2, 4]]),
    ([1, 5, 1], 2, [[0, 2]]),
    ([5], 5, [[]]),
  ]

  for nums, target, expected_any in tests:
    result = twosum(nums, target)
    if expected_any == [[]]:
      ok = result == []
    else:
      ok = result in expected_any
    status = "PASS" if ok else "FAIL"
    print(f"{status} nums={nums} target={target} result={result}")

if __name__ == "__main__":
  run_tests()
     
