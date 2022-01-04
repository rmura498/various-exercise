"""
Fizz Buzz is a classic simple problem in computer science,
often used as an exercise in interviews

Write a function tha accepts an integer i, and

if i is multiple of 3, print Fizz instead of the number
if i is multiple of 5, print Buzz instead of the number
if i is multiple of both 3 and 5, print FizzBuzz instead of the number
if no condition are met print the number i

Test the function with all the numbers between 1 and N.
"""


def is_multiple_of(number, d):
    if (number % d) == 0:
        return True
    return False


divider_3 = 3
divider_5 = 5


def FizzBuzz(number):
    cond1 = is_multiple_of(number, divider_3)
    cond2 = is_multiple_of(number, divider_5)

    if cond1 and cond2:
        print("FizzBuzz")
    elif cond1:
        print("Fizz")
    elif cond2:
        print("Buzz")

    else:
        print(number)


for i in range(26):
    FizzBuzz(i)
