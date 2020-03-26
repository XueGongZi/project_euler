# John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

def circularArrayRotation(a, k, queries):
    n = len(a)
    remainder = k % n
    index = list(range(n))
    new_a = list(map(lambda x: a[((x - remainder) % n)], index))
    return list(map(lambda x: new_a[x], queries))
arr = [2, 3, 1, 9, 8, 8]
rou = 2
query = [1, 2]
print(circularArrayRotation(arr, rou, query))
