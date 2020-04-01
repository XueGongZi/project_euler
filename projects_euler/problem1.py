# Problem 1, Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 and 5, we get 3, 5, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

lower_limit = 1
first_factor = 3
second_factor = 5
upp_limit = 1000

def sum_of_multiples_within(array_of_factors, upper_limit):
    array = []
    for a in array_of_factors:
        array += find_multiples(a, upper_limit)
    unique_array = find_unique_elements(array)
    return find_sum_array(unique_array)

def find_multiples(factor, upper_limit):
    array = []
    for a in range(lower_limit, upper_limit + 1):
        if a % factor == 0:
            array += [a]
    return array

def find_sum_array(array):
    total = 0
    for a in array:
        total += a
    return total

def find_unique_elements(array):
    new_array = []
    for a in array:
        if a in new_array:
            new_array
        else:
            new_array += [a]
    return new_array

def sum_of_multiples_within_v2_2_elements(array_of_factors, upper_limit):
    first_element = array_of_factors[0]
    second_element = array_of_factors[1]
    return sum_of_multiples_of(first_element, upper_limit) + \
           sum_of_multiples_of(second_element, upper_limit) - \
           sum_of_multiples_of(first_element * second_element, upper_limit)

def sum_of_multiples_of(element, upper_limit):
    last_element = upper_limit - upper_limit % element
    number_of_elements = (last_element - element) // element + 1
    total = (element + last_element) * number_of_elements // 2
    return total

def ans():
    return sum_of_multiples_within_v2_2_elements([first_factor, second_factor], upp_limit)  
