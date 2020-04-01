from itertools import permutations

dice_number = list(range(1, 7))
dice_perm = [list(i) for i in list(permutations(dice_number, 2))] + list(map(lambda x: [x, x], dice_number))

def more_dice():
    no_of_desired_outcomes = len(list(filter(lambda x: x[0] != x[1] and x[0] + x[1] == 6, dice_perm)))
    no_of_total_outcomes = len(dice_perm)
    return no_of_desired_outcomes / no_of_total_outcomes

print(more_dice())
