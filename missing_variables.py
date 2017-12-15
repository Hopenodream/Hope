import var
import math

def common_change_missing():
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
    if var.selection == var.operations[0] or var.operations[1]:  # if selection is arithmetic
        if not var.d:
            var.d = float(input('common difference>>>'))
            pass
        if not var.aSubX:
            var.aSubX = float(input('a sub x >>>'))
            pass
        if not var.x:
            var.x = int(input('value of x >>>'))
            pass
    if var.selction == var.operations[2] or var.operations[3]:  # if selection is geometric
        if not var.sSubN:
            var.sSubN = float(input('s sub n>>>'))
        if not var.r:
            var.r = float(input('common rate>>>'))
        if not var.n:
            var.n = int(input('index "n">>>'))


def index_missing():
    if var.selection == var.operations[0] or var.operations[1]:  # if selection is arithmetic
        if not var.aSubN:
            var.aSubN = float(input('a sub n>>>'))
        if not var.d:
            var.d = float(input('common difference>>>'))
        if not var.aSub1:
            var.aSub1 = float(input('a sub 1>>>'))
    if var.selection == var.operations[2] or var.operations[3]:  # if selection is geometric
        if not var.r:
            var.r = float(input('common rate>>>'))
        if not var.sSubN:
            var.sSubN = float(input('s sub n>>>'))
        if not var.aSub1:
            var.aSub1 = float(input('a sub 1>>>'))

def a_sub_n_missing():
    if var.selection == var.operations[0] or var.operations[1]:
        if not var.aSub1:
            var.aSub1 = float(input('first value in sequence>>>'))
            pass
        if not var.d:
            var.d = float(input('common difference>>>'))
            pass
        if not var.n:
            var.n = int(input('index (n)>>>'))
            pass
    if var.selection == var.operations[2] or var.operations[3]:
        if not var.aSub1:
            var.aSub1 = float(input('first value in sequence>>>'))
        if not var.r:
            var.r = float(input('common rate>>>'))
        if not var.n:
            var.n = int(input('index (n)>>>'))


def s_sub_n_missing():
    if var.selection == var.operations[0] or var.operations[1]:
        if not var.n:
            var.n = int(input('how many numbers of sequence to add up (n)>>>'))
            pass
        if not var.aSub1:
            var.aSub1 = float(input('value of first number in sequence>>>'))
            pass
        if not var.aSubN:
            var.aSubN = float(input('value of last value in series being added>>>'))
            pass
    if var.selection == var.operations[2] or var.operations[3]:
        if not var.aSub1:
            var.aSub1 = float(input('first number in sequence>>>))
        if not var.r:
            var.r = float(input('common rate>>>')
        if not var.n:
            var.n = int(input('index>>>')


# =============finding variables===============#

def find_a_sub_1()):
    if var.selection == var.operaions[0] or var.operations[1]:
        var.aSub1 = var.aSubX + var.d * (1 - var.x)
    if var.selection == var.operations[2], var.operations[3]:
        var.aSub1 == var.sSubN * ((1 - var.r) / (1 - pow(var.r, var.n))


def find_common_change():
    if var.selection == var.operations[0] or var.operations[1]:
        var.d = (var.aSubX - var.aSubY) / (var.x - var.y)
    if var.selection == var.operations[2] or var.operations[3]:
        var.r = pow((var.aSubX / var.aSubY), (1 / var.x - var.y))
                                  
"""    # this is a duplicate, remove after a_sub_n is tested and working                              
def find_nth_value():
    if var.selection == var.operations[0] or var.operations[1]:
        var.aSubN = var.aSub1 + (var.d * (var.n - 1))
    if var.selection == var.operations[2] or var.operations[3]:
        print('this section is in progress')
"""

def find_index():
    if var.selection == var.operations[0] or var.operations[1]:
        var.n = ((asubn - asub1) / commondifference) + 1
    if var.selection == var.operations[2] or var.operations[3]:
        var.n = log(1 - ((var.sSubN / var.aSub1) * (1 - var.r)), var.r)

def find_s_sub_n():
    if var.selection == var.operations[0] or var.operations[1]:
        var.sSubN = (var.n * (var.aSub1 + var.aSubN)) / 2
    if var.selection == var.operations[2] or var.operations[3]:
        var.sSubN = var.aSub1 * ((1 - var.r ** var.n) / (1 - var.r))

def find_a_sub_n():
    if var.selection == var.operations[0] or var.operations[1]:
        var.aSubN = var.aSub1 + var.d * (var.n - 1)
    if var.selection == var.operations[2] or var.operations[3]:
        var.aSubN = var.aSub1 * pow(var.r, var.n - 1)
