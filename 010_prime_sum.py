from perf_timer import Timer


# https://projecteuler.net/problem=10
class Solution:
    def __init__(self, n):
        self.n = n

    def naive(self) -> int:
        n = self.n
        s = 0

        for i in range(1, n + 1):
            s += i if self.is_prime(i) else 0

        return s

    def sieve(self) -> int:
        n = self.n
        primes = [True for _ in range(n)]  # initially assume 'all numbers are prime'
        primes[0] = False
        primes[1] = False

        curr_num = 2
        while curr_num ** 2 <= n:
            if primes[curr_num]:
                for mult in range(curr_num * 2, n, curr_num):  # go through future multiples of curr_num, mark as False
                    primes[mult] = False
            curr_num += 1
        s = 0
        for num, is_prime in enumerate(primes[1:]):
            if is_prime:
                s += num + 1

        return s

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
    sol = Solution(2000000)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.sieve())
