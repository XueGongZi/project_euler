class Solution:
    new_arr = []
    def flatten_list(self, array):
        for i in array:
            if type(i) == list:
                self.flatten_list(i)
            else:
                self.new_arr.append(i)
        return self.new_arr

    def set_first_lower_limit(self, arr):
        # set lower limit
        lower_limit = 0
        for i in arr:
            lower_limit += i[-1]
        return lower_limit

    def get_the_correct_number(self, j, x, arr, i):
        if j == 0:
            return x + arr[i - 1][j]
        elif j == len(arr[i]) - 1:
            return x + arr[i - 1][j - 1]
        else:
            print([arr[i - 1][j - 1], arr[i - 1][j]])
            return x + max(arr[i - 1][j - 1], arr[i - 1][j])

    def get_new_arr(self, arr):
        for i in range(len(arr)):
            if i == 1:
                arr[i] = list(map(lambda x: x + arr[i - 1][i - 1], arr[i]))
            elif i == 0:
                arr[0] = arr[0]
            else:
                arr[i] = [self.get_the_correct_number(j, x, arr, i) for j, x in enumerate(arr[i])]
        print(arr)
        return max(arr[len(arr) - 1])

arr = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

print(Solution().set_first_lower_limit(arr))
print(Solution().get_new_arr(arr))
