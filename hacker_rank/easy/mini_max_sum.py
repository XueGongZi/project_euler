# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. 

def miniMaxSum(arr):
    index = list(range(len(arr)))
    def findCombination(arr, combination):
        return list(map(lambda x: arr[x], combination))

    comb = list(map(lambda x: list(filter(lambda y: y != x, index)), index))
    result = list(map(lambda x: sum(findCombination(arr, x)), comb))
    print("{} {}".format(min(result), max(result)))
