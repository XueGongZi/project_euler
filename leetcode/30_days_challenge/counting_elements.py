import collections as cl
class Solution:
    def countElements(self, arr: [int]) -> int:
        new_arr = list(set(arr))
        new_arr.sort()
        filter_arr = list(filter(lambda x: (x + 1) in new_arr, new_arr))
        ct = cl.Counter(arr)
        result = 0
        for i in filter_arr:
            result += ct[i]
        return result
