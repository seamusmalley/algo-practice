"""
problem
	- input: two non-empty arrays of ints
	- output: array of one int from each list with the smallest absolute dif
	- only one pair with the smallest dif

brute force solution
	- for each item in list a, go throught list b
	- for each pair, if its the smallest dif, save it and the two list items
	- time O(n^2)
	- space O(1)
"""

def smallest_difference_brute(arrayOne: [int], arrayTwo: [int]) -> [int]:
	i, j = arrayOne[0], arrayTwo[0]
	smallest_dif = abs(i - j)

	for x in arrayOne:
		for y in arrayTwo:
			dif = abs(x - y)

			if dif < smallest_dif:
				i, j = x, y
				smallest_dif = dif

	return [i, j]

"""
solution
	- sort each list
	- starting at the left side of each list, indices i and j
	- if the dif of a1[i] and a2[j] is smaller than any seen dif, store it, i, and j
	- if a1[i] < a2[j], i++, else j++
	- time O(n*lg(n))
	- space O(1)
"""

def smallest_difference(arrayOne: [int], arrayTwo: [int]) -> [int]:
	arrayOne.sort()
	arrayTwo.sort()

	"""
	x = arrayOne[i]
	y = arrayTwo[j]
	"""

	i, j = 0, 0
	x, y = arrayOne[0], arrayTwo[0]
	smallest_dif = abs(arrayOne[i] - arrayTwo[j])

	while i < len(arrayOne) and j < len(arrayTwo):
		dif = abs(arrayOne[i] - arrayTwo[j])
		if dif < smallest_dif:
			x, y = arrayOne[i], arrayTwo[j]
			smallest_dif = dif

		if arrayOne[i] < arrayTwo[j]:
			i += 1
		else:
			j += 1

	return [x, y]


"""
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
->
arrayOne = [-1, 3, 5, 10, 20, 28]
arrayTwo = [15, 17, 26, 134, 135]
"""

print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))