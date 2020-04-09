# Write an algorithm to determine if a number is "happy".
import math

arr = []
class Solution:
    def isHappy(self, n: int) -> bool:
        global arr
        def is_power_of_10(number):
            power = math.floor(math.log(number, 10))
            return 10 ** power == number
        if is_power_of_10(n):
            return True
        else:
            new_number = sum(list(map(lambda x: (int(x)) ** 2, list(str(n)))))
            arr += [n]
            print(arr)
            if True in list(map(lambda x: is_power_of_10(new_number / x), arr[:-1])):
                arr = []
                return False
            else:
                return Solution().isHappy(new_number)
