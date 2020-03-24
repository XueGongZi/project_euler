# Problem 6, Sum square difference
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
lower_limit = 1
upper_limit = 100

def sum_of_squares(ll, ul):
    list_of_squares = list(map(lambda x: x ** 2, range(ll, ul + 1)))
    return sum(list_of_squares)

def squares_of_sums(ll, ul):
    return sum(range(ll, ul + 1)) ** 2

def ans():
    ans = squares_of_sums(lower_limit, upper_limit) - sum_of_squares(lower_limit, upper_limit)
    return ans
