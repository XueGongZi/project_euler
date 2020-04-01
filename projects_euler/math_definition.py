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
        while factor <= number ** 0.5:
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

def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]

    p = 2
    while(p * p <= n):

        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    c = 0

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            c += 1
    return c
