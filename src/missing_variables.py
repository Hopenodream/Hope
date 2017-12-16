from src import var
import math

v = var


def common_change_missing():
    if not v.aSubX:
        v.aSubX = input('a sub x>>>')
        pass
    if not v.x:
        v.x = input('x in a sub x>>>')
        pass
    if not v.aSubY:
        v.aSubY = input('a sub y>>>')
        pass
    if not v.y:
        v.y = input('y in a sub y>>>')
        pass
    pass


pass


def a_sub_1_missing():
    if v.selection in {v.operations[0], v.operations[1]}:  # if selection is arithmetic
        if not v.d:
            v.d = input('common difference>>>')
            pass
        if not v.aSubX:
            v.aSubX = input('a sub x >>>')
            pass
        if not v.x:
            v.x = input('value of x >>>')
            pass
        pass
    pass
    if v.selection in {v.operations[2], v.operations[3]}:  # if selection is geometric
        if not v.sSubN:
            v.sSubN = input('s sub n>>>')
            pass
        if not v.r:
            v.r = input('common rate>>>')
            pass
        if not v.n:
            v.n = input('index "n">>>')
            pass
        pass
    pass


pass


def index_missing():
    if v.selection in {v.operations[0], v.operations[1]}:  # if selection is arithmetic
        if not v.aSubN:
            v.aSubN = input('a sub n>>>')
            pass
        if not v.d:
            v.d = input('common difference>>>')
            pass
        if not v.aSub1:
            v.aSub1 = input('a sub 1>>>')
            pass
        pass
    pass
    if v.selection == v.operations[2] or v.operations[3]:  # if selection is geometric
        if not v.r:
            v.r = input('common rate>>>')
            pass
        if not v.sSubN:
            v.sSubN = input('s sub n>>>')
            pass
        if not v.aSub1:
            v.aSub1 = input('a sub 1>>>')
            pass
        pass
    pass


pass


def a_sub_n_missing():
    if v.selection in {v.operations[0], v.operations[1]}:
        if not v.aSub1:
            v.aSub1 = input('first value in sequence>>>')
            pass
        if not v.d:
            v.d = input('common difference>>>')
            pass
        if not v.n:
            v.n = input('index (n)>>>')
            pass
        pass
    pass
    if v.selection in {v.operations[2], v.operations[3]}:
        if not v.aSub1:
            v.aSub1 = input('first value in sequence>>>')
        if not v.r:
            v.r = input('common rate>>>')
        if not v.n:
            v.n = input('index (n)>>>')
            pass
        pass
    pass


pass


def s_sub_n_missing():
    if v.selection in {v.operations[0], v.operations[1]}:
        if not v.n:
            v.n = input('index (n)>>>')
            pass
        if not v.aSub1:
            v.aSub1 = input('first number in sequence>>>')
            pass
        if not v.aSubN:
            v.aSubN = input('value given index n>>>')
            pass
        pass
    pass
    if v.selection in {v.operations[2], v.operations[3]}:
        if not v.aSub1:
            v.aSub1 = input('first number in sequence>>>')
            pass
        if not v.r:
            v.r = input('common rate>>>')
            pass
        if not v.n:
            v.n = input('index>>>')
            pass
        pass
    pass


pass


# =============finding variables===============#

def find_a_sub_1():
    if v.selection in {v.operations[0], v.operations[1]}:
        v.aSub1 = v.aSubX + v.d * (1 - v.x)
        pass
    if v.selection in {v.operations[2], v.operations[3]}:
        v.aSub1 == v.sSubN * ((1 - v.r) / (1 - pow(v.r, v.n)))
        pass
    pass


pass


def find_common_change():
    if v.selection in {v.operations[0], v.operations[1]}:
        v.d = (v.aSubX - v.aSubY) / (v.x - v.y)
        pass
    if v.selection in {v.operations[2], v.operations[3]}:
        v.r = pow((v.aSubX / v.aSubY), (1 / v.x - v.y))
        pass
    pass


pass


def find_index():
    if v.selection in {v.operations[0], v.operations[1]}:
        v.n = ((v.aSubN - v.aSub1) / v.d) + 1
        pass
    if v.selection in {v.operations[2], v.operations[3]}:
        v.n = math.log(1 - ((v.sSubN / v.aSub1) * (1 - v.r)), v.r)
        pass
    pass


pass


def find_s_sub_n():
    if v.selection in {v.operations[0], v.operations[1]}:
        v.sSubN = (v.n * (v.aSub1 + v.aSubN)) / 2
        pass
    if v.selection in {v.operations[2], v.operations[3]}:
        v.sSubN = v.aSub1 * ((1 - v.r ** v.n) / (1 - v.r))
        pass
    pass


pass


def find_a_sub_n():
    if v.selection in {v.operations[0], v.operations[1]}:
        v.aSubN = v.aSub1 + v.d * (v.n - 1)
        pass
    if v.selection in {v.operations[2], v.operations[3]}:
        v.aSubN = v.aSub1 * pow(v.r, v.n - 1)
        pass
    pass


pass
