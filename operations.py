from missing_variables import *
from functions import *


def arithmetic_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    # these values should be stored in the global variable
    var.aSub1 = (input('whats the first value in the sequence>>>'))
    var.aSubN = (input('whats the value of A given an index of n>>>'))
    var.n = (input('value of n for A sub n>>>'))

    if not var.aSub1:
        a_sub_1_missing()
        find_a_1(float(var.d), float(var.aSubX), int(var.x))
        pass
    if not var.aSubN:
        a_sub_n_missing()
        find_a_sub_n(var.d, var.aSub1, var.n)
        pass
    if not var.n:
        n_missing()
        find_n(int(var.n), float(var.aSub1), float(var.aSubN))
        pass
    var.sSubN = (int(var.n) * (float(var.aSub1) + float(var.aSubN))) / 2


pass


def arithmetic_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    var.aSub1 = (input('first value in sequence >>>'))
    var.d = (input('common difference >>>'))
    var.n = (input('index of the number you\'re trying to find in the sequence'))

    if not var.aSub1:
        a_sub_1_missing()
        find_a_1(float(var.d), float(var.aSubX), int(var.x))
        pass
    if not var.d:
        d_missing()
        find_common_difference(float(var.aSubX), int(var.x), float(var.aSubY), int(var.y))
        pass
    if not var.n:
        n_missing()
        find_n(int(var.n), float(var.aSub1), float(var.aSubN))
        pass
    find_a_sub_n(float(var.d), float(var.aSub1), int(var.n))
