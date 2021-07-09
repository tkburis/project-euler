from perf_timer import Timer
from math import factorial


# https://projecteuler.net/problem=20
class Solution:
    def __init__(self, n):
        self.n = n

    def naive(self):
        n = self.n
        fact = factorial(n)
        return sum(list(map(int, str(fact))))

    def ignore_zeroes(self):  # uses slightly less memory in theory
        n = self.n

        num = 1
        for i in range(2, n+1):
            while i % 10 == 0:
                i //= 10
            num *= i
        return sum(list(map(int, str(num))))


if __name__ == "__main__":
    sol = Solution(100)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.ignore_zeroes())
