def rangeBitwiseAnd( m, n):
        res = m
        i = m+1
        while i <= n:
            res = res & i
            i+=1
        return res
print(rangeBitwiseAnd(5,7))