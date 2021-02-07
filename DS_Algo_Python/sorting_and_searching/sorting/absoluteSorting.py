def absSort(arr):
  def sorting(a):
    return abs(a)
    
  arr.sort(key=sorting)
  
  i = 0
  start = 0
  while i < len(arr)-1:
    if abs(arr[i]) == abs(arr[i+1]):
      i+=1
    else:
      toBeSorted = arr[start:i+1]
      toBeSorted.sort()
      for j,d in enumerate(toBeSorted):
          arr[start+j] = d
      i+=1
      start = i
    
  return arr


absSort([2, -7, -2, -2, 0])

# return arr.sort((a, b) => {
#     if(Math.abs(a) < Math.abs(b)) {
#       return -1;
#     } else if(Math.abs(a) > Math.abs(b)) {
#       return 1;
#     } else if( a > b) {
#       return 1;
#     } else {
#       return -1;
#     }
#   });