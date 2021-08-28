"""
problem
	- in [int], len n, n > 0, sorted
	- out [int], len n, sorted
	- new array, not in place
	- need to handle negatives

simple solution
	- create arr2 with size of arr1
	- arr2[i] = arr1[i]^2
	- sort arr2
	- time: O(nlgn), space: O(n)

obsersvations
	- when numbers are positive, their square increases as they increase
	- when numbers are negative, their square increases as they decrease
	- squares of sorted negative integers are sorted, just in reverse order

solution
	- if arr[i] is negative, square it and put it in arrNeg
	- if arr[i] is positive, square it and put it in arrPos
	- starting at the beginning of arrPos and end of arrNeg, zip merge them
	- O(n) time, O(n) space
"""

def sorted_squared_array(array: [int]) -> [int]:
	pos, neg = [], []
	for x in array:
		if x < 0:
			neg.append(x*x)
		else:
			pos.append(x*x)

	if pos:
		p = pos.pop(0)
	else:
		return neg.reverse()

	if neg:
		n = neg.pop()
	else:
		return pos

	result = []
	while pos and neg:
		if n < p:
			result.append(n)
			n = neg.pop()
		else:
			result.append(p)
			p = pos.pop(0)

	while pos:
		result.append(pos.pop(0))
	while neg:
		result.append(neg.pop())

	return result
