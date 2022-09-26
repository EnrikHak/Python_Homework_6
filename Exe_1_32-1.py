#   Нас попросили сделать в плюс к таблице умножения ещё и таблицу возведения в степень.
#   Чтоб не копироват код и обобщать все функции в одну, напишите функцию, которая
#   принимает в качестве аргумента функцию, вычисляющую элемент по строке и столбцу.



table = int(input('Выберите какую таблицу вы хотите видеть\n1 - Умножение\n2 - Сложение\n3 - Возведение в степень:\n '))
row = int(input('Число на строке: '))
column = int(input('Число в столбце: '))

def print_operation_table(row, column):
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            if table == 1:
                result_mult = lambda i, j: i*j
                print(result_mult)
            if table == 2:
                result_summ = lambda i, j: i+j
                print(result_summ)
            if table == 3:
                result_pow = lambda i, j: i**j
                print(result_pow)

print(print_operation_table(row, column))