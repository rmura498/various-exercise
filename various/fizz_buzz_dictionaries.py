def is_multiple_of(value1, value2):
    return value1 % value2 == 0


def is_grater_than(value1, value2):
    return value1 > value2


def gfb(v, dict_of_cond, r_cond):
    string_to_print=''
    for d, s in dict_of_cond.items():
        if r_cond(v, d):
            string_to_print += s
    if not string_to_print:
        string_to_print=str(v)
    return string_to_print


dict1 = {3: 'A', 5: 'B', 7: 'C'}
dict2 = {10: 'X', 20: 'Y', 30: 'Z'}

print(gfb(21, dict1, is_multiple_of))
print(gfb(8,dict1, is_multiple_of))
print(gfb(20, dict2, is_grater_than))