# Complete the camelcase function in the editor below. It must return the integer number of words in the input string.

def camelcase(s):
    return 1 + len(list(filter(lambda x: x.isupper(), list(s))))
