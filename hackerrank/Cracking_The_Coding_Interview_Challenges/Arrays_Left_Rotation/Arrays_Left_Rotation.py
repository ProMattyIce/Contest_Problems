"""
url:https://www.hackerrank.com/challenges/ctci-array-left-rotation
The solution was to do it without allocating a new list 
"""

import math

def array_left_rotation(a, n, d):
    """
    :param a: list
    :param n: size of list
    :param d: left rotations 
    :return: an array shift left d times
    """

    # d is not a mutiple of n
    if n % d != 0:
        temp = a[0]
        circle = False
        pos = 0

        while not circle:

            pos = (pos - d) % n
            a[pos], temp = temp, a[pos]

            if pos == 0:
                circle = True
    else:
        middle = int(math.ceil(n / 2))
        for i in range(0, middle):
            a[i], a[n - d + i] = a[n - d + i], a[i]

    return a


if __name__ == "__main__":
    n, d = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, d)
    print(*answer, sep=' ')
