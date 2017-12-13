from missing_variables import *
from functions import *


def arithmetic_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    asub1 = (input('whats the first value in the sequence>>>'))
    asubn = (input('whats the value of A given a value of n>>>'))
    index = (input('value of n for A sub n>>>'))

    if not asub1:
        values = list(a_sub_1_missing())
        ASub1 = find_a_1(values[0], values[1], values[2])
        pass
    elif not asubn:
        values = list(a_sub_n_missing())
        ASubN = find_a_sub_n(values[0], values[1], values[2])
        pass
    elif not index:
        values = list(n_missing())
        n = find_n(values[0], values[1], values[2])
        pass
    sSubN = (n * (ASub1 + ASubN)) / 2
    print('the answer is ', sSubN)


pass


def arithmetic_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    asub1 = (input('first value in sequence >>>'))
    commond = (input('common difference >>>'))
    index = (input('index of the number you\'re trying to find in the sequence'))

    if not asub1:
        print('=====finding a sub 1=====')
        values = list(a_sub_1_missing())
        ASub1 = find_a_1(values[0], values[1], values[2])
        pass
    elif not commond:
        print('=====finding the common difference=====')
        values = list(d_missing())
        asubx, x, asuby, y = values[0], values[1], values[2], values[3]
        d = float(find_common_difference(asubx, x, asuby, y))
        pass
    elif not index:
        print('=====finding the nth index=====')
        values = list(n_missing())
        n = float(find_n(values[0], values[1], values[2]))
        pass
    asubn = find_a_sub_n(float(d), float(asub1), int(n))
    print('a sub n ', asubn)
