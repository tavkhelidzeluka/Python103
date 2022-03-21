import math

# OOP - Object Oriented Programming

class Dog:

    # static attributes
    breed = 'German Shepherd'

    def __init__(self, name: str, age: int) -> None:
        # constructor
        self.name = name
        self.age = age
    
    # functions in classes are called methods
    def bark(self):
        print(f'wof wof, my name is: {self.name}')



a = Dog('Lucky', 5) # instance <-> object
b = Dog('Doggo', 7)

Dog.breed = 'Chihuahua'
print(Dog.breed)
# a.breed = 'Chihuahua1'
# print(a.breed)

# b.breed = 'Chihuahua2'
# print(b.breed)
# print(Dog.breed)


# print(a.breed)
# print(b.breed)
# print(Dog.breed)


# print(a.name, a.age)
# print(b.name, b.age)
# a.bark()
# b.bark()


class Person:
    count: int = 0
    # Private Static Attribute
    __i_am_a_static_attribute = 0.5

    def __init__(self, name: str, last_name: str, age: int) -> None:
        # dunder method

        # public visibility
        self.name = name
        self.last_name = last_name

        # private attribute
        self.__age = age

        self.is_adult = age > 18
        Person.count += 1

    def __del__(self):
        Person.count -= 1
        print(self.name, 'Went away')
    
    def grow(self):
        self.__age += 1
        self.is_adult = self.__age > 18
    
    def get_age(self):
        return self.__age
    
    def show_details(self):
        print(self.name + self.last_name, self.__age, self.is_adult)



# student_1 = Person('Niko', 'Muskhelishvili', 21)
# student_2 = Person('George', 'Washington', 24)
# student_3 = Person('Ilia', 'Washington', 24)
# student_4 = Person('Ilia', 'VV', 18)

# student_4.show_details()
# # student_4.name = 25
# print(Person.count)
# del student_3
# print(Person.count)

# # student_4.age += 1
# # student_4.is_adult = student_4.age > 18
# student_4.grow()


# # print(student_1.name, student_1.last_name, student_1.age, student_1.is_adult)
# # print(student_2.name, student_2.last_name, student_2.age, student_2.is_adult)
# # student_1.show_details()
# # student_2.show_details()
# # student_3.show_details()
# student_4.show_details()


# students: list[Person] = [
#     Person('Niko', 'Muskhelishvili', 21),
#     Person('George', 'Washington', 24),
#     Person('Ilia', 'Washington', 24),
#     Person('Ilia', 'VV', 18)
# ]

# print('-' * 10)
# [i.show_details() for i in students]
# for i in students: 
#     i.show_details()


# print([i % 2 == 0 for i in range(10)])
# print([i for i in range(10) if i % 2 == 0])

from abc import ABC, abstractmethod


class Shape(ABC):
    # def __init__(self, area: float) -> None:
    #     self.area = area

    @abstractmethod
    def get_area(self):
        # print('shemovedi shape is get areashi')
        pass

    @staticmethod
    def tell_joke():
        print('hahaahhaha')
    


class Rectangle(Shape):
    def __init__(self, a: float, b: float) -> None:
        # super().__init__(a * b)
        self.a = a
        self.b = b
    
    def get_area(self):
        print(self.a * self.b)

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def get_area(self):
        print(math.pi * (self.radius ** 2))


class Square(Rectangle):
    def __init__(self, a: float, b: float) -> None:
        if a != b:
            raise Exception('Square sides must be equal!')
        super().__init__(a, b)


square_1 = Square(2, 2)

# print(square_1.area)

circle = Circle(5)
# print(circle.area)


shapes: list[Shape] = [
    Square(2, 2),
    Rectangle(2, 4),
    Circle(1.2)
]

for shape in shapes:
    shape.get_area()

Shape.tell_joke()
Square.tell_joke()
shapes[0].tell_joke()
# Shape()