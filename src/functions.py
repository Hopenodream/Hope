from src import operations, var

v = var
o = operations


def operation_selection(prompt='choose the operation you would like to perform:'):
    print(var.operations)
    v.selection = input(prompt)
    print('you have chosen: ', v.selection)
    print('          ==============================         ')
    if v.selection == var.operations[0]:
        o.arithmetic_summation()
        pass
    elif v.selection == v.operations[1]:
        o.arithmetic_sequence()
        pass
    elif v.selection == v.operations[2]:
        o.geometric_summation()
        pass
    elif v.selection == v.operations [3]:
        o.geometric_sequence()
        pass
    else:
        print('unrecognized selection, try again')
        pass
    pass


pass


def return_answers():
    print('=======', v.selection, '=======')
    if v.selection == var.operations[0] or var.operations[1]:  # if v.selection is arithmetic
        if v.d:
            print('common difference :', v.d)
            pass
        if v.n:
            print('index "n" :', v.n)
            pass
        if v.aSub1:
            print('a sub 1 : ', v.aSub1)
            pass
        if v.selection == var.operations[1]:
            if v.aSubN:
                print('a sub ', v.n, ': ', v.aSubN)  # prints a sub n if arithmetic sequence was chosen
                pass
        if v.selection == var.operations[0]:
            if v.sSubN:
                print('s sub ', v.n, ': ', v.sSubN)  # prints partial sum if arithmetic summation was chosen
                pass
        pass
    pass


pass


def init():
    print('\nWelcome to Zaxy - an advanced mathematical calculator')
    print('\n')
    print('                                           Created by Hope - Beta v0.2')
    print('                    ==================Enjoy==================')