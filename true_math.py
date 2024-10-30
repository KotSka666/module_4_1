from math import inf

def divide(first, second):
    if second == 0:
        return f'{inf}'
    else:
        res = first / second
        return res