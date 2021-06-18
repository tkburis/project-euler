from perf_timer import Timer
from math import prod


# https://projecteuler.net/problem=8
class Solution:
    def __init__(self, num, adj):
        self.num = num
        self.adj = adj

    def naive(self) -> int:  # O(len(num) * adj)
        num = self.num
        adj = self.adj
        num = str(num)

        curr_max = 0

        for i in range(len(num) - adj + 1):
            curr_prod = prod([int(num[i + k]) for k in range(adj)])
            curr_max = max(curr_max, curr_prod)

        return curr_max

    def slightly_smarter(self):  # O(len(num))
        num = self.num
        adj = self.adj
        num = str(num)

        curr_max = 0
        curr_prod_list = [int(num[k]) for k in range(adj)]
        curr_prod = prod([int(num[k]) for k in range(adj)])

        for i in range(adj, len(num) - adj + 1):  # goes through each character linearly; divides by the one that is
            # leaving the chain and multiply by the one getting added
            if int(num[i-adj]) == 0:
                curr_prod_list = [int(num[i - adj + k + 1]) for k in range(adj)]
                curr_prod = prod([int(num[i - adj + k + 1]) for k in range(adj)])
            else:
                curr_prod *= int(num[i])
                curr_prod //= int(num[i-adj])
                curr_prod_list.pop(0)
                curr_prod_list.append(int(num[i]))
            curr_max = max(curr_max, curr_prod)

        return curr_max


if __name__ == "__main__":
    with open("data/8_adjacent_max_prod.txt", "r") as f:
        data = int(f.read())

    sol = Solution(data, 13)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.slightly_smarter())
