# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    n = len(arr)
    index = list(range(len(arr)))
    left_digonals = list(map(lambda x, y: x[y], arr, index))
    right_digonals = list(map(lambda x, y: x[n - (y + 1)], arr, index))
    return abs(sum(left_digonals) - sum(right_digonals))
