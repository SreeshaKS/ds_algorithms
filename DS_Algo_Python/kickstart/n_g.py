import sys

def solve(a, b):
  m = (a + b) // 2
  print(m)
  sys.stdout.flush()
  s = input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  else:
    b = m - 1
  solve(a, b)

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  _ = int(input())
  solve(a + 1, b)



# import sys

# if __name__ == '__main__':
#     # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
#     # This is all you need for most Kickstart problems.
#     t = int(input())  # read a line with a single integer
   
#     for _ in range(t):

#         inp = input()
#         if inp == "WRONG_ANSWER":
#             print("failed",file=sys.stderr)
#             break

#         l = inp.split(" ")

#         a = int(l[0])
#         b = int(l[1])
        
#         head = a + 1
#         tail = b
#         mG = int(input())
#         printedValue = 2
#         print(str(printedValue))
#         for _ in range(mG-1):
#             mid = ( a + b ) / 2
#             print(str(mid))
#             res = input()
#             if res == "TOO_SMALL":
#                 tail = mid - 1
#             if res == "TOO_BIG":
#                 head = mid + 1
#             if res == "CORRECT":
#                 break
#             if res == "WRONG_ANSWER":
#                 break
#     sys.exit(0)