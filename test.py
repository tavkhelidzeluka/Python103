"""
შექმენით 10 ელემენტიანი ლისტი და შეავსეთ 
კლავიატურიდან შეტანილი მთელი რიცხვებით.
 შემდეგ თითოეული ელემენტი ლისტში აიყვანეთ
  მომდევნო ინდექსზე მდგომი ელემენტის ხარისხში 
  (ბოლო ინდექსზე მდგომი ელემენტი აიყვანეთ პირველი ელემენტის ხარისხში)
"""

from random import randint

numbers = [randint(2, 2) for _ in range(10)]
b = numbers[0]
for i, number in enumerate(numbers[:-1]):
    numbers[i] **= numbers[i + 1]

numbers[-1] **= b
print(numbers)


# numbers: list[int] = []

# for _ in range(5):
#     numbers.append(int(input('Enter Number: ')))

# for i, number in enumerate(numbers):
#     numbers[i] = number ** 2
#     print(numbers[i])
