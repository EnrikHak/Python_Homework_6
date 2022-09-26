#   Планеты вращаются вокруг звезд по эллиптическим орбитам. Самая дальняя планета, где орбита имеет самую большую площадь.
#   Написать функцию, которая среди списка орбит планет найдет ту, по которой вращ, самая далекая планета.
#   Круговые орбиты не учитываайте: вы знаете что у вашей звезды, таких планет нет, есть только спутники которые были запущенны искусственно.
#   Результатом должен быть кортеж, (содержащай длины полуосей эллипса орбиты самой далекой планеты).
#   Каждая орбита представляет собой кортеж из пары чисел - полуосей и элипса.
#   Площадь элипса вычисл. по формуле S = pi*a*b, где a, b - длины полуосей элипса.


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Pi = 3.14159265359
def find_fathest_orbit(orbits):
    for i in orbits:
        if i[0] == i[1]:
            orbits = list(map(lambda i: Pi * i[0] *  i[1], orbits))
    return orbits
print(find_fathest_orbit(orbits))

#print(find_fathest_orbit(orbits))