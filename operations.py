import missing_variables
import var

mv = missing_variables
v = var


def arithmetic_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    # these values should be stored in the global variable
    mv.s_sub_n_missing()

    if not v.aSub1:
        mv.a_sub_1_missing()
        mv.find_a_sub_1()
        pass
    if not v.aSubN:
        mv.a_sub_n_missing()
        mv.find_a_sub_n()
        pass
    if not var.n:
        mv.index_missing()
        mv.find_index()
        pass
    mv.find_s_sub_n()
    pass


pass


def arithmetic_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    
    mv.a_sub_n_missing()
    if not v.aSub1:
        mv.a_sub_1_missing()
        mv.find_a_sub_1()
        pass
    if not v.d:
        mv.common_change_missing()
        mv.find_common_change()
        pass
    if not v.n:
        mv.index_missing()
        mv.find_index()
        pass
    mv.mv.find_a_sub_n()
    pass


pass


def geometric_sequence():
    print('for the following value inputs, leave blank if the value is unknown')
    
    mv.a_sub_n_missing()
    if not v.aSub1:
        mv.a_sub_1_missing()
        mv.find_a_sub_1()
        pass
    if not v.r:
        mv.common_change_missing()
        mv.find_common_change()
        pass
    if not v.n:
        mv.index_missing()
        mv.find_index()
        pass
    mv.find_a_sub_n()
    pass


pass


def geometric_summation():
    print('for the following value inputs, leave blank if the value is unknown')
    
    mv.s_sub_n_missing()
    if not v.aSub1:
        mv.a_sub_1_missing()
        mv.find_a_sub_1()
        pass
    if not v.r:
        mv.common_change_missing()
        mv.find_common_change()
        pass
    if not v.n:
        mv.index_missing()
        mv.find_index()
        pass
    mv.find_s_sub_n()
    pass


pass
