#   Все равны, как на подбор
#   Напишите функцию same_by, которая проверяет, все ли объекты имеют одинаковые значения
#   и возвращ. True, если это так.
#   Если значения характер. для разных объктов - то False.
#   Для пустого набора объектов, функция должна возвращать True.



def sam_by(chracteristic, object):
    res = list(map(chracteristic, object))
    for i in res:
        if i != res[0]:
            return False
    return True

differ_num = [4, 8, 15, 16, 21, 25, 32]
if sam_by(lambda x: x % 2, differ_num):
    print('same')
else:
    print('different')

differ_num2 = [4, 32, 16] #[4, 9, 16, 17, 22, 25, 33]
if sam_by(lambda x: x % 2, differ_num2):
    print('same')
else:
    print('different')