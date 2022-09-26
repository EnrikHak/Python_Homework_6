#   Винни-Пух считает, что ритм есть, если число слогов в каждой фразе стихотворения одинаковые.
#   Фраза может состоять из одного слова, если во фрезе несколько слов, то они разделяются дефисами.
#   Фразы отделяются друг от друга пробелами.




fraza = 'Papa-ram pam-pam pam-pam-param pa-ra-pa-dam '.split()

print(fraza)

spisok = [(i for i in fraza)]

if len(set(spisok)) == fraza:
    result = 'Param pam-pam'
else:
    result = 'Pam param'

print(result)