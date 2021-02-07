def solve(n,k):
    matrix = []
    return matrix

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n,k = [int(i) for i in input()]
        y = solve(n,k)
        if len(y) == 0:
            print("Case #{}: {}".format( t_itr+1, "IMPOSSIBLE" ) )
        else:
            print("Case #{}: {}".format( t_itr+1, "POSSIBLE" ) )
            for i in range(y):
                print(" ".join(y[i]))
