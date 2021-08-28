"""
Feedback:
    - start with the problem
  	- reiterate the requirements
    - inputs/outputs
      - constraints
      - assumptions about the problem
    - Make obsersations about the problem
    - explicit observations
    - brute force
    - talk about time, space, why it's not optimal
    - make more observations on what could be done better
    - do the brute force

    - derive a more optimal solution
    - why it's better, do the psudo code
    - write out process, then code it up
    - write test cases and walk through

    - don't memorize problems
    - better naming
    - clear code

"""

"""
for i in range(len(array)):
    for j in range(i, len(array)):
  	if a[i] + a[j]



    array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetSum = 10

  ->

  array = [-4, -1, 1, 3, 5, 6, 8, 11]
        *                  *

    -4 + 11 = 7
    -1 + 11 = 10

    [-1, 11]


-------------------------------------

    targetSum = 100
    array = [-4, -1, 1, 3, 5, 6, 8, 11]
  											          **

-------------------------------------

    array = []
  targetSum = 10

-------------------------------------

  array = [10]
  targetSum = 10


time: O(nlg(n))
space: O(n) / O(1)

"""


def two_sum(array: [int], targetSum: int) -> [int]:
  # O(nlg(n))
    array.sort()
    left, right = 0, len(array) - 1

  # O(n)
    while (left < right):
    currentSum = array[left] + array[right]
    if currentSum == targetSum:
    	return [array[left], array[right]]
    elif currentSum > targetSum:
        right -= 1
    elif currentSum < targetSum:
        left += 1

    return []



# ---------------------------------------------------------------

"""
1. look at a value
2. look at map to see if (targetSum-currentValue) is there

targetSum - currentValue = desiredValue

if desiredValue in map
 	return [currentValue, desiredValue]

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

map = {
    3: 0,
        5: 1,
        -4: 2,
        8: 3,
        ...
      }


time: o(n)
space: o(n)
"""
