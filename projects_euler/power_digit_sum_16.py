class Solution:
    def power_digit_sum(self, base, power):
        power_result = base ** power
        sum_of_digits = sum(list(map(lambda x: int(x), list(str(power_result)))))
        print(sum_of_digits)
