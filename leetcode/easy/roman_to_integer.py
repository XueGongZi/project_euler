# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        letters = "MDCLXVI"
        romans = list(letters)
        integers = [1000, 500, 100, 50, 10, 5, 1]
        before_convert = list(s)
        convert_to_int = list(map(lambda x: integers[romans.index(x)], before_convert))
        n = len(s)
        converted = 0
        for i in list(range(n)):
            if i == n - 1:
                converted += convert_to_int[i]
            else:
                if convert_to_int[i] >= convert_to_int[i + 1]:
                    converted += convert_to_int[i]
                else:
                    converted -= convert_to_int[i]
        return converted

print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("MCMXCIV"))
