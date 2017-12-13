from missing_variables import *
from functions import *


def arithmetic_summation():
    print('for the following value inputs, type "missing" if the value is unknown')
    ASub1 = (input('whats the first value in the sequence'))
    ASubN = (input('whats the value of A given a value of n'))
    n = (input('value of n for A sub n...'))

    if ASub1 == 'missing':
        a_sub_1_missing()
        find_a_1()
        pass
    elif ASubN == 'missing':
        a_sub_n_missing()
        pass
    elif n == 'missing':
        n_missing()
        find_n()
        pass
    answer = (n * (ASub1 + ASubN)) / 2
    print('the answer is ', answer)
    #test


pass


def arithmetic_sequence():
    print('for the following value inputs, leave it blank if the value is unknown')
    asub1 = (input('first value in sequence >>>'))
    d = (input('common difference >>>'))
    n = (input('index of the number you\'re trying to find in the sequence'))

    if not asub1:
        print('=====finding a sub 1=====')
        values = list(a_sub_1_missing())
        solvedasub1 = find_a_1(values[0], values[1], values[2])
        print('a sub 1: ', solvedasub1)
        pass
    elif not d:
        print('=====finding the common difference=====')
        values = list(d_missing())
        asubx, x, asuby, y = values[0], values[1], values[2], values[3]
        d = float(find_common_difference(asubx, x, asuby, y))
        print('common difference:  ', d)
        pass
    elif not n:
        print('=====finding the nth index=====')
        values = list(n_missing())
        n = float(find_n(values[0], values[1], values[2]))
        print('index "n" ', int(n))
        pass
    asubn = find_a_sub_n(float(d), float(asub1), int(n))
    print('a sub n ', asubn)
