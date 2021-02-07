
def sieve(n):
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    
    primes = []
    for i in range(len(prime)):
        if prime[i] is True:
            primes.append(str(i))
    return primes

primes = []
p = ""
def solution(i):

    global primes
    global p

    if len(primes) == 0:
        primes = sieve(21000)
        p = "".join(primes)
    if i < 0:
        return ""
    return p[i:i+5]

solution(0)
solution(3)