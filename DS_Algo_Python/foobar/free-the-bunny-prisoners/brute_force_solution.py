import itertools

def keyRepeats(comboList,keyList,required):
    copyNum = [ 0 ] * len(keyList)
    for c in comboList:
        for key in c:
            copyNum[key] += 1
            if copyNum[key] > required:
                return False
    return True

def checkSets(comboList, keyList, required, bunnies):

    resultCombo = itertools.combinations(comboList, bunnies)

    for window in resultCombo:
        b = keyRepeats(window, keyList, required)

        if not b:
            continue
        cs = list(itertools.combinations(list(window), required))
        
        possible = True
        for x in list(cs):
            
            s = set()
            lx = list(x)
            
            for y in lx:
                s = set(list(s) + list(y))

            if list(s) != keyList:
                possible = False
                break
        if possible:
            return window
    
    return []


def isPossible(comboList, keyList, required, bunnies):
    # required number of copies of each key
    # required - 1 of lists should not union upto keyList
    # required of lists should union upto keyList    

    r = checkSets(comboList, keyList, required, bunnies) 
    # l = checkSets(comboList, keyList, required - 1, bunnies)
    
    # if len(l) is not 0:
    #     return []
    return r
        
def solution(num_buns, num_required):
    m = num_buns
    n = num_required

    if n == 0:
        return None

    if n == 1:
        return [ [0] for x in range(m) ]
    
    if m == n:
        return [ [x] for x in range(m) ]
     

    numKeys = len(list(itertools.combinations([0]*m,n)))

    kl = [ x for x in range(numKeys) ]

    
    l = list(itertools.combinations(kl, numKeys * n / m ))
    response = []
    result = isPossible(l, kl, num_required, num_buns)

    for r in result:
        response.append(list(r))
    
    return response

print(solution(4, 3))