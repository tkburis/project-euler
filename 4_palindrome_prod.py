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
        c = 0

        for i in range(_min, _max+1):
            for j in range(_min, _max+1):
                curr = i * j
                if self.is_palindrome(curr):
                    curr_max = max(curr_max, curr)
                c += 1
        print(f"Products checked: {c}")
        return curr_max

    def count_backwards(self) -> int:
        _min = self._min
        _max = self._max
        curr_max = 0
        c = 0

        for i in range(_max, _min-1, -1):
            for j in range(_max, i-1, -1):
                curr = i * j
                if curr <= curr_max:  # because we are counting down, from here i*j < curr_max, so just skip to next i
                    break
                if self.is_palindrome(curr):  # this condition is reached only if curr > curr_max
                    curr_max = curr
                c += 1

        print(f"Products checked: {c}")
        return curr_max

    def mults_eleven(self) -> int:
        _min = self._min
        _max = self._max
        curr_max = 0
        c = 0

        for i in range(_max, _min-1, -1):
            if i % 11 == 0:
                for j in range(_max, i-1, -1):
                    curr = i * j
                    if curr <= curr_max:
                        break
                    if self.is_palindrome(curr):
                        curr_max = curr
            else:  # at least one of i/j must be divisible by 11. so if i not divisible, j must be mult of 11
                max_j = _max - (_max % 11)
                for j in range(max_j, i-1, -11):
                    curr = i * j
                    if curr <= curr_max:
                        break
                    if self.is_palindrome(curr):
                        curr_max = curr

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
    with Timer():
        print(sol.count_backwards())
    with Timer():
        print(sol.mults_eleven())
