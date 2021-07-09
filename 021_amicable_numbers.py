from perf_timer import Timer
from math import sqrt


# https://projecteuler.net/problem=21
class Solution:
    def __init__(self, to_range):
        self.to_range = to_range

    def naive(self, div_sum_method):
        to_range = self.to_range

        _sum = 0
        for n in range(1, to_range):
            if self.check_amicable(n, div_sum_method):
                _sum += n
        return _sum

    @staticmethod
    def check_amicable(n, div_sum_method):  # amicable if d(a) = b & d(b) = a; so amicable if d(d(a)) = a for a != d(a)
        d = div_sum_method(n)
        if n == div_sum_method(d) and n != d:
            return True
        return False

    @staticmethod
    def sum_of_divisors_naive(n):
        _sum = 0
        for i in range(1, n):
            if n % i == 0:
                _sum += i
        return _sum

    @staticmethod
    def sum_of_divisors_improved(n):
        _sum = -n
        step = 2 if n % 2 == 1 else 1

        for i in range(1, int(sqrt(n))+1, step):
            if n % i == 0:
                _sum += i + (n // i)
                # print(i, n // i)
        if int(sqrt(n)) ** 2 == n:
            _sum -= int(sqrt(n))
        return _sum


if __name__ == "__main__":
    sol = Solution(10000)
    with Timer():
        print(sol.naive(sol.sum_of_divisors_naive))
    with Timer():
        print(sol.naive(sol.sum_of_divisors_improved))
    # print(sol.sum_of_divisors_improved(220))
