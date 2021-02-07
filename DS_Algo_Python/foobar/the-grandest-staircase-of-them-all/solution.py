def solution(n):
    sol = [1] + [0] * n
    for j in range(1, n+1):
        for i in range(n, j-1, -1):
            sol[i] += sol[i-j]
    return sol[n] - 1