# Словари

person = {
    'name': 'John',
    'age': 18,
    'last_name': 'Johnson',
    # 'address': 'Durand, Michigan(MI), 48429 Mount Street',
    'address': {
        'city': 'Durand',
        'state': 'Michigan(MI)',
        'zip': 48429,
        'street': 'Mount Street'
    },
    'phone': None,
}

print(
    'person: ', person,
)
# result:
# person:  {'name': 'John', 'age': 18, 'last_name': 'Johnson', 'address': {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}, 'phone': None}

# Получение значений

print(
    'name: ', person.get('name'),
    'name: ', person['name'], 
    # 'email: ', person['email'],
    'email: ', person.get('email', None),
)
# result:
# name:  John name:  John email:  None

# Получение только значений словаря
print(
    person.values()
)
# result:
# dict_values(['John', 18, 'Johnson', {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}, None])

# Получить только ключи
print(
    person.keys()
)
# result:
# dict_keys(['name', 'age', 'last_name', 'address', 'phone'])

# Получени: пар ключ-значение
print(
    person.items()
)
# dict_items([('name', 'John'), ('age', 18), ('last_name', 'Johnson'), ('address', {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}), ('phone', None)])

for k in person.items():
    print(k)


for k in person.values():
    print(k)


# Добавление значения
person['birthday'] = '2005-06-14'
print(
    'person: ', person
)

person.setdefault('birthday', '2005-06-14')
print(
    'person: ', person
)