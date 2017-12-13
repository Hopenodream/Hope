def d_missing():
    if not aSubX:
        aSubX = float(input('a sub x>>>'))
        return aSubX
        pass
    if not x:
        x = int(input('x in a sub x>>>'))
        return x
        pass
    if not aSubY
        aSubY = float(input('a sub y>>>'))
        return aSubY
        pass
    if not y:
        y = int(input('y in a sub y>>>'))
        return y
        pass


def a_sub_1_missing():
    if not d:
        d = float(input('common difference>>>'))
        return d
        pass
    if not aSubX:
        aSubX = float(input('a sub x >>>'))
        return aSubX
        pass
    if not x
        x = int(input('value of x >>>'))
        return x
        pass


def n_missing():
    if not aSubN:
        aSubN = float(input('a sub n>>>'))
        return aSubN
        pass
    if not d:
        d = float(input('common difference>>>'))
        return d
        pass
    if not aSub1:
        aSub1 = float(input('a sub 1>>>'))
        return aSub1
        pass


def a_sub_n_missing():
    if not aSub1:
        aSub1 = float(input('first value of sequence>>>'))
        return aSub1
        pass
    if not d:
        d = float(input('common difference>>>'))
        return d
        pass
    if not n:
        n = int(input('order of value in sequence (n)>>>'))
        return n
        pass


def s_sub_n():
    if not n:
        n = int(input('how many numbers of sequence to add up (n)>>>'))
        return n
        pass
    if not aSub1:
        aSub1 = float(input('value of first number in sequence>>>'))
        return aSub1
        pass
    if not aSubN:
        aSubN = float(input('value of last value in series being added'>>>))
        return aSubN
        pass


# =============finding variables===============#

def find_a_1(CommonDifference, asubx, xval):
    ASub1 = asubx + CommonDifference * (1 - xval)
    return aSub1


def find_common_difference(asubx, xval, asuby, yval):
    d = (asubX - asubY) / (xval - yval)
    return d


def find_nth_value(index, commond, asub1):
    aSubN = asub1s + (commond * (index - 1))
    return aSubN


def find_n(asubn, CommonDifference, asub1):
    n = ((asubn - asub1) / CommonDifference) + 1
    return n


def find_s_sub_n(n, asub1, asubn):
    sSubN = (n * (asub1 + asubn)) / 2
    return sSubN


def find_a_sub_n(d, asub1, n):
    aSubN = asub1 + d * (n - 1)
    return aSubN
