from function import summ, mult, stepow
from log import print_result



print('Welcome!!!')


table = int(input('Выберите какую таблицу вы хотите видеть\n1 - Умножение\n2 - Сложение\n3 - Возведение в степень:\n '))

if table == 1:
    row = int(input('Введите количество строк: '))
    column = int(input('Введите количество столбцов: '))
    result = mult(row, column)

elif table == 2:
    row = int(input('Введите количество строк: '))
    column = int(input('Введите количество столбцов: '))
    result = summ(row, column)

elif table == 3:
    row = int(input('Введите количество строк: '))
    column = int(input('Введите количество столбцов: '))
    result = stepow(row, column)

print_result(result)




