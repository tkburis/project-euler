from perf_timer import Timer
from math import comb


# https://projecteuler.net/problem=15
class Solution:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def recursive(self) -> int:
        x = self.x
        y = self.y
        dp = {(i, j): -1 for i in range(x + 1) for j in range(y + 1)}

        def f(n, m) -> int:
            if dp[n, m] != -1:
                return dp[n, m]

            if n == 1 or m == 1:
                dp[n, m] = n + m
                return dp[n, m]
            dp[n, m] = f(n - 1, m) + f(n, m - 1)
            return dp[n, m]

        ans = f(x, y)
        return ans

    def iterative(self) -> int:
        x = self.x
        y = self.y

        grid = {(i, j): 0 for i in range(x + 1) for j in range(y + 1)}
        for i in range(x+1):
            grid[i, 0] = 1
        for j in range(y+1):
            grid[0, j] = 1

        for i in range(1, x+1):
            for j in range(1, y+1):
                grid[i, j] = grid[i-1, j] + grid[i, j-1]

        return grid[x, y]

    def combinatorics(self) -> int:  # from a total of x+y operations, there must be x 'RIGHT' operations, rest are y
        # 'DOWN' operations; so find number of ways to put 'RIGHT' operations in x+y string
        x = self.x
        y = self.y
        return comb(x + y, x)


if __name__ == "__main__":
    sol = Solution(20, 20)
    with Timer():
        print(sol.recursive())
    with Timer():
        print(sol.iterative())
    with Timer():
        print(sol.combinatorics())
