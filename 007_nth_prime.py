from perf_timer import Timer


# https://projecteuler.net/problem=7
class Solution:
    def __init__(self, n):
        self.n = n

    def naive(self) -> int:
        n = self.n
        curr_nth = 1
        curr_num = 3
        curr_prime = 3

        while curr_nth < n:
            if self.is_prime(curr_num):
                curr_nth += 1
                curr_prime = curr_num
            curr_num += 2

        return curr_prime

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:  # all primes are of form 6k+/-1 except 2 and 3
            return False
        _max = int(n ** 0.5) + 1
        for factor in range(5, _max, 6):  # all primes are of form 6k+/-1
            if n % factor == 0:
                return False
            if n % (factor + 2) == 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution(10001)
    with Timer():
        print(sol.naive())
