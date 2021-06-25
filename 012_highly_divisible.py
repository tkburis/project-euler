from perf_timer import Timer
from math import sqrt


# https://projecteuler.net/problem=12
class Solution:
    def __init__(self, min_factors):
        self.min_factors = min_factors

    def naive(self) -> int:
        min_factors = self.min_factors

        for triangular in self.get_triangular():
            if self.num_factors(triangular) > min_factors:
                return triangular

    @staticmethod
    def get_triangular():
        n = 1
        to_add = 2
        while True:
            yield n
            n += to_add
            to_add += 1

    @staticmethod
    def num_factors(n):
        facs = 0
        for i in range(1, int(sqrt(n)+1)):
            if n % i == 0:
                facs += 1
        facs *= 2
        return facs


if __name__ == "__main__":
    sol = Solution(500)
    with Timer():
        print(sol.naive())
