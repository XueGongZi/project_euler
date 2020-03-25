# Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.
#

size = 3

def compareTriplets(a, b):
    index = list(range(size))
    score = [0, 0]
    for i in index:
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
        else:
            score
    return score
