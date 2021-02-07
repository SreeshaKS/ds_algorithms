import math


def gcd(a, b):
    a, b = abs(a), abs(b)
    while a != 0 and b != 0:
        a %= b
        if a == 0:
            break
        b %= a
        if b == 0:
            break
    return a + b


def fix(a, b):
    if a == 0 and b == 0:
        return 0, 0
    d = gcd(a, b)
    a //= d
    b //= d
    return a, b


def norm(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def get_vectors(sp, tp, dimensions, distance, last, vec, vis):
    if tp in vis:
        return
    vis.add(tp)
    if norm(sp, tp) <= distance:
        v = fix(tp[0] - sp[0], tp[1] - sp[1])
        vec[v] = norm(sp, tp)
        for i in range(4):
            if i != last:
                if i == 0:
                    ntp = (-tp[0], tp[1])
                elif i == 1:
                    ntp = (2 * dimensions[0] - tp[0], tp[1])
                elif i == 2:
                    ntp = (tp[0], -tp[1])
                elif i == 3:
                    ntp = (tp[0], 2 * dimensions[1] - tp[1])
                get_vectors(sp, ntp, dimensions, distance, i, vec, vis)


def solution(dimensions, your_position, guard_position, distance):
    vec1, vis1 = dict(), set()
    get_vectors(tuple(your_position), tuple(guard_position), dimensions,
                distance, -1, vec1, vis1)

    
    vec2, vis2 = dict(), set()
    get_vectors(tuple(your_position), tuple(your_position), dimensions,
                distance, -1, vec2, vis2)
    print(vis2)
    ans = 0
    for k in vec1:
        if k not in vec2:
            ans += 1
        else:
            if vec1[k] > vec2[k]:
                ans += 1
    return ans

print(solution([3,2], [1,1], [2,1], 4))
# print(solution([300,275], [150,150], [185,100], 500))