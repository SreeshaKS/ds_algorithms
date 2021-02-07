def pancake_sort(arr):
  i = 0
  n = len(arr)-1
  
  while i <= n:
    x = arr[0:n-i]
    print(x)
    largest = -1
    index = 0
    for idx, e in enumerate(x):
      if e > largest:
        largest = e
        index = idx
    arr = flip(arr,index+1)
    print(arr,index,i)
    arr = flip(arr,n-i)
    print(arr,n-i)
    i+=1
    return arr
def flip(arr,k):
  i = k
  while i >= 0:
    if i == k / 2:
        break
    arr[i], arr[k-i] = arr[k-i], arr[i]
    i-=1
  return arr

print( pancake_sort( [1, 3, 1] ) )