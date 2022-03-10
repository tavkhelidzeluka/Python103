from pprint import pprint
# Ordered / Unordered Data Structures

numbers: list[int] = [i for i in range(0, 10, 2)]

numbers.insert(1, 5)
numbers[5] = 9


print(numbers)

# immutable / muttable
tuple_numbers: tuple = (5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4)
# name: str = 'luka'
# name[1] = 'u'

# print(name[0])

print(tuple_numbers, type(tuple_numbers))
print(tuple_numbers[0])

for number in tuple_numbers:
    print(number, end=', ')


print()
# print('luka', 'nika', 25, sep=' 25 ')
# print('luka', sep='gio')

integers: set[int] = {i for i in range(2)}

# separator
print('\n', integers, sep='')
# print(integers)

for num in integers:
    print(num)


# dict

# key value pair
person: dict[str, any] = {
    'name': 'Giorgi',
    'age': 25,
    'student': True,
    'friends': ['Natali', 'Levani'],
    'family': {
        'sister': 'Neli',
        'mother': 'Nia',
        'brothers': ['Brandon', 'Bill']
    },
    1: 'nika'
}
pprint(person)
# print(person['age'])
# print(person['family']['mother'])
# print(person['friends'][1])

person['is_working'] = True
person.pop('student')

person.pop('gela', None)
# del person['gela']

person['age'] += 1
person['friends'].append('Gia')

print(person['family']['brothers'][1])

pprint(person)

print(person.get('job'))

print('-' * 10 + ' Person Keys ' + '-' * 10)
for key in person.keys():
    print(key)


print('-' * 10 + ' Person Values ' + '-' * 10)
for value in person.values():
    print(value)

print('-' * 10 + ' Person Items ' + '-' * 10)

# destructuring
for key, value in person.items():
    print(key, ' - ', value)

print('-' * 10 + ' Person Items with tuples ' + '-' * 10)
for item in person.items():
    print(item[0], ' - ', item[1])

# a, b = [2, 5]
print('-' * 10 + ' Zip ' + '-' * 10)

list_1 = ['name', 'age', 'gender', 'b']
list_2 = ['Nika', 25, 'M']
list_3 = [1, 2, 3]


for gela in zip(list_1, list_2, list_3):
    print(gela)

import random

print('-' * 10 + ' Random ' + '-' * 10)

# 0, 1, 2, 3, 4, 5
random_numbers = [random.randint(0, 5) for _ in range(5)]

# print(random_numbers)



# print(counter)
print(random_numbers)
print(random_numbers.count(5))

# import time 

# s = time.time()

# for _ in range(10000):
#     pass

# print(time.time() - s)

