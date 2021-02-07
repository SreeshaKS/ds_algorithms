def sudoku_solve(board):
    #Time Complexity: O(9^(m * n)) - Brute Foirce
    #Time Complexity: O(9!^9)
    #Space Complexity: O(m*n)
    rows = len(board)
    cols = len(board[0])

    def print_board():
      for row in board:
        print(row)
        
     def is_valid(row, col, num):      
  
        rowIndex =  3*(row/3) + i/3
        colIndex =  3*(col/3) + i%3
        if board[rowIndex][colIndex] == num:
          return False        
      return True
        
    def is_valid(row, col, num):      
      for i in range(9):
        if board[i][col] == num:
          return False
        
        if board[row][i] == num:
          return False
        
        rowIndex =  3*(row/3) + i/3
        colIndex =  3*(col/3) + i%3
        if board[rowIndex][colIndex] == num:
          return False
        
      return True
    
    def helper():
      for r in range(rows):
        for c in range(cols):
          if board[r][c] == ".":
            for num in range(1, 10):
              if is_valid(r, c, str(num)):
                board[r][c] = str(num)
                if helper():                  
                  return True
                board[r][c] = "."
            return False
      return True
    if helper():
      print_board()
      return True
    return False