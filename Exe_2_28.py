#   Есть код, которыйнельзя изменять.
#   Единственный способ вашего взаимодействия с этим кодом - посредством задания
#   функции transformation.
#   Получить список не преобразывывая, как есть.


transformation = lambda x: x * 1
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))
print(transformed_values)