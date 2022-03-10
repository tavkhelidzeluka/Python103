
# print(False) # statement / expression 

print(45 <= 45 and 45 < 46) # True and True -> True

print(5 == 5 or 'nika' == 'levan') # True or False -> True

x: int = 5
a = 27
b = 'luka'


# list (array)
#                   Index   0       1         2         3
student_names: list[str] = ['Nika', 'Tamari', 'Levani', 'Giorgi', 'Luka']
student_last_names = ['t', 'n', 'c', 's', 'd']

# print(student_names)

print(student_names[0])


# my_list: list[any] = [1, 25, 'Nika', True, [1, 5, 234]]

# print(my_list[4][2])

# list_2d = [  
#     [1, 2,  3,  4],
#     [5, 6,  7,  8],
#     [9, 10, 11, 12]
# ]

# print(list_2d[1][2])

students = [
    ['Nika', 'Tamari', 'Levani', 'Giorgi', 'Luka'],
    ['t', 'n', 'c', 's', 'd']
]

students = [
    ['luka', 'tavkhelidze'],
    ['Nika', 'Gvaramia'],
    ['Nmae', 'Last Name'],
    ['luka', 'tavkhelidze'],
    ['luka', 'tavkhelidze'],

]
students[0] # names
students[1] # last names

print('----------------------------')

# გაარკვიეთ რა ტიპის მონაცემებია ლისტში
for i in range(len(student_names)):
    print(student_names[i], student_last_names[i])

student_names.append('Paolo')
student_last_names.append('Rodrigez')

# print(student_names, student_last_names)
# print(len(student_names))
# print(student_names[len(student_names) - 1])
print(student_names[-1])

student_names.pop()
student_last_names.pop()
print(student_names, student_last_names)

student_last_names[3] = 'Kirkitadze'

# student_names.pop(0)
# student_last_names.pop(0)
# del student_names[0], student_last_names[0]
# del student_last_names[0]

# print(student_names, student_last_names)

# print(student_names[:-2])

# print(student_last_names[:-1])


# my_numbers = []

# for i in range(10):
#     my_numbers.append(i)

# list comprehension / generator
my_numbers = [i * 2 for i in range(10)]
# my_numbers.append(5)
print('my numbers:', my_numbers)
# is_even = True

# for i in range(len(my_numbers)):
#     if my_numbers[i] % 2 != 0:
#         print('ara')
#         # is_even = False
#         break
# else:
#     print('ki')

# for number in my_numbers:
#     if number % 2 != 0:
#         print('ara')
#         break
# else:
#     print('ki')

# if is_even:
#     print('ki')
# else:
#     print('ara')

a = [i - 1 for i in range(10)]
print('a: ', a)

# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i])

for index, element in enumerate(a):
    print(index, element)
