def shortestPath(sx, sy, m):
    w = len(m[0])
    h = len(m)
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] is None:
                board[nx][ny] = board[x][y] + 1
                if m[nx][ny] == 1:
                  continue
                arr.append((nx, ny)) 
                  
    return board

def solution(m):
  w = len(m[0])
  h = len(m)
  tb = shortestPath(0, 0, m)
  bt = shortestPath(h-1, w-1, m)

  ans = 2 ** 32-1
  for i in range(h):
      for j in range(w):
          if tb[i][j] and bt[i][j]:
              ans = min(tb[i][j] + bt[i][j] - 1, ans)
  return ans

# s = solution([
#     [0, 1, 1, 0],
#     [0, 0, 0, 1], 
#     [1, 1, 0, 0], 
#     [1, 1, 1, 0]
# ])

s= solution([
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
])

# [
#     [1, 2, 3, 4, 5, 6], 
#     [2, 3, 4, 5, 6, 7],
#     [13, 12, 11, 10, 9, 8], 
#     [14, 13, 12, 11, 10, 9],
#     [15, 16, 19, 20, 21, 22], 
#     [16, 17, 18, 19, 20, 21]
 
#  ]


# [
#     [21, 20, 19, 18, 17, 16], 
#     [10, 11, 12, 13, 14, 15],
#     [9, 10, 11, 12, 13, 14], 
#     [8, 9, 12, 13, 14, 15], 
#     [7, 6, 5, 4, 3, 2],
#     [6, 5, 4, 3, 2, 1]
# ]


print(s)