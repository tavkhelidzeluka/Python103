import csv
import json


def jami(*args, **kwargs) -> float:
    print('args = ', args, 'kwargs = ', kwargs)
    s = 0
    for i in args:
        s += i
    return s


def substraction(x, y = 5, *args):
    return x - y

# void
def multiplication(x, y) -> None:
    print(x * y)




# substraction(17, 2)
# print(jami(5, 6))
# print(jami(2, 36))
# print(jami(123, 123))
# print(jami(234, 24))
# print(jami(23, 34))
# print(jami(5, 62))

# print(multiplication(2, 9))

# # print(jami(jami(jami(2, 1), 7), 5))

# print(jami(1, 2, 1, 1))

# # print(substraction(25, 6,True, "gela", 27, 19.1))
# print(substraction(5, y=5))

# jami(5, 6, neli=2, mari='niko')


# my_file = open('./workshop 5/info.txt')

# # print(my_file.read())
# # print(my_file.readline(), end='')
# for gela in my_file.readlines():
#     print(gela)

# # print('~~~~~~~~~~~~~~~~~~~~~~')
# # my_file.seek(0)
# # print(my_file.read(), end='')

# my_file.close()


# modes: r, a, w
# numbers_file = open('./workshop 5/info.txt', 'a+')
# numbers_file.seek(0)
# k = jami( *[int(number) for number in numbers_file.readlines()] )
# print(k)
# numbers_file.write(f'Sum: {k}')

# if not numbers_file.closed:
#     numbers_file.close()
numbers = []
with open('./workshop 5/info.txt', 'r') as f:
    # f.seek(0)
    # k = jami( *[int(number) for number in f.readlines()] )
    # print(k)
    # f.write(f'Sum: {k}')

    numbers = [number for number in f.readlines() if int(number) != 3]

    # for number in numbers:
    #     f.write(f'{number}\n')

    # f.readline()
    # f.readline()

    # print(f.readline())

# with open('./workshop 5/info.txt', 'w') as f:
#     f.writelines(numbers)

# with open('workshop 5\\betfair_data.csv') as f:
#     data = csv.reader(f, delimiter=',')

#     count = 0
#     for row in data:
#         print(row)
#         count += 1
#     print(count)

# from pprint import pprint 
# data = json.load(open('workshop 5\\Other 2019-2020 Data.json'))
# pprint(data)