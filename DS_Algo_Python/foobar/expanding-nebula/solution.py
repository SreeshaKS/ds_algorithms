from collections import defaultdict

def generate(c1,c2,bitlen):
    y = 2**bitlen

    a = c1 & ~y
    b = c2 & ~y
    c = c1 / 2
    d = c2 / 2

    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def buildMap(n, generations):
    mapping = defaultdict(set)
    generations = set(generations)
    
    for i in range(2**(n+1)):
        for j in range(2**(n+1)):

            generation = generate(i,j,n)
            
            if generation in generations:
                mapping[(generation, i)].add(j)
    
    return mapping

def solution(g):
    transpose = list(zip(*g)) # transpose
    ncols = len(transpose[0])

    # turn map into numbers
    generations = []
    for row in transpose:
        vals = []
        for i,col in enumerate(row):
            if col:
                vals.append(2**i)
            else:
                vals.append(0)
        generations.append(sum(vals))

    mapping = buildMap(ncols, generations)

    preimage = defaultdict(int)
    n = 2 ** (ncols+1)

    for i in range(n):
        preimage[i] = 1
    
    for row in generations:

        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[ (row, c1) ]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    
    
    return sum(preimage.values())

print(solution([[True, False, True], [False, True, False], [True, False, True]]))