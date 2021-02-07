class Solution:
    def climbStairs(self, n: int) -> int:
        map = {0:0, 1:1, 2:2 }
        for i in range(n+1):
            if i > 2:
                map[i] = 0

        for i in range(n+1):
            if i > 2:
                map[i] = map[i-1] + map[i-2]
        return map[n]