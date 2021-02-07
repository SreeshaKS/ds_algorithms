def solution(s):
    f = 0
    c = 0
    for i in range(len(s)):
        if s[i] == ">":
            f += 1
            continue
        if s[i] == "<":
            c = c + f * 2
            continue
    return c

print(solution("<<"))