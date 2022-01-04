"""More general solution:
There is no control coupling between the main and the fizzbuzz function
because there is not a flag that control the inner behavior of the fb function
Who write the fb function is free to change every line of the implementation
He cannot change the interface of the function
There is no coupling between fb and the other functions
if you change the name of multiple of for sure you have to change the main
but not the fb function, because it receives a reference to the function
And the last point: if you need to add some functions, some new conditions,
you have to change only the definition of the references in the main
"""


def is_multiple_of(value1, value2):
    return value1 % value2 == 0


def is_grater_than(value1, value2):
    return value1 > value2


def new_c():
    # ...
    pass


def fb(i, v1, v2, r_condition):
    cond_1 = r_condition(i, v1)
    cond_2 = r_condition(i, v2)

    if cond_1 and cond_2:
        print("fizzbuzz")
    elif cond_1:
        print("Fizz")
    elif cond_2:
        print("Buzz")
    else:
        print(i)


# main
r_condition = is_multiple_of
v1 = 3
v2 = 5
for i in range(30):
    fb(i, v1, v2, r_condition)

