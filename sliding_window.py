"""
Problem 1
	- Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
	- Example 1:
		- Input: [2, 1, 5, 1, 3, 2], k=3
		- Output: 9
		- Explanation: Subarray with maximum sum is [5, 1, 3].
	- Example 2:
		- Input: [2, 3, 4, 1, 5], k=2
		- Output: 7
		- Explanation: Subarray with maximum sum is [3, 4].
"""


# brute force: O(n*k)
def find_max_subarray(array: [int], k: int) -> int:
	max_sum = 0
	for i in range(len(array)-k):
		sum = sum(array[i:i+k])
		if sum > max_sum:
			max_sum = sum

	return max_sum

# sliding window: O(n)
def find_max_subarray(array: [int], k: int) -> int:
	window_start, window_sum, max_sum= 0, 0, 0

	for window_end in range(len(array)):
		window_sum += array[window_end]
		if window_end >= k-1:
			if window_sum > max_sum:
				max_sum = window_sum
			window_sum -= array[window_start]
			window_start += 1

	return max_sum


"""
Problem 2
	- Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
	- Example 1:
		- Input: [2, 1, 5, 2, 3, 2], S=7
		- Output: 2
		- Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
	- Example 2:
		- Input: [2, 1, 5, 2, 8], S=7
		- Output: 1
		- Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
	- Example 3:
		- Input: [3, 4, 1, 1, 6], S=8
		- Output: 3
		- Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
		  or [1, 1, 6].
"""


def find_smallest_subarray_size(array: [int], target: int) -> int:
	window_start = 0
	min_size = len(array)
	window_sum = 0

	for window_end in range(len(array)):
		window_sum += array[window_end]

		while window_sum >= target:
			min_size = min(min_size, window_end - window_start + 1)
			window_sum -= array[window_start]
			window_start += 1

	return min_size


# print(find_smallest_subarray_size([3, 4, 1, 1, 6], 8))


"""
Problem 3
	- Given a string, find the length of the longest substring in it with no more than K distinct characters.
	- Example 1:
		- Input: String="araaci", K=2
		- Output: 4
		- Explanation: The longest substring with no more than '2' distinct characters is "araa".
	- Example 2:
		- Input: String="araaci", K=1
		- Output: 2
		- Explanation: The longest substring with no more than '1' distinct characters is "aa".
	- Example 3:
		- Input: String="cbbebi", K=3
		- Output: 5
		- Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def find_max_substring(string: str, k: int) -> int:
	window_start, max_size = 0, 0, 0
	chars = {}

	for window_end in range(len(string)):
		char = string[window_end]
		if char not in chars:
			chars[char] = 0
		chars[char] += 1

		while len(chars) > k:
			chars[string[window_start]] -= 1
			if chars[string[window_start]] == 0:
				del chars[string[window_start]]
			window_start += 1

		max_size = max(max_size, window_end - window_start + 1)

	return max_size


"""
Problem 4
	- Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
	- You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
	- Write a function to return the maximum number of fruits in both baskets.
	- Example 1:
		- Input: Fruit=['A', 'B', 'C', 'A', 'C']
		- Output: 3
		- Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
	- Example 2:
		- Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
		- Output: 5
		- Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
		- This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def find_max_fruits(trees: [str]) -> int:
	max_fruits = 0
	basket = {}

	window_start = 0
	for window_end in range(len(trees)):
		fruit = trees[window_end]
		if fruit not in basket:
			basket[fruit] = 0
		basket[fruit] += 1

		while len(basket) > 2:
			old_fruit = trees[window_start]
			basket[old_fruit] -= 1
			if basket[old_fruit] == 0:
				del basket[old_fruit]
			window_start += 1

		max_fruits = max(max_fruits, window_end - window_start + 1)

	return max_fruits


#print(find_max_fruits(['A', 'B', 'C', 'A', 'C']))
#print(find_max_fruits(['A', 'B', 'C', 'B', 'B', 'C']))


"""
Problem 5
	- Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
	- Example 1:
		- Input: String="aabccbb", k=2
		- Output: 5
		- Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
	Example 2:
		- Input: String="abbcb", k=1
		- Output: 4
		- Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
	Example 3:
		- Input: String="abccde", k=1
		- Output: 3
		- Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

def find_longest_substring_with_replacement(string: str, k: int) -> int:
	result = 0
	found = {}
	window_start = 0
	max_freq = 0
	
	for window_end in range(len(string)):
		char_end = string[window_end]
		if char_end not in found:
			found[char_end] = 0
		found[char_end] += 1
		max_freq = max(max_freq, found[char_end])
		
		if (window_end - window_start + 1) - max_freq > k:
			char_start = string[window_start]
			found[char_start] -= 1
			if found[char_start] == 0:
				del found[char_start]
			window_start += 1
		
		result = max(result, window_end - window_start + 1)
		
	return result

print(find_longest_substring_with_replacement('aabccbb', 2))
print(find_longest_substring_with_replacement('abbcb', 1))
print(find_longest_substring_with_replacement('abccde', 1))