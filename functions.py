from operations import *


def operation_selection(prompt='choose the operation you would like to perform:'):
    print(operations)
    selection = input(prompt)
    print('you have chosen: ', selection)
    print('                ==============================         ')
    if selection == operations[0]:
        arithmetic_summation()
        pass
    elif selection == operations[1]:
        arithmetic_sequence()
        pass
    else:
        print('unrecognized selection, try again')


def return_answers(operation):
    print('=======', operation, '=======')
    if operation == operations[0] or operations[1]:
        print('common difference ', d)
        print('index "n" ', n)
        print('a sub 1 ', aSub1)
        print('a sub n ', aSubN) if operation == operations[1] # prints a sub n if arithmetic sequence was chosen
        print('s sub n ', sSubN) if operation == operations[0] # prints partial sum if arithmetic summation was chosen
        pass
    

# =============all variables===================#


def init():
    global d, ASub1, ASubN, ASubX, ASubY, x, y, sSubN, n, operations
    d = None
    aSub1 = None
    aSubN = None
    aSubX = None
    aSubY = None
    x = None
    y = None
    sSubN = None
    n = None
    operations = ['arithmetic summation', 'arithmetic sequence', 'geometric summation', 'geometric sequence']
