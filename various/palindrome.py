# coding=utf-8
"""
1) write a function that receive in input a string
and returns True if the string is palindrome, False otherwise

2) write a function that receives in input a string, and
return a palindrome string. The function must build the
palindrome string adding characters on the left of the initial string

3) as in 2, but the function must add the minimum number of character on the left
"""


def reverse_string(string):
    rev_string = ''
    for character in string:
        rev_string = character + rev_string
    return rev_string


def create_palindrome3(string):
    if is_palindrome(string):
        return string
    other_string = ''
    for idx in range(len(string)):

        s_pal = string[:idx]
        if is_palindrome(s_pal):
            palindrome_part=s_pal
            i=idx


    rev_string = reverse_string(string[i:])
    return rev_string + palindrome_part+string[i:]


def create_palindrome(string):
    if is_palindrome(string):
        return string
    s_pal = string
    for character in string:
        s_pal = character + s_pal
        print('Building palindrome', s_pal)
    return s_pal


def is_palindrome(string):  # retunr s==s[::-1]
    rev_string = reverse_string(string)
    if bool(string.count(rev_string)):
        return True
    return False


#list_of_strings = ['abaxabak']
list_of_strings = ['A',
                   'AA', 'AX',
                   'ABA', 'AAX', 'AXY',
                   'ABBA', 'ABAX', 'AAXY', 'AXYW',
                   'ABCA', 'ABBAX', 'ABAXY', 'AAXYW', 'AXYWZ']

print('\n PALINDROME \n')
for s in list_of_strings:
    print('String: ', s)
    # s_pal = create_palindrome(s)
    s_pal3 = create_palindrome3(s)
    print(s, '->', s_pal3)
    if not is_palindrome(s_pal3):
        print('ERROR! The string is not palindrome')
    else:
        print("It is palindrome")
