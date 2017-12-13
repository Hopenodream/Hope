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
    if operation == 'arithmetic sequence':
        print('a sub n ', ASubN)
        print('common difference ', d)
        print('index "n" ', n)
        print('a sub 1 ', ASub1)
        pass
    elif operation == 'arithmetic summation':
        print('s sub n ', sSubN)
        print('index "n" ', n)
        print('common difference ', d)
        print('a sub 1 ', ASub1)

# =============all variables===================#


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
