def product(leftProduct, arr, i, res):
  if i < len(arr):
    rightProduct = product( leftProduct * arr[i] , arr, i+1, res )
    res[i] = leftProduct * rightProduct
    return rightProduct * arr[i]
  return 1

def array_of_array_products(arr):
  if len(arr) == 0 or len(arr) == 1:
    return []
  res = [1] * len(arr)
  product( 1, arr, 0, res)
  return res


"""

Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 20
[output] array.integer
"""