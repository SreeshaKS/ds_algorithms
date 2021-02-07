# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Graph:
    
    def __init__(self, row,col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
    
    def isSafe(self, i, j, visited):
        
        bounded = i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j] == "1"
        
        return bounded
    
    def DFS(self, i, j, visited):
        
        visited[i][j] = True
        
        for k in [ [1, 0], [0, 1], [-1, 0], [0, -1] ]:
            
            cI, cJ = i + k[0], j + k[1]
            
            if self.isSafe(cI, cJ, visited):
                self.DFS(cI, cJ, visited)

    def countIsLands(self):
        
        visited = [ [ False ] * self.COL for i in range(self.ROW) ]
        count = 0
        
        for i in range(self.ROW):
            
            for j in range(self.COL):
                
                if visited[i][j] == False and self.graph[i][j] == "1":
                    self.DFS(i, j, visited)
                    count += 1
        
        return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid) 
        if row > 0:
            col = len(grid[0]) 

            g = Graph(row, col, grid) 
            return g.countIsLands()
        return 0