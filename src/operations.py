from src import missing_variables, var

mv = missing_variables
v = var


def arithmetic_summation():
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
    mv.find_a_sub_n()
    pass


pass


def geometric_sequence():
    
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
