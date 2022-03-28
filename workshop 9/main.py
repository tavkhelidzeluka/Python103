from random import randint


sample_list = ({}, {}, {})

# print(any(sample_list))

# Truthy | Falsy
# print(bool(None))
# print(bool([]))
# print(bool({}))
# print(bool(tuple()))
# print(bool(set()))
# print(-1, bool(-1))
# print(1, bool(1))
# print(0, bool(0))
# print(bool(''))
# print(bool(' '))


# class Post:
#     __instances: list['Post'] = []

#     def __init__(self) -> None:
#         Post.__instances.append(self)

#     @staticmethod
#     def all():
#         return Post.__instances

# print(type(Post))

# [Post() for _ in range(10)]

# for Post in Post.all():
#     print(Post)


# print(type(Post))
for dict in sample_list:
    if not len(dict):
        print('Empty!')
        break
else:
    print('Not empty!')

# a = [[randint(10000, 1000000) for i in range(100)] for _ in range(100000000)]

# class Range:
#     def __init__(self, n: int) -> None:
#         self.n = n
#         self.last = 0


#     def __next__(self):
#         if self.last == self.n:
#             raise StopIteration()
#         curr = self.last
#         self.last += 1
#         return curr

def Range(n: int):
    i = 0
    while i < n:
        yield i
        i += 1
        print('Shemovedi aqet')

# n = Range(100)

# while True:
#     try:
#         cur = next(n)
#         print(cur)
#     except StopIteration:
#         break

# l = list(i for i in Range(10))
# print(l)
# for i in Range(10):
#     print(i)
import random
nums = [i for i in range(1, 10000000)]
random.shuffle(nums)
target = 900000

found = False
print('gadavedi amoxsnaze')
# c = 0
# for i in range(len(nums)): 
#     for j in range(i, len(nums)):
#         c += 1
#         if nums[i] + nums[j] == target:
#             print([i],"---",[j])
#             found = True
#             break
    
#     if found:
#         break
# print(c)

# # ~ O (n ^ 2)

# for i, num_1 in enumerate(nums):
#     for j, num_2 in enumerate(nums[i:]):
#         if num_1 + num_2 == target:
#             print(i, "---", j + i)

# i, j = 0, len(nums) - 1
# nums.sort()

# while i < j:
#     if nums[j] > 9:
#         j -= 1
#         continue
#     if nums[i] + nums[j] == target:
#         print(i, "---", j)
#         break
    
#     elif nums[i] + nums[j] > target:
#         j -= 1
#     else:
#         i += 1

c = 0
l = [(i, e) for i, e in enumerate(nums)]
l.sort(key=lambda x: x[1]) 

pivot = len(l) // 2

while True:
    c += 1
    val = l[pivot][1]
    if val > target:
        l = l[:pivot]
        pivot = len(l) // 2
    elif val == target:
        l = l[:pivot + 1]
        break
    else:
        break


# print(l)
i = 0
j = len(l) - 1 

while i <= j:
    c += 1
    num1 = l[i][1]
    num2 = l[j][1]
    s = num1 + num2

    if s > target:
        j -= 1
    elif s < target:
        i += 1
    else:
        print(l[i], l[j])
        # print(l[i][0], l[j][0])
        break
else:
    print('No numbers found!')

print(c)