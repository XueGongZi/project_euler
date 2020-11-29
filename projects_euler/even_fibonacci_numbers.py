class Solution:
    def fibonacci_numbers(self, upper):
        fib = [1, 1]
        while fib[-1] <= upper:
            new_element = fib[-1] + fib[-2]
            fib.append(new_element)
        return fib[:-1]

    def sum_even_fibonacci(self, upper):
        return sum(self.fibonacci_numbers(upper)) // 2

upper = 4000000
print(Solution().sum_even_fibonacci(upper))
