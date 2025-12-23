"""
🟡 Sliding Window + Hash Map — Practice Problem
Problem: Longest Substring With At Most K Distinct Characters

You are given:

A string s

An integer k

Return the length of the longest contiguous substring that contains at most k distinct characters.


s = "eceba"
k = 2
# Output: 3
# Explanation: "ece"

simplify the problem:
given a string and a int k,
K will be the number of ATMOST K distinct numbers
example: aa , k = 1 output:2. 

it looks like we want to return value of chars 

test case:

eceba, distinct char = 2
e c = 2 distinct chars
"""
from collections import defaultdict
def longest_k_distinct(s, k):
    left = 0
    max_length = 0
    map = defaultdict(int)

    for i in range(len(s)):
        map[s[i]] += 1

        while len(map) > k:
            map[s[left]] -= 1
            if map[s[left]] == 0:
                del map[s[left]]
            left += 1
        
        max_length = max(max_length, i - left + 1)
    return max_length




def run_tests():
    tests = [
        ("eceba", 2, 3),
        ("aa", 1, 2),
        ("aabacbebebe", 3, 7),
        ("abc", 2, 2),
        ("abc", 1, 1),
        ("", 2, 0),
        ("aaaa", 1, 4),
        ("abaccc", 2, 4),  # "accc"
    ]

    for s, k, expected in tests:
        result = longest_k_distinct(s, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} s={s} k={k} result={result} expected={expected}")


if __name__ == "__main__":
    run_tests()
