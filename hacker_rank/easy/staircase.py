# Complete the staircase function in the editor below. It should print a staircase as described above.

def staircase(n):
    for i in range(n):
        staircase = " " * (n - i - 1) + "#" * (i + 1)
        print(staircase)
