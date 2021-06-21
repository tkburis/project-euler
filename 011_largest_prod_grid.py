from perf_timer import Timer
from math import prod


# https://projecteuler.net/problem=11
class Solution:
    def __init__(self, lines):
        self.lines = lines

    def naive(self) -> int:
        lines = self.lines
        curr_max = 0

        # check rows
        for row in range(len(lines)):
            for char in range(len(lines[0]) - 3):
                curr_max = max(curr_max, prod([lines[row][char+k] for k in range(4)]))

        # check cols
        for col in range(len(lines[0]) - 3):
            for char in range(len(lines)):
                curr_max = max(curr_max, prod([lines[col+k][char] for k in range(4)]))

        # check top-left -> bottom-right diag
        for row in range(len(lines) - 3):
            for col in range(len(lines[0]) - 3):
                curr_max = max(curr_max, prod([lines[row+k][col+k] for k in range(4)]))

        # check top-right -> bottom-left diag
        for row in range(len(lines) - 1, 2, -1):
            for col in range(len(lines[0]) - 3):
                curr_max = max(curr_max, prod([lines[row-k][col+k] for k in range(4)]))

        return curr_max


if __name__ == "__main__":
    with open("data/011_largest_prod_grid.txt", "r") as f:
        all_lines = []
        for line in f.readlines():
            curr_line = line.strip('\n')
            curr_line = curr_line.split()
            curr_line = [int(x) for x in curr_line]
            all_lines.append(curr_line)
    sol = Solution(all_lines)
    with Timer():
        print(sol.naive())
