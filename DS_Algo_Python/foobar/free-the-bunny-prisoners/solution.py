from itertools import combinations

def solution(num_buns, num_required):
    solution = [[] for bunny in range(num_buns)]

    copies = num_buns - num_required + 1
    l = list(combinations(range(num_buns),copies))
    print(l)
    for key, bunnies in enumerate(l):
        for bun in bunnies:
            solution[bun].append(key)
    return solution


print(solution(5,3))