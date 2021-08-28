def validate_subsequence(array: [int], sequence: [int]) -> bool:
	if not array:
		return false
	if not sequence:
		return true

	if array[0] == sequence[0]:
		return validate_subsequence(array[1:], sequence[1:])
	else:
		return validate_subsequence(array[1:], sequence)

"""

arr = [5, 1, 22, 25, 6, -1, 8, 10]
       i

seq = [1, 6, -1, 10]
	   j

i, j = 0, 0
while i > len(arr) and j < len(seq)
	if arr[i] = seq[j]
		j++
	else
		i++

return (j > len(seq))

"""

def validate_subsequence(array: [int], sequence: [int]) -> bool:
	i, j = 0, 0
	while i < len(arr) and j < len(seq):
		if arr[i] == seq[j]:
			j += 1
		else:
			i += 1
	return j > len(seq)
