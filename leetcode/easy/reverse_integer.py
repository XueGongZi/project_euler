# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        reverse_int = 0
        if x >= 0:
            reverse_int = int(str(x)[::-1])
        else:
            reverse_int = 0 - int(str(x)[1:][::-1])
        if x <= 2 ** 31 - 1 and x >= -(2 ** 31) and reverse_int <= 2 ** 31 - 1 and reverse_int >= -(2 ** 31):
            return reverse_int
        else:
            return 0
