class Solution:
    def lattice_paths(self, length, width):
        if length < width:
            short = length
        else:
            short = width
        total = length + width
        times = 1
        divide = 1
        for i in range(1, short + 1):
            times *= total - short + i
            divide *= i
        return times // divide
