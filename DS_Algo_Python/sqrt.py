
import math

i = 2
N = 1500450271
iPrime = False

while i < math.sqrt(N):
  if N % i == 0: 
    isPrime = False
  i+=1

# Time taken by B's program = 1ms * number of divisions 
# = 1ms * square root of 1500450271
# = approximately 40000ms = 40 seconds.