"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example 1:
    - Input: String = "oidbcaf", Pattern = "abc"
    - Output: True, "bca"

Example 2:
    - Input: String = "odicf", Pattern = "dc"
    - Output: False

Example 3: 
    - Input: String = "bcdxabcdy", Pattern = "bcdyabcdx"
    - Output: True

Example 4:
    - Input: String = "aaaacb", Pattern = "abc"
    - Output: True, "acb"

"""

def permutation_search(string: str, pattern: str) -> bool:
    pattern_map = {}
    for char in pattern:
        if char not in pattern_map:
            pattern_map[char] = 0
        pattern_map[char] += 1

    window_start = 0
    for window_end in range(len(string)):
        char_end = string[window_end]

        if char_end in pattern_map and pattern_map[char_end] > 0:
            pattern_map[char_end] -= 1
        else:
            while window_start <= window_end:
                char_start = string[window_start]
                if char_start in pattern_map:
                    pattern_map[char_start] += 1
                window_start += 1

        if (window_end - window_start + 1) == len(pattern):
            return True

    return False


# Tests
print(permutation_search("oidbcaf", "abc"))
print(permutation_search("odicf", "dc"))
print(permutation_search("bcdxabcdy", "bcdyabcdx"))
print(permutation_search("aaacb", "abc"))