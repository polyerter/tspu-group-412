# списки

a = []

# добавление элемента к конец списка
a.append(1)
a.append(2)

print(
    'list:', a
)

# длина списка
print(
    'len:', len(a)
)

# получение элемента по индексу
print(
    'first element:', a[0]
)

# создание последовательности
b = list(range(6, 20, 2))
print(
    'b:', b
)

#max и min
c = [2, 4, 1, -1, 8 ,10, 22, 2, 2, 2, 2]

print(
    'max:', max(c),
    'min:', min(c)
)

# сумма
print(
    'sum:', sum(c)
)

# сортировка А-Я
c.sort()

print(
    'sort:', c
)

# сортировка Я-А
c.sort(reverse=True)

print(
    'sort:', c
)

# кол-во элементов по значению
print(
    'count:', c.count(2)
)

# удаление по индексу
del c[0]

print(
    'c:', c
)

# удаление по значение
c.remove(2)

print(
    'c:', c
)

# 

d = ['яблоки', 'дыни', 'груши', 'клубника']
e = d.pop()

print(
    'd:', d,
    'e:', e,
)


# копирование
f = d.copy()
f.append('арбуз')

print(
    'd:', d,
    '\nf:', f,
)


