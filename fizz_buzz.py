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


def is_multiple_of_3(number):
    if (number % 3) == 0:
        return True
    return False


def is_multiple_of_5(number):
    if (number % 5) == 0:
        return True
    return False


def is_multiple_of_3_5(number):
    if ((number % 3) == 0) and ((number % 5) == 0):
        return True
    return False


def FizzBuzz(number):
    if is_multiple_of_3_5(number):
        print("FizzBuzz")
    elif is_multiple_of_3(number):
        print("Fizz")
    elif is_multiple_of_5(number):
        print("Buzz")

    else:
        print(number)


for i in range(26):
    FizzBuzz(i)
