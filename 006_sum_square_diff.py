from perf_timer import Timer
from itertools import combinations


# https://projecteuler.net/problem=6
class Solution:
    def __init__(self, to_range):
        self.to_range = to_range

    def naive(self) -> int:
        to_range = self.to_range

        sum_of_squares = sum([x**2 for x in range(1, to_range+1)])
        square_of_sums = sum(range(1, to_range+1)) ** 2

        return abs(sum_of_squares - square_of_sums)

    def using_combinations(self) -> int:  # BAD! O(N^2)
        to_range = self.to_range
        _sum = 0

        nums = list(range(1, to_range+1))
        combs = combinations(nums, 2)
        for comb in combs:
            _sum += 2 * comb[0] * comb[1]  # e.g. (a+b)^2 - (a^2-b^2) = 2ab; this generalises for more variables

        return _sum

    def arithmetic(self) -> int:
        to_range = self.to_range

        sum_of_squares = (to_range * ((2 * to_range) + 1) * (to_range + 1)) // 6
        square_of_sums = (((to_range + 1) * to_range) // 2) ** 2
        return abs(sum_of_squares - square_of_sums)


if __name__ == "__main__":
    sol = Solution(1000)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.using_combinations())
    with Timer():
        print(sol.arithmetic())
