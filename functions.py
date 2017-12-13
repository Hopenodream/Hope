from operations import *
import var


def operation_selection(prompt='choose the operation you would like to perform:'):
    print(var.operations)
    selection = input(prompt)
    print('you have chosen: ', selection)
    print('                ==============================         ')
    if selection == var.operations[0]:
        arithmetic_summation()
        pass
    elif selection == var.operations[1]:
        arithmetic_sequence()
        pass
    else:
        print('unrecognized selection, try again')


def return_answers(operation):
    print('=======', operation, '=======')
    if operation == var.operations[0] or var.operations[1]:
        print('common difference ', d)
        print('index "n" ', var.n)
        print('a sub 1 ', var.aSub1)
        if operation == var.operations[1]:
            print('a sub n ', var.aSubN)  # prints a sub n if arithmetic sequence was chosen
            pass
        if operation == var.operations[0]:
            print('s sub n ', var.sSubN)  # prints partial sum if arithmetic summation was chosen
            pass
        pass
    pass
