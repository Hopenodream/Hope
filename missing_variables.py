def d_missing():
    asubx = float(input('a sub x>>>'))
    x = int(input('x in a sub x>>>'))
    asuby = float(input('a sub y>>>'))
    y = int(input('y in a sub y>>>'))
    return asubx, x, asuby, y


def a_sub_1_missing():
    d = float(input('common difference>>>'))
    aSubX = float(input('a sub x >>>'))
    x = int(input('value of x >>>'))
    return d, aSubX, x


def n_missing():
    aSubN = float(input('a sub n'))
    d = float(input('common difference'))
    aSub1 = float(input('a sub 1'))
    return aSubN, d, aSub1


def a_sub_n_missing():
    aSub1 = float(input('first value of sequence'))
    d = float(input('common difference'))
    n = int(input('order of value in sequence (n)'))
    return d, aSub1, n


def s_sub_n():
    n = int(input('how many numbers of sequence to add up (n)'))
    aSub1 = float(input('value of first number in sequence'))
    aSubN = float(input('value of last value in series being added'))
    return n, aSub1, aSubN


# =============finding variables===============#

def find_a_1(CommonDifference, ASubX, x):
    ASub1 = ASubX + CommonDifference * (1 - x)
    return ASub1


def find_common_difference(asubx, x, asuby, y):
    commondifference = (asubx - asuby) / (x - y)
    return commondifference


def find_nth_value(n, commondifference, ASub1):
    ASubN = ASub1 + (commondifference * (n - 1))
    return ASubN


def find_n(ASubN, CommonDifference, ASub1):
    n = ((ASubN - ASub1) / CommonDifference) + 1
    return n


def find_s_sub_n(n, aSub1, aSubN):
    sSubN = (n * (aSub1 + aSubN)) / 2
    return sSubN


def find_a_sub_n(d, asub1, n):
    asubn = asub1 + d * (n - 1)
    return asubn
