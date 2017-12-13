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


pass

# =============all variables===================#

CommonDifference = 0
ASub1 = 0
ASubN = 0
ASubX = 0
ASubY = 0
x = 0
y = 0
sSubN = 0
n = 0
operations = ['arithmetic summation', 'arithmetic sequence', 'geometric summation', 'geometric sequence']
