from perf_timer import Timer


# https://projecteuler.net/problem=14
class Solution:
    def __init__(self, _max):
        self._max = _max
        self.dp = dict()

    def collatz(self):
        _max = self._max

        max_length = 0
        max_starting_num = 0
        for starting_num in range(2, _max):
            curr_chain = self.chain_length(starting_num)
            if curr_chain > max_length:
                max_length = curr_chain
                max_starting_num = starting_num
        return max_starting_num

    def chain_length(self, n):
        if n == 1:
            return 1

        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1

        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.chain_length(n)
        return self.dp[n] + 1


if __name__ == "__main__":
    sol = Solution(1000000)
    with Timer():
        print(sol.collatz())
