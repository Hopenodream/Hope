from missing_variables import *
from functions import *


def arithmetic_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    # these values should be stored in the global variable
    aSub1 = (input('whats the first value in the sequence>>>'))
    aSubN = (input('whats the value of A given a value of n>>>'))
    n = (input('value of n for A sub n>>>'))

    if not aSub1:
        values = list(a_sub_1_missing())
        aSub1 = find_a_1(values[0], values[1], values[2])
        pass
    if not aSubN:
        values = list(a_sub_n_missing())
        aSubN = find_a_sub_n(values[0], values[1], values[2])
        pass
    if not n:
        values = list(n_missing())
        n = find_n(values[0], values[1], values[2])
        pass
    sSubN = (n * (aSub1 + aSubN)) / 2


pass


def arithmetic_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    aSub1 = (input('first value in sequence >>>'))
    d = (input('common difference >>>'))
    n = (input('index of the number you\'re trying to find in the sequence'))

    if not aSub1:
        values = list(a_sub_1_missing())
        aSub1 = find_a_1(values[0], values[1], values[2])
        pass
    if not d:
        values = list(d_missing())
        d = float(find_common_difference(values[0], values[1], values[2], values[3]))
        pass
    if not n:
        values = list(n_missing())
        n = float(find_n(values[0], values[1], values[2]))
        pass
    aSubN = find_a_sub_n(float(d), float(aSub1), int(n))
