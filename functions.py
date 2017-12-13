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
        print('a sub 1 ', ASub1)
        print('a sub n ', ASubN) if operation == operations[1]
        print('s sub n ', sSubN) if operation == operations[0]
            

# =============all variables===================#

global d, ASub1, ASubN, ASubX, ASubY, x, y, sSubN, n, operations
d = 0
ASub1 = 0
ASubN = 0
ASubX = 0
ASubY = 0
x = 0
y = 0
sSubN = 0
n = 0
operations = ['arithmetic summation', 'arithmetic sequence', 'geometric summation', 'geometric sequence']
