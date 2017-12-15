from operations import *
import var


def operation_selection(prompt='choose the operation you would like to perform:'):
    print(var.operations)
    var.selection = input(prompt)
    print('you have chosen: ', var.selection)
    print('          ==============================         ')
    if var.selection == var.operations[0]:
        arithmetic_summation()
        pass
    elif var.selection == var.operations[1]:
        arithmetic_sequence()
        pass
    else:
        print('unrecognized selection, try again')


def return_answers():
    print('=======', var.selection, '=======')
    if var.selection == var.operations[0] or var.operations[1]:  # if selection is arithmetic
        if var.d:
            print('common difference :', var.d)
        if var.n:
            print('index "n" :', var.n)
        if var.aSub1:
            print('a sub 1 : ', var.aSub1)
        if var.selection == var.operations[1]:
            if var.aSubN:
                print('a sub ', var.n, ': ', var.aSubN)  # prints a sub n if arithmetic sequence was chosen
                pass
        if var.selection == var.operations[0]:
            if var.sSubN:
                print('s sub ', var.n, ': ', var.sSubN)  # prints partial sum if arithmetic summation was chosen
                pass
        pass


def init():
    print('\nWelcome to Zaxy - an advanced mathematical calculator')
    print('\n')
    print('                                           Created by Hope - Beta v0.2')
    print('                    ==================Enjoy==================')
