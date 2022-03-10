import random


print('-' * 10 + ' Functions ' + '-' * 10)

# counter = 25

# declaration
def count(list_of_numbers: list[int]) -> int:
    # global counter
    # Local Scope

    # print(numbers_1)
    print(list_of_numbers)
    counter = 0
    for i in list_of_numbers:
        if i == 5:
            counter += 1

    return counter

numbers_1 = [random.randint(0, 5) for _ in range(10)] # 1, 2, 3, 4
numbers_2 = [random.randint(0, 5) for _ in range(10)] # 2, 5, 5, 1

# call
print(count(numbers_1))

# call
print(count(numbers_2)) 


# default
def jami(a: float, b: float = 4) -> float:
    return a + b


print(jami(5, 6))
print(jami(1))