def find_pairs_with_given_difference(arr, k):
  diffs = {}
  for y in arr:
     diffs[y-k] = y
  
  result=[]
  i = 0
  while i < len(diffs):
    try:
      if arr[i] in diffs:
         result.append([ diffs[arr[i]], arr[i] ])
    except:
      pass
    i+=1
  return result


'''
Pairs with Specific Difference
A naive approach is is to run two loops. The outer loop picks the first element (smaller element) and the inner loop looks up for the element picked by the outer loop plus k. While this solution is done in O(1) space complexity, its time complexity is O(N^2), which isn’t asymptotically optimal.

We can use a hash map to improve the time complexity to O(N⋅log(N)) for the worst case and O(N) for the average case. We rely on the fact that if x - y = k then x - k = y.

The first step is to traverse the array, and for each element arr[i], we add a key-value pair of (arr[i] - k, arr[i]) to a hash map. Once the map is populated, we traverse the array again, and check for each element if a match exists in the map.

Both the first and second steps take O(N⋅log(N)) for the worst case and O(N) for the average case. So the overall time complexity is O(N) for the average case.

Pseudocode:

function findPairsWithGivenDifference(arr, k):
    # since we don't allow duplicates, no pair can satisfy x - 0 = y
    if k == 0:
        return []
        
    map = {}
    answer = []
    
    for (x in arr):
        map[x - k] = x
    
    for (y in arr):
        if y in map:
            answer.push([map[y], y]) 

    return answer
Time Complexity: a generic hash map insert/lookup takes O(N) in the worst case. However, since we’re storing numbers, we can use a hash map that is based on a Binary Search Tree, and reduces inserts and lookups to O(log(N)). For the average case these operations take O(1). The while loop is O(N) since we go through every element in the array. So the total time complexity is O(N⋅log(N)) + O(N⋅log(N)) = O(N·log(N)) for the worst case, and O(N) + O(N) = O(N) for the average case.

Space Complexity: since the size of the output itself is O(N), the space complexity is O(N) as well. The map we added will only hold N elements, and won’t increase the space complexity.
'''