













from heapq import heapify, heappop, heappush

def sort_k_messed_array(arr, k):
  heap = arr[:k+1]
  
  heapify(heap)
  i =0 
  for index in range(k+1, len(arr)):
    arr[i] = heappop(heap)
    heappush(heap, arr[index])
    i+=1
    
  while len(heap) > 0:
    arr[i] = heappop(heap)
    i+=1
  
  return  arr # your code goes here

#(n-k) * 1 + (n-k)*log(k)  + (n-k)*1

#2n-1k + (n-k) * log(k)

#O((n-k) * log(k))

#O(k)