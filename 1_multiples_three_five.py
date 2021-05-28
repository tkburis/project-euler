from perf_timer import Timer


# https://projecteuler.net/problem=1
class Solution:
    def __init__(self, to_range):
        self.to_range = to_range

    def naive(self) -> int:  # O(N) complexity
        to_range = self.to_range
        _sum = 0
        for n in range(to_range):
            _sum += n if n % 3 == 0 or n % 5 == 0 else 0
        return _sum

    def for_increments(self) -> int:  # O(N) complexity, still linear but slightly more efficient for extremely large N
        to_range = self.to_range
        _sum = 0
        for n in range(0, to_range, 3):
            _sum += n
        for n in range(0, to_range, 5):
            _sum += n
        for n in range(0, to_range, 15):  # don't double-count multiples of 15
            _sum -= n
        return _sum

    def arithmetic(self) -> int:  # O(1) complexity
        to_range = self.to_range
        _sum = 0
        num_mult_threes = (to_range - 1) // 3
        num_mult_fives = (to_range - 1) // 5
        num_mult_fifteens = (to_range - 1) // 15
        _sum += ((num_mult_threes * (num_mult_threes + 1)) // 2) * 3
        _sum += ((num_mult_fives * (num_mult_fives + 1)) // 2) * 5
        _sum -= ((num_mult_fifteens * (num_mult_fifteens + 1)) // 2) * 15  # don't double-count multiples of 15
        return _sum


if __name__ == "__main__":
    sol = Solution(to_range=1000)
    with Timer():
        print(sol.naive())  # 0.74s for to_range=10^7
    with Timer():
        print(sol.for_increments())  # 0.19s for to_range=10^7
    with Timer():
        print(sol.arithmetic())  # 0.0s for to_range=10^7
