#test
def d_missing():
    asubx = float(input('a sub x...'))
    x = int(input('x in a sub x'))
    asuby = float(input('a sub y'))
    y = int(input('y in a sub y'))
    return asubx, x, asuby, y
    pass


def a_sub_1_missing():
    d = float(input('common difference>>>'))
    aSubX = float(input('a sub x >>>'))
    x = int(input('value of x >>>'))
    return d, aSubX, x
    pass


def n_missing():
    aSubN = input('a sub n')
    d = input('common difference')
    aSub1 = input('a sub 1')
    pass


def a_sub_n_missing():
    aSub1 = input('first value of sequence')
    d = input('common difference')
    n = input('order of value in sequence (n)')
    pass


def s_sub_n():
    n = input('how many numbers of sequence to add up (n)')
    aSub1 = input('value of first number in sequence')
    aSubN = input('value of last value in series being added')
    pass


# =============finding variables===============#

def find_a_1(CommonDifference, ASubX, x):
    ASub1 = ASubX + CommonDifference * (1 - x)
    return ASub1


pass


def find_common_difference(asubx, x, asuby, y):
    commondifference = (asubx - asuby) / (x - y)
    return commondifference


pass


def find_nth_value(n, commondifference, ASub1):
    ASubN = ASub1 + (commondifference * (n - 1))
    return ASubN


pass


def find_n(ASubN, CommonDifference, ASub1):
    n = ((ASubN - ASub1) / CommonDifference) + 1
    return n


pass


def find_s_sub_n(n, aSub1, aSubN):
    sSubN = (n * (aSub1 + aSubN)) / 2
    return sSubN
    pass

