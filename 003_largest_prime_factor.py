from perf_timer import Timer


# https://projecteuler.net/problem=3
class Solution:
    def __init__(self, n):
        self.n = n

    def naive(self, prime_check) -> int:
        n = self.n
        max_prime = 0

        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                if prime_check(factor):
                    max_prime = factor

        if max_prime == 0:  # n must be a prime itself
            return n
        return max_prime

    def optimised(self) -> int:
        n = self.n
        max_prime = 0
        while n % 2 == 0:  # divide by 2 until you cannot anymore
            max_prime = 2
            n /= 2

        for factor in range(3, int(n ** 0.5) + 1, 2):  # n must be odd, so factors now must only be odd, so skip evens
            while n % factor == 0:
                max_prime = factor
                n /= factor

        if max_prime == 0:  # n must itself be prime
            return n
        return max_prime

    @staticmethod
    def is_prime_naive(n: int) -> bool:
        if n < 2:
            return False
        for factor in range(2, int(n ** 0.5) + 1):  # unique factors are below sqrt(n)
            if n % factor == 0:
                return False
        return True

    @staticmethod
    def is_prime_optimised(n: int) -> bool:  # based off https://en.wikipedia.org/wiki/Primality_test
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
    sol = Solution(n=600851475143)
    with Timer():
        print(sol.naive(sol.is_prime_naive))
    with Timer():
        print(sol.naive(sol.is_prime_optimised))
    with Timer():
        print(sol.optimised())
    with Timer():
        print(sol.optimised())
    # is_prime_naive and is_prime_optimised are very similar in runtime. My guess is the number of % operations being
    # used in the optimised version, making calculations more expensive (?).
