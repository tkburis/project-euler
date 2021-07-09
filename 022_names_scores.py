from perf_timer import Timer
from string import ascii_uppercase


# https://projecteuler.net/problem=22
class Solution:
    def __init__(self, names):
        self.names = names

    def solve(self):
        names = self.names
        names = sorted(names)

        total = 0
        for index, name in enumerate(names):
            name_sum = sum([ascii_uppercase.index(ch) + 1 for ch in name])
            total += name_sum * (index + 1)
        return total


if __name__ == "__main__":
    with open("data/022_names_scores.txt", "r") as f:
        all_names = f.readline()
    all_names = all_names.replace('"', '')
    all_names = all_names.split(',')
    sol = Solution(all_names)
    with Timer():
        print(sol.solve())
