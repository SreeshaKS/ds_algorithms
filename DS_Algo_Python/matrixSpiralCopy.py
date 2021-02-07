def spiralVisit(mat,inverted,row,col):
  if row <= 0 and col <= 0 :
    return []
  row1 = mat[0][0:col-1]
  col1 = inverted[0][0:row-1]
  row2 = mat[col-1][row:0]
  col3 = inverted[0][0:col-1]
  
  return []+row1+col1+row2+col3 + spiralVisit(mat,inverted,row-1,col-1)

def spiral_copy(inputMatrix):
  
  row = len(inputMatrix)
  col = len(inputMatrix[0])
  
  inverted = [[]] * col
  for i,r in enumerate(inputMatrix):
    R = []
    for c in r:
      R.append(c)
    inverted[i] = R
  
  return spiralVisit(inputMatrix,inverted,row,col)

