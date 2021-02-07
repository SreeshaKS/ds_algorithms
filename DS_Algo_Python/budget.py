def find_grants_cap(grantsArray, newBudget):
  
  grantsArray.sort()
  maximum = max(grantsArray)
  difference = sum(grantsArray) - newBudget
  if difference < 0:
    return 0
  
  n = len(grantsArray)
  i = n - 1
  cap = maximum
  
  while i > 0:
    difference = sum(grantsArray[0:i]) + grantsArray[i-1] * (n - i) - newBudget
    #print(grantsArray[0:i],i, difference,cap)
    if difference > 0:
      cap = grantsArray[i-1]
      i -= 1
    else:
      i = i+1
      break
  print(n,i)
  v = (cap * (n - i ) - newBudget) / float(n - i)

print()
