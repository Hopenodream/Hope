### Welcome to Zaxy, an advanced calculator by a python beginner

**Easy to use**: All you need to do is select your desired operation, enter a few values the problem will provide you with, and the caculator returns answers you need to solve the problem

**Open-source**: If you feel the need to add more operations, the project is organized in a way where operations could easily be added

#### How to add operations:
1. Figure out an equation for **_each_** of the variables in a function
2. Add inputs for the values in `opearations.py` i.g.
``` python
    var.aSub1 = float(input('whats the first value in the sequence>>>'))
    var.aSubN = float(input('whats the value of A given an index of n>>>'))
    var.n = int(input('value of n for A sub n>>>'))
```
3. Add missing variable detection
``` python
    if not var.aSub1:
        a_sub_1_missing()
        find_a_1()
        pass
    if not var.d:
        change_missing()
        find_common_change()
        pass
```
4. Add inputs for finding the missing variables in the **_top_** section of `missing_variables.py`
``` python
    def a_sub_1_missing():
      if var.selection == var.operations[0] or var.operations[1]:  # if selection is arithmetic
          if not var.d:
              var.d = float(input('common difference>>>'))
              pass
          if not var.aSubX:
              var.aSubX = float(input('a sub x >>>'))
              pass
          if not var.x:
              var.x = int(input('value of x >>>'))
              pass
```
5. Add calculations for each variable in the **_bottom_** section of `missing_variables.py`
``` python
    if var.selection == var.operaions[0] or var.operations[1]:
        var.aSub1 = var.aSubX + var.d * (1 - var.x)
```

#### Contact me
- [Twitter](https://twitter.com/deathbethecat) - @Deathbethecat
- Discord - @Deathbe9500
