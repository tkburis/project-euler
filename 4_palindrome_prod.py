from perf_timer import Timer


# https://projecteuler.net/problem=4
class Solution:
    def __init__(self, _min, _max):
        self._min = _min
        self._max = _max

    def naive(self) -> int:
        _min = self._min
        _max = self._max
        curr_max = 0
        # start from _max, then go down
        for i in range(_max, _min-1, -1):
            for j in range(i, _min-1, -1):
                curr = i * j
                if self.is_palindrome(curr):
                    curr_max = max(curr, curr_max)
        return curr_max

    @staticmethod
    def is_palindrome(n: int) -> bool:
        n = str(n)
        if n == n[::-1]:
            return True
        return False


if __name__ == "__main__":
    sol = Solution(100, 999)  # 3-digits
    with Timer():
        print(sol.naive())
