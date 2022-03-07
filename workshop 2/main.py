# name: str = "luka"


# print(name)

"""
    int
    str
    bool
    float
"""


# arithmetic operators

x: int = 2
y: int = 4

# experssion = str(x) + ' + ' + str(y) + ' = ' + str(x + y) # '4' + ' + ' + '4' + ' = ' + '8' => '4 + 4 = 8'
# print(x, '+', y, '=', x + y)
# print(experssion)
# print(f'{x + y = }')
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} / {y} = {x / y}')
print(f'{x} * {y} = {x * y}')


# ნაშთის ოპერატორი ( modulus )
print(f'{x} % {y} = {x % y}')


# Floor division
print(f'{x} // {y} = {x // y}')

print(f'{x} ** {y} = {x ** y}')



# comparison operators
print('~~~~~~~~~~~~~ Comparison Operators ~~~~~~~~~~~~~~~~')
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print('~~~~~~~~~~~~~ Assignment Operators ~~~~~~~~~~~~~~~~')

# assignmet operators
x = 7

# x = x + 3
x += 3
print(x)

x -= 5
print(x)


x /= 2
print(x)


x %= 2
print(x)


print('~~~~~~~~~~~~~ Conditionals ~~~~~~~~~~~~~~~~')

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(type(age), type(name))
# if age < 0 or age > 150:
#     print('Please provide correct age!')
#     quit()

# if age > 0 and age < 150:
#     if age >= 18:
#         print(f'{name} is adult, {age} years old!')
#     else:
#         print(f'{name} is underage, {age} years old!')
# else:
#     print('Please provide correct age!')

# worst, best case
# if age > 100:
#     print('Free entrance, Free drinks')
# elif 50 <= age < 55: # 50 <= age and age < 55
#     print('Free entrance')
#     if name == "niko":
#         print('VIP Status')
# elif age < 21:
#     print('You cannot enter!')
# else:
#     print('pay 25 usd')


print('~~~~~~~~~~~~~ Loops ~~~~~~~~~~~~~~~~')
age = int(input('Enter your age: '))

# for i in range(10):
#     print(i)

# ASCII encoding
# A - 65
# Z - 91
# a - 97
# z - 122
# print(ord('A'))
# print(ord('0')) # 48
# print(ord('9')) # 57


# for character in age:
#     # print(character)
#     # if ord('A') <= ord(character) <= ord('Z') or ord('a') <= ord(character) <= ord('z'):
#     #     print('characters are involved!', character)

#     if ord('0') > ord(character) or ord(character) > ord('9'):
#         break
# else:
#     print('everything is')
    
print('~~~~~~~~~~~~~ While ~~~~~~~~~~~~~~~~')

# x = 0

# while x < 5:
#     print(x)
#     x -= 1
#     if x <= -1000:
#         break


x = 0



while x < 10:
    x += 1
    if x % 2 == 1:
        continue

    print(x)

