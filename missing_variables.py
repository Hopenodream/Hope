import var
import math

def d_missing():
    if not var.aSubX:
        var.aSubX = float(input('a sub x>>>'))
        pass
    if not var.x:
        var.x = int(input('x in a sub x>>>'))
        pass
    if not var.aSubY:
        var.aSubY = float(input('a sub y>>>'))
        pass
    if not var.y:
        var.y = int(input('y in a sub y>>>'))
        pass


def a_sub_1_missing():
    if not var.d:
        var.d = float(input('common difference>>>'))
        pass
    if not var.aSubX:
        var.aSubX = float(input('a sub x >>>'))
        pass
    if not var.x:
        var.x = int(input('value of x >>>'))
        pass


def n_missing():
    if var.selection == var.operations[0] or var.operations[1]:  # if selection is arithmetic
        if not var.aSubN:
            var.aSubN = float(input('a sub n>>>'))
        if not var.d:
            var.d = float(input('common difference>>>'))
        if not var.aSub1:
            var.aSub1 = float(input('a sub 1>>>'))
    elif var.selection == var.operations[2] or var.operations[3]:  # if selection is geometric
        if not var.r:
            var.r = float(input('common rate>>>'))
        if not var.sSubN:
            var.sSubN = float(input('s sub n>>>'))
        if not var.aSub1:
            var.aSub1 = float(input('a sub 1>>>'))

def a_sub_n_missing():
    if not var.aSub1:
        var.aSub1 = float(input('first value of sequence>>>'))
        pass
    if not var.d:
        var.d = float(input('common difference>>>'))
        pass
    if not var.n:
        var.n = int(input('order of value in sequence (n)>>>'))
        pass


def s_sub_n():
    if not var.n:
        var.n = int(input('how many numbers of sequence to add up (n)>>>'))
        pass
    if not var.aSub1:
        var.aSub1 = float(input('value of first number in sequence>>>'))
        pass
    if not var.aSubN:
        var.aSubN = float(input('value of last value in series being added>>>'))
        pass


# =============finding variables===============#

def find_a_1(rate, asubx, xval):
    if var.selection == var.operaions[0] or var.operations[1]:
        var.aSub1 = asubx + rate * (1 - xval)
    elif var.selection == var.operations[2], var.operations[3]:
        var.aSub1 ==


def find_common_difference(asubx, xval, asuby, yval):
    var.d = (asubx - asuby) / (xval - yval)


def find_nth_value(index, commond, asub1):
    var.aSubN = asub1 + (commond * (index - 1))


def find_n(asubn, commondifference, asub1):
    if var.selection == var.operations[0] or var.operations[1]:
        var.n = ((asubn - asub1) / commondifference) + 1
    if var.selection == var.operations[2] or var.operations[3]:
        var.n = log(1 - ((var.sSubN / var.aSub1) * (1 - var.r)), var.r)

def find_s_sub_n(n, asub1, asubn, r):
    if var.selection == var.operations[0] or var.operations[1]:
        var.sSubN = (n * (asub1 + asubn)) / 2
    elif var.selection == var.operations[2] or var.operations[3]:
        var.sSubN = asub1 * ((1 - r ** n) / (1 - r))

def find_a_sub_n(d, asub1, n):
    var.aSubN = asub1 + d * (n - 1)
