from msilib.schema import tables


def summ(row, column):
    for i in range(1, row + 1):
        for k in range(1, column + 1):
            print(f'{i} + {k} = {i + k}\t', end='')
        print('')
    return row, column


def mult(row, column):
    for i in range(1, row + 1):
        for k in range(1, column + 1):
            print(f'{i} * {k} = {i * k}\t', end='')
        print('')
    return row, column


def stepow(row, column):
    for i in range(1, row + 1):
        for k in range(1, column + 1):
            print(f'{i} ** {k} = {i**k}\t', end='')
        print('')
    return row, column
