def solution(A,N,L):
    # A = [20 5 10]
    A.sort(reverse=True)
    # A = [20 10 5]
    i = 0
    tE = 1
    print(A)
    while i < len(A):
        d = A[i] * tE
        print(A[i],d)
        if d > L:
            return False
        tE += 1
        i+=1
    return True

print(solution( [20,5, 10], 3, 50 ) )