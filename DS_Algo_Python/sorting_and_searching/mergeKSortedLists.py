
import heapq
def mergeKLists( lists):
    
    mL = [[1,4,5],[1,3,4],[2,6]]
    return list(heapq.merge(*mL))
print(mergeKLists([]))