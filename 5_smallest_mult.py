from perf_timer import Timer
from math import prod


# https://projecteuler.net/problem=5
class Solution:
    def __init__(self, to_range):
        self.to_range = to_range

    def iterative(self) -> int:
        to_range = self.to_range
        mult_string = [1]

        for num in range(2, to_range+1):  # e.g. 2 ~ 20
            to_mult = num
            for alr in mult_string:  # go through each one already multiplied: if 'part' of the current number has
                # already been multiplied, then divide by that number
                if to_mult % alr == 0:
                    to_mult //= alr
            mult_string.append(to_mult)

        return prod(mult_string)


if __name__ == "__main__":
    sol = Solution(20)
    with Timer():
        print(sol.iterative())
