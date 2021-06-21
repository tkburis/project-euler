from perf_timer import Timer
from math import sqrt


# https://projecteuler.net/problem=29
class Solution:
    def __init__(self, max_a, max_b):
        self.max_a = max_a
        self.max_b = max_b

    def naive(self) -> int:
        max_a = self.max_a
        max_b = self.max_b
        seen = set()
        for a in range(2, max_a+1):
            for b in range(2, max_b+1):
                seen.add(a**b)
        return len(seen)


if __name__ == "__main__":
    sol = Solution(100, 100)
    with Timer():
        print(sol.naive())
