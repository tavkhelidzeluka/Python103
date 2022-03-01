# Data Manipulation

- [Operators](#operators)
- [Data Structures](#data-structures)
    - [Lists](#lists)
    - [Tuples](#tuples)
    - [Dctionaries](#dictionaries)
    - [Sets](#sets)
    - [Built-in functions](#built-ins)
- [Loops](#loops)
    - [for loop](#for-loop)
    - [while loop](#while-loop)
    - [continue](#continue)
    - [break](#break)
    - [for else](#for-else)
- [Chained Conditionals](#chained-conditionals)
- [Nesting](#nesting)



### Operators
```python
"""
    პითონში გვაქვს რამდენიმე ოპერატორების ჯგუფი:
    - Arithmetic operators (არითმეტიკული)
    - Assignment operators (მინიჭების)
    - Comparison operators (შედარების)
    - Logical operators (ლოგიკური)
    - Identity operators (საიდენტიფიკაციო)
    - Membership operators (წევრობის)
    - Bitwise operators (ბიტური)
"""
```
[დეტალები](https://www.w3schools.com/python/python_operators.asp)


### Data structures
```python
"""
    მონაცემთა სტრუქტურები - list, tuple, dict, set
    მათი დანიშნულებაა ობიექტების გაერთიანება, როდესაც ბევრი
    მსგავსი ცვლადი გვჭირდება.

    როდესაც ბევრი ცვლადი გვჭირდება სათითაოდ არ ვქმნით მათ
    და ვიყენებთ ე.წ. მონაცემთა სტრუქტურა, მათ შორის ძირითად 
    განსხვავება მოქნილობა და სისწრაფეა

    str - არის თუ არა მონაცემთა სტრუქტურა?
"""
```

#### Lists
*სხვა ენებში შეგხვდებათ array (მასივის) სახელით*
[დეტალები](https://www.w3schools.com/python/python_lists.asp)

#### Tuples
[დეტალები](https://www.w3schools.com/python/python_tuples.asp)


#### Dictionaries
[დეტალები](https://www.w3schools.com/python/python_dictionaries.asp)

*სხვა ენებში შეიძლება შეგხვდეთ map -ის სახელით, javaScript - ში object-ის სახელითაა ცნობილი*

#### Sets
[დეტალები](https://www.w3schools.com/python/python_sets.asp)


#### Built-ins

```python

# len ფუნქცია იღებს iterable-ს პარმეტრად და გვიბრუნებს
# მის ზომას
print(len([1, 2, 3, 4]))

# range იღებს 2 პარამეტრს ან 1-ს
# 2 პარამეტრი - range(საიდან, სადამდე)
# 1 პარამეტრი - range(სადამდე)
print(range(4, 10))
print(range(5))
```

### Loops
ციკლები გვეხმარება, რომ მანიპულაცია მოვახდინოთ
iterable-ში არსებულ მონაცემებზე

არსებობს ორი ტიპის ციკლი
for და while

#### For Loop
სინტაქსი

```python
for number in [1, 2, 3, 4]:
    print(number)

# output:
"""
1
2
3
4
"""
```

#### While Loop

სინტაქსი

```python
"""
მანამ სანამ (პირობა ჭეშმარიტია):
    შეასრულე აქ არსებული კოდი
"""

i: int = 0
while i < 5:
    print(i)
    i += 1

# output:
"""
1
2
3
4
"""
```

#### Continue
skip iteration (იტერაციის გამოტოვება)
```python
for i in range(5):
    if i % 2 != 0:
        continue

    print(i)
```

#### Break
ციკლიდან გამოსვლა 

```python
for i in range(5000):
    if i % 8 == 0:
        break

    print(i)
```

#### For Else
for ციკლის შემდეგ else შესრულება მხოლოდ იმ შემთხვევაში, თუ ციკლი არ გაჩერდა და ყველა იტერაცია ბოლომდე გაიარა

```python
for i in range(15):
    if i % 16 == 0:
        print("Loop has been stopped!")
        break
else:
    print("Loop didn't stop!")

```


### Chained Conditionals

```python

age = 20
if age > 50:
    print("elder")
if age > 30:
    print("adult")
if age > 18:
    print("young adult")
else:
    print("young")

"""
    მინიმუმ რამდენი შემოწმება მოხდება? (best case)
    და მაქსიმუმ რამდენი შემოწმება მოხდება? (worst case)
"""

"""
    Chained Conditionals

    თუ (პირობა 1):
        პირობა 1 შესრულდა შემოდი აქ
    თუ არა და (პირობა 2):
        პირობა 2 შესრულდა შემოდი აქ
    თუ არა და (პირობა 3):
        პირობა 3 შესრულდა შემოდი აქ
    ყველა დანარჩენი შემთხვევა:
        შემოდი აქ
"""

age = 20
if age > 50:
    print("elder")
elif age > 30:
    print("adult")
elif age > 18:
    print("young adult")
else:
    print("young")

"""
    მინიმუმ რამდენი შემოწმება მოხდება? (best case)
    და მაქსიმუმ რამდენი შემოწმება მოხდება? (worst case)
"""

"""
    ფრჩხილებში ჩასმულ ნაწილს (ფრჩხილები არაა აუცილებელი!)
    ეწოდება statement-ი (პირობა), თუ ის ჭეშმარიტია, მაშინ
    მისი evaluation -ი მოხდება და ან True იქნება ან False
"""

name = "nick"
age = 18


if (age == 18 and name == "nick"):
    print("do something")
elif age < 18 or name == "Erick":
    print("do something")


```

### Nesting
ყველფერი რაც ვისწავლეთ შეგვიძლია ერთმანეთში ჩავდგათ
ციკლები, შედარებები

```python
multi_dimensional_list = [
    [1, 2, 3, 4, 5]
    [6, 7, 8, 9, 10]
]
odd_found: bool = False

for inner_list in multi_dimensional_list:
    if odd_found:
        break
    for number in inner_list:
        if number % 2 == 1:
            odd_found = True
            break
else:
    print("list contains only even numbers!")
    
```
