# book = {
#     'title': "Кобзар",
#     'author': "Тарас Шевченко",
#     'copies': 15

# }
# print(book)

# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
#     def available(self):
#         return self.copies > 0


# book1 = Book('Кобзар', 'Тарас Шевченко', 15)
# # book2 = Book()

# print(book1.title, book1.author, book1.copies)
# print(book1.available())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'Rectangle width: {self.width}, height: {self.height}')
#         print(f'Perimeter: {self.perimeter()}')
#         print(f'Area: {self.area()}')
# rectangle = Rectangle(10, 57)
# rectangle.info()
# print(area)
# print(area > 500)

# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1

# counter1 = Counter()
# counter2 = Counter()
# print(f'Was {counter1.value, counter2.value}')

# counter1.increment()
# counter2.increment()
# print(f'Became {counter1.value, counter2.value}')

# class Book:
#     def __init__(self, title, copies):
#         self.title = title
#         self.copies = copies
#     def give_one(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print(f'Видано книгу {self.title}')
#         else:
#             print(f'Немає доступних примірників {self.tittle}')
# book = Book('Кобзар', 3)
# book.give_one()
# book.give_one()
# print(f'Залишилось: {book.copies}')
        
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
        else:
            print('Grade must be between 1 and 12')

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def info(self):
        print(f'Name: {self.name}, Grades: {self.grades}')

    def __str__(self):
        return f'Student {self.name}, Grades: {self.grades}, Average: {self.average_grade():.2f}'



# student2 = Student("Ivan")
# # student1.grades.append(12)
# # student2.grades.append(1)
# student1.add_grade(12)
# student2.add_grade(13)
# student1.add_grade(10)


# students = [
#     Student('Anna', [1, 2, 3]),
#     Student('Ivan', [12, 10, 11])
# ]

# print(f'Students: {len(students)}')
# for student in students:
#     print(f'Student: {student.name}, Grades: {student.grades}')
#     print(student)

class Product:
    def __init__(self, name, price, count):
        self.name  = name
        self.price = price
        self.count = count
    def total_price(self):
        return self.price * self.count

mouse = Product("Mause", 1500, 10)
keyboard = Product('Keyboard')