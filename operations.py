from missing_variables import *
from functions import *


def arithmetic_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    # these values should be stored in the global variable
    var.aSub1 = float(input('whats the first value in the sequence>>>'))
    var.aSubN = float(input('whats the value of A given an index of n>>>'))
    var.n = int(input('value of n for A sub n>>>'))

    if not var.aSub1:
        a_sub_1_missing()
        find_a_1()
        pass
    if not var.aSubN:
        a_sub_n_missing()
        find_a_sub_n()
        pass
    if not var.n:
        n_missing()
        find_n())
        pass
    find s_sub_n)()


pass


def arithmetic_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    var.aSub1 = float(input('first value in sequence>>>'))
    var.d = float(input('common difference>>>'))
    var.n = int(input('index of the number you\'re trying to find in the sequence'))

    if not var.aSub1:
        a_sub_1_missing()
        find_a_1()
        pass
    if not var.d:
        change_missing()
        find_common_change()
        pass
    if not var.n:
        n_missing()
        find_n()
        pass
    find_a_sub_n()
    
pass


def geometric_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    var.aSub1 = float(input('first value in sequence>>>'))
    var.r = float(input('common rate>>>'))
    var.n = int(input('index'))
    
    if not var.aSub1:
        a_sub_1_missing()
        find_a_1()
    if not var.r:
        change_missing()
        find_common_change()
    if not var.n:
        n_missing()
        find_n()
        pass
    find_a_sub_n()
    
pass


def geometric_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    
