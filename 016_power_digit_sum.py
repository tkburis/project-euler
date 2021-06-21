from perf_timer import Timer
from math import log10


# https://projecteuler.net/problem=16
class Solution:
    def __init__(self, exp):
        self.exp = exp

    def naive(self) -> int:
        exp = self.exp
        powered = 2**exp
        powered = list(str(powered))
        powered = sum([int(x) for x in powered])

        return powered

    def manual(self) -> int:  # TODO: find out why this is so inefficient...
        exp = self.exp

        # num_length = int(1+exp*log10(2))
        curr_num = [1]
        curr_num_digits = 1

        carry = 0
        for i in range(exp):
            for digit in range(len(curr_num)):
                curr_num[digit] *= 2
                if carry == 1:
                    curr_num[digit] += carry
                    carry = 0
                if curr_num[digit] > 9:
                    carry = curr_num[digit] // 10
                    curr_num[digit] -= carry * 10
                    curr_num_digits += 1
                if digit == len(curr_num) - 1 and curr_num[digit] >= 5:
                    curr_num.insert(len(curr_num), 0)
        return sum(curr_num)


if __name__ == "__main__":
    sol = Solution(5)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.manual())
