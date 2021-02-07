def binSearch(A,B):
    if A[0] == B:
        return 0
        
    if A[len(A)-1] == B:
        return len(A) - 1
    
    low = 0
    high = len(A) - 1
    mid = (low + high) // 2
    
    while low < high:
        print(low,high)
        if A[mid] == B:
            return mid
        
        if A[mid] < B:
            high = mid
        else:
            low = mid + 1
        
        mid = (low + high) // 2
    return -1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pP = 0
        i = 0
        
        if A[0] == B:
            return 0
        
        if A[len(A)-1] == B:
            return len(A) - 1

        while i < len(A) - 1:
            if A[i+1] < A[i]:
                pP = i
                break
            i+=1
        
        a1 = A[0:pP+1]
        a2 = A[pP+1:]

        i1 = binSearch(a1,B)
        if i1 != -1:
            return i1
        
        i2 = binSearch(a2,B)
        if i2 != -1:
            return i2 + pP + 1
        
        return -1

s = Solution()

print(s.search( [5, 17, 100, 3], 6))