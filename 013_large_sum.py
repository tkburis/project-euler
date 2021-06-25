from perf_timer import Timer


# https://projecteuler.net/problem=13
class Solution:
    def __init__(self, lines):
        self.lines = lines

    def naive(self) -> int:
        lines = self.lines

        s = 0
        for line in lines:
            s += int(line)

        return int(str(s)[:10])

    def truncated_summands(self) -> int:
        lines = self.lines

        s = 0
        for line in lines:
            s += int(line[:11])

        return int(str(s)[:10])


if __name__ == "__main__":
    with open("data/013_large_sum.txt", "r") as f:
        all_lines = f.readlines()
    sol = Solution(all_lines)
    with Timer():
        print(sol.naive())
    with Timer():
        print(sol.truncated_summands())
