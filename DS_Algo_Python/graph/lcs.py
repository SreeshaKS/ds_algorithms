


def lcsRecursive(cA,cB,a,b,table):
    try:
        # check if value exists
        table[cA][cB]
    except:
        res = 0
        if cA == len(a) or cB == len(b):
            res = 0
        elif a[cA] == b[cB]:
            res = 1 + lcsRecursive(cA +1, cB +1, a, b, table)
        else:
            res = max( lcsRecursive(cA+1 ,cB, a, b, table), lcsRecursive(cA, cB+1, a, b, table) )
        table[cA] = { cB: res }
    return table[cA][cB]

print(lcsRecursive(0,0,"bd","abcd",{}))
