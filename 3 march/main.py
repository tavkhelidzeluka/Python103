# print( '1'.__len__() )



# a = [1, 2, 3]

'''
event_id,score
0,"0, 1"
1,"2, 1"
'''

# სად არის 2 მეტი score

numbers = [1, 2, 3, 4]

#                 0       1       2       3
# list_of_lists = [ [1, 2], [1, 2], [2, 2], [1, 3] ]

events = [ 
    [52, [0, 1]], 
    [1234, [2, 1]],
    # [23, [0, 4]],
    # [24, [1, 4]],
    # [27, [0, 0]],
    # [57, [0, 2]]
]

for event in events:
    scores = event[1]
    
    jami = 0
    for score in scores:
        jami += score
    
    print(jami > 2)
    # print(sum(scores) > 2)

# print(event_1)

#               0  1  2  3  4
# even_numbers = [2, 4, 6, 8, 10]

# # 0x12643 + 0


# # 0, 1, 2, 3, 4
# for index in range( len(even_numbers) ):

#     if even_numbers[0] % 4 == 0:
#         print(even_numbers[index])


# for number in even_numbers:
#     print(number)

gela = 2
# print(even_numbers[gela])
# gela += 1

# print(even_numbers[gela])
# gela += 1

# print(even_numbers[gela])

# while gela < len(even_numbers):
#     print(even_numbers[gela]) # 
#     gela += 1

boats = ['Flying Dutchman', 'Titanic', 'Marmaid', 'Victoria']



# for i in range(len(boats)):
#     print('-' * 10)
#     print(f'{boats[i]} - ნავი შევიდეს ყურეში')
#     print(f'შავი ნავი წავიდეს მარჯვნივ')
#     print(f'{boats[i]} - ნავი გამოვიდეს ყურედან')
#     print(f'შავი ნავი წავიდეს მარცხნივ')
#     print('-' * 10)
# for boat_name in boats:
#     print('-' * 10)
#     print(f'{boat_name} - ნავი შევიდეს ყურეში')
#     print(f'შავი ნავი წავიდეს მარჯვნივ')
#     print(f'{boat_name} - ნავი გამოვიდეს ყურედან')
#     print(f'შავი ნავი წავიდეს მარცხნივ')
#     print('-' * 10)

