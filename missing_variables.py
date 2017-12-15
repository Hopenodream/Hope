import var
import math

v = var


def common_change_missing():
    if not v.aSubX:
        v.aSubX = float(input('a sub x>>>'))
        pass
    if not v.x:
        v.x = int(input('x in a sub x>>>'))
        pass
    if not v.aSubY:
        v.aSubY = float(input('a sub y>>>'))
        pass
    if not v.y:
        v.y = int(input('y in a sub y>>>'))
        pass
    pass


pass


def a_sub_1_missing():
    if v.selection == v.operations[0] or v.operations[1]:  # if selection is arithmetic
        if not v.d:
            v.d = float(input('common difference>>>'))
            pass
        if not v.aSubX:
            v.aSubX = float(input('a sub x >>>'))
            pass
        if not v.x:
            v.x = int(input('value of x >>>'))
            pass
        pass
    pass
    if v.selection == v.operations[2] or v.operations[3]:  # if selection is geometric
        if not v.sSubN:
            v.sSubN = float(input('s sub n>>>'))
            pass
        if not v.r:
            v.r = float(input('common rate>>>'))
            pass
        if not v.n:
            v.n = int(input('index "n">>>'))
            pass
        pass
    pass


pass


def index_missing():
    if v.selection == v.operations[0] or v.operations[1]:  # if selection is arithmetic
        if not v.aSubN:
            v.aSubN = float(input('a sub n>>>'))
            pass
        if not v.d:
            v.d = float(input('common difference>>>'))
            pass
        if not v.aSub1:
            v.aSub1 = float(input('a sub 1>>>'))
            pass
        pass
    pass
    if v.selection == v.operations[2] or v.operations[3]:  # if selection is geometric
        if not v.r:
            v.r = float(input('common rate>>>'))
            pass
        if not v.sSubN:
            v.sSubN = float(input('s sub n>>>'))
            pass
        if not v.aSub1:
            v.aSub1 = float(input('a sub 1>>>'))
            pass
        pass
    pass


pass


def a_sub_n_missing():
    if v.selection == v.operations[0] or v.operations[1]:
        if not v.aSub1:
            v.aSub1 = float(input('first value in sequence>>>'))
            pass
        if not v.d:
            v.d = float(input('common difference>>>'))
            pass
        if not v.n:
            v.n = int(input('index (n)>>>'))
            pass
        pass
    pass
    if v.selection == v.operations[2] or v.operations[3]:
        if not v.aSub1:
            v.aSub1 = float(input('first value in sequence>>>'))
        if not v.r:
            v.r = float(input('common rate>>>'))
        if not v.n:
            v.n = int(input('index (n)>>>'))
            pass
        pass
    pass


pass


def s_sub_n_missing():
    if v.selection == v.operations[0] or v.operations[1]:
        if not v.n:
            v.n = int(input('how many numbers of sequence to add up (n)>>>'))
            pass
        if not v.aSub1:
            v.aSub1 = float(input('value of first number in sequence>>>'))
            pass
        if not v.aSubN:
            v.aSubN = float(input('value of last value in series being added>>>'))
            pass
        pass
    pass
    if v.selection == v.operations[2] or v.operations[3]:
        if not v.aSub1:
            v.aSub1 = float(input('first number in sequence>>>'))
            pass
        if not v.r:
            v.r = float(input('common rate>>>'))
            pass
        if not v.n:
            v.n = int(input('index>>>'))
            pass
        pass
    pass


pass


# =============finding viables===============#

def find_a_sub_1():
    if v.selection == v.operations[0] or v.operations[1]:
        v.aSub1 = v.aSubX + v.d * (1 - v.x)
        pass
    if v.selection == v.operations[2] or v.operations[3]:
        v.aSub1 == v.sSubN * ((1 - v.r) / (1 - pow(v.r, v.n)))
        pass
    pass


pass


def find_common_change():
    if v.selection == v.operations[0] or v.operations[1]:
        v.d = (v.aSubX - v.aSubY) / (v.x - v.y)
        pass
    if v.selection == v.operations[2] or v.operations[3]:
        v.r = pow((v.aSubX / v.aSubY), (1 / v.x - v.y))
        pass
    pass


pass


"""    # this is a duplicate, remove after a_sub_n is tested and working                              
def find_nth_value():
    if calculator.v.selection == calculator.v.operations[0] or calculator.v.operations[1]:
        calculator.v.aSubN = calculator.v.aSub1 + (calculator.v.d * (calculator.v.n - 1))
    if calculator.v.selection == calculator.v.operations[2] or calculator.v.operations[3]:
        print('this section is in progress')
"""


def find_index():
    if v.selection == v.operations[0] or v.operations[1]:
        v.n = ((v.aSubN - v.aSub1) / v.d) + 1
        pass
    if v.selection == v.operations[2] or v.operations[3]:
        v.n = math.log(1 - ((v.sSubN / v.aSub1) * (1 - v.r)), v.r)
        pass
    pass


pass


def find_s_sub_n():
    if v.selection == v.operations[0] or v.operations[1]:
        v.sSubN = (v.n * (v.aSub1 + v.aSubN)) / 2
        pass
    if v.selection == v.operations[2] or v.operations[3]:
        v.sSubN = v.aSub1 * ((1 - v.r ** v.n) / (1 - v.r))
        pass
    pass


pass


def find_a_sub_n():
    if v.selection == v.operations[0] or v.operations[1]:
        v.aSubN = v.aSub1 + v.d * (v.n - 1)
        pass
    if v.selection == v.operations[2] or v.operations[3]:
        v.aSubN = v.aSub1 * pow(v.r, v.n - 1)
        pass
    pass


pass
