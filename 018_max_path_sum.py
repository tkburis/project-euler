from perf_timer import Timer


# https://projecteuler.net/problem=18
class Solution:
    def __init__(self, triangle):
        self.triangle = triangle

    # NOTE: problem 67 is the same, but cannot be brute forced; therefore, i only present the brute force solution for
    # this problem
    def naive(self):
        sums = []

        def get_sum(curr_triangle, curr_sum=0, src_index=0):
            if len(curr_triangle) == 1:
                sums.append(curr_sum+curr_triangle[0][src_index])
                return
            get_sum(curr_triangle[1:], curr_sum + curr_triangle[0][src_index], src_index)
            get_sum(curr_triangle[1:], curr_sum + curr_triangle[0][src_index], src_index+1)
        get_sum(self.triangle)
        return max(sums)


if __name__ == "__main__":
    with open("data/018_max_path_sum.txt", "r") as f:
        file_triangle = []
        for line in f.readlines():
            line = line.split()
            line = [int(x) for x in line]
            file_triangle.append(line)

    sol = Solution(file_triangle)
    with Timer():
        print(sol.naive())
