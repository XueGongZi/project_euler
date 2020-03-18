# Mathematical Definition

def is_divisible(small_number, big_number):
    if big_number % small_number == 0:
        return True
    else:
        return False

def is_prime(number):
    if number == 2:
        return True
    elif number == 3:
        return True
    else:
        factor = 2
        while factor < number ** 0.5:
            if is_divisible(factor, number):
                return False
                break
            else:
                factor += 1
        return True

def smallest_factor(number):
    factor = 2
    if is_prime(number):
        return number
    else:
        while factor < number ** 0.5:
            if number % factor == 0:
                return factor
            else:
                factor += 1

def is_palindromic(number):
    return str(number) == str(number)[::-1]

def is_n_digits_positive_number(n, number):
    return (10 ** (n - 1)) < number < (10 ** n - 1)
