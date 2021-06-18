from perf_timer import Timer


# https://projecteuler.net/problem=2
class Solution:
    def __init__(self, to_range):
        self.to_range = to_range

    def naive(self) -> int:  # O(N), but this works fine even for large N as Fibonacci numbers grow exponentially fast
        to_range = self.to_range
        _sum = 0
        n1 = 1
        n2 = 2
        while n2 < to_range:
            _sum += n2 if n2 % 2 == 0 else 0
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return _sum

    def arithmetic(self) -> int:  # O(1), but naive solution works just as well for almost all cases
        # in fact, naive is better for large N as n_fib() overflows for large N
        to_range = self.to_range
        _sum = 0
        n = 3  # n_fib() starts at 0, 1, 1, 2, etc.; first even is 2, so n=3
        curr_fib = self.n_fib(n)
        while curr_fib < to_range:
            _sum += curr_fib
            n += 3  # takes advantage of the fact that fibonacci numbers are even every 3 terms
            curr_fib = self.n_fib(n)
        return _sum

    @staticmethod
    def n_fib(n) -> int:
        phi = (1 + 5 ** 0.5) / 2
        inv_phi = (1 - 5 ** 0.5) / 2
        fib = int((phi ** n - inv_phi ** n) // (5 ** 0.5))  # Euler-Binet formula
        return fib


if __name__ == "__main__":
    sol = Solution(to_range=4000000)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.arithmetic())
