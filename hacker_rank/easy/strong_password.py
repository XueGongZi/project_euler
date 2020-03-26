# She typed a random string of length in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    def satisfyCriterio(sentence, case):
        return len(list(filter(lambda x: x in list(case), sentence))) > 0

    criterio = [numbers, lower_case, upper_case, special_characters]
    satisfied = list(map(lambda x: satisfyCriterio(password, x), criterio))
    score = len(list(filter(lambda x: x == True, satisfied)))
    if n >= 6 or (n + 4 - score) >= 6:
        return 4 - score
    else:
        return 6 - n
