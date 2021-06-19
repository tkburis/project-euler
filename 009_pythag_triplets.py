from perf_timer import Timer


# https://projecteuler.net/problem=9
class Solution:
    def __init__(self, n):
        self.n = n

    def naive(self) -> int:
        n = self.n

        for a in range(1, n):
            for b in range(a + 1, n):
                c = n - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    print(a, b, c)
                    return a * b * c
        return -1


if __name__ == "__main__":
    sol = Solution(1000)
    with Timer():
        print(sol.naive())
