"""
observations
	- can make hashmap of elements and desired values, like two sum
  	- make grid of element combinations
  	- parse grid and search hashmap to find third element
  	- output needs to be sorted

time: O(n^2)
space: O(n)
"""

def three_number_sum(array: [int], target_sum: int) -> [[int]]:
	array.sort()

	desired_values = {}
  	for x in array:
		desired_values[target_sum - x] = x

	result = []
  	for i in range(len(array)):
    	for j in range(i + 1, len(array)):
      		two_sum = array[i] + array[j]
      		if two_sum in desired_values:
        		k = desired_values[two_sum]
        		if k > array[i] and k > array[j]:
          			result.append([array[i], array[j], k])

	return result


array = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0
