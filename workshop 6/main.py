# 0, 1, 1, 2, 3, 5, 8, 13, 21


a1 = 0
a2 = 1
num = 0

for _ in range(3):
    num = a1 + a2
    a1 = a2
    a2 = num

# print(num)

# def fib(pos: int, num_1=0, num_2=1):
#     if pos - 2 != 0:
#         return fib(pos - 1, num_1=num_2, num_2=num_1 + num_2)
#     return num_2

# n = 5
def fib(n: int):
    if n == 1:
        return 0

    if n == 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)


print(fib(5))