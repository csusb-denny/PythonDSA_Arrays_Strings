"""
Hash Map Practice — Problem 8 (Medium)
Problem: Longest Substring Without Repeating Characters

You are given a string s.

Return the length of the longest substring (contiguous) that contains no repeating characters.


s = "abcabcbb"
# Output: 3   ("abc")


#simplify the problem
first i want to loop through the string i believe:
once i find any char that recurrs, i will insert that as a key


"""
def longest(s):
  left = 0
  string_map = {}
  window_length = 0

  for i in range(len(s)):
      if s[i] in string_map and string_map[s[i]] >= left:
          left = string_map[s[i]] + 1

      string_map[s[i]] = i
      window_length = max(window_length, i - left + 1)

  return window_length

        



def run_tests():
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("aab", 2),
        ("dvdf", 3),
        ("anviaj", 5),
        ("abba", 2),
    ]

    for s, expected in tests:
        result = longest(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} s={s} result={result} expected={expected}")


if __name__ == "__main__":
    run_tests()
