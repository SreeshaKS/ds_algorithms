def cV(v):
    return [ x[:] for x in v]

def move(m, v, i, j, steps, path, modified, check):
    s1 = s2 = 99999
    if m[i][j] == 0:
        s1 = solve(m, cV(v), i, j, steps, path+[(i,j)], modified,check)
        return s1
    elif not modified:
        s2 = solve(m, cV(v), i, j, steps, path+[(i,j,True)], True,check)
        return s2
    return 99999

def solve(m, v, i, j, steps, path, modified, check):
    r = len(m)
    # print(i,j,path)
    # mark as visisted
    v[i][j] = True
    minSteps = [99999]

    # loops through each cardinal direction
    for p in [ [1, 0], [0, 1], [-1, 0], [0, -1] ]:
        x, y = i + p[0], j + p[1]
        if 0 <= x < r and 0 <= y < len(m[x]) and not v[x][y]:
            minSteps.append(
                move(m, v, x, y, steps + 1, path, modified, check)
            )   
    if check(i, j, m):
        return steps+1
    return min(minSteps)

def solution(m):
    def check(i,j,m):
        return  i == 0 and j == 0
        # return  i == len(m) - 1 and j == len(m[i])-1
    visited = [[False]*len(x) for x in m]
    return solve(m, visited, len(m) - 1, len(m[0]) - 1, 0 , [], False, check)


# s = solution([
#     [0, 1, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1, 0, 1], 
#     [1, 1, 1, 1, 1, 0, 1], 
#     [1, 1, 1, 1, 1, 0, 0]
# ])
# print(s)

s = solution([
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
])
print(s)

# s = solution(
#     [
#         [0, 1, 1, 0], 
#         [0, 0, 0, 1], 
#         [1, 1, 0, 0], 
#         [1, 1, 1, 0]
#     ]
# )
# print(s)

# s= solution([
#     [0, 0, 0, 0, 0, 0], 
#     [1, 1, 1, 1, 1, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 1, 1, 1, 1, 1], 
#     [0, 1, 1, 1, 1, 1], 
#     [0, 0, 0, 0, 0, 0]
# ])
# print(s)