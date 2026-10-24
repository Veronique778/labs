
# №1

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def info(self):
#         print("Розміри:", self.width, "x", self.height)
#         print("Площа:", self.area())
#         print("Периметр:", self.perimeter())

# r1 = Rectangle(5, 3)
# r2 = Rectangle(10, 4)

# r1.info()
# r2.info()


# №2

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             print("Оцінка повинна бути від 1 до 12.")

#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def __str__(self):
#         return (
#             f"{self.name}: {self.grades}, "
#             f"середній = {round(self.average(), 2)}"
#         )


# student = Student("Plyushch Veronica")

# print("Середній без оцінок:", student.average())

# student.add_grade(12)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(12)

# print(student)


# №3

# student1 = Student("Koroliuk Illya")
# student2 = Student("Panechko Sophie")
# student3 = Student("Ostapenko Mariana")
# student4 = Student("Kobets Artem")
# student5 = Student("Glazko Alexandr")

# for grade in [12, 10, 11]:
#     student1.add_grade(grade)

# for grade in [11, 9, 10]:
#     student2.add_grade(grade)

# for grade in [12, 11, 12]:
#     student3.add_grade(grade)

# for grade in [2, 3, 1]:
#     student4.add_grade(grade)

# for grade in [11, 11, 11]:
#     student5.add_grade(grade)

# students = [student1, student2, student3, student4, student5]

# for student in students:
#     print(student)

# best_student = students[0]

# for student in students:
#     if student.average() > best_student.average():
#         best_student = student

# print("Учні з найвищим середнім балом:")

# for student in students:
#     if student.average() == best_student.average():
#         print(student.name, "—", round(student.average(), 2))

# №4

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Помилка: сума поповнення повинна бути додатною.")
#         else:
#             self.balance += amount
#             print("Поповнення:", amount)

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Помилка: сума списання повинна бути додатною.")
#         elif amount > self.balance:
#             print("Помилка: недостатньо коштів.")
#         else:
#             self.balance -= amount
#             print("Списання:", amount)

#     def info(self):
#         print(self.owner, "— баланс:", self.balance)


# account1 = BankAccount("Іван", 1000)
# account2 = BankAccount("Ольга", 700)

# print("\nРахунок Івана:")
# account1.info()
# account1.deposit(500)
# account1.withdraw(300)
# account1.withdraw(2000)
# account1.deposit(0)
# account1.deposit(-100)
# account1.withdraw(0)
# account1.withdraw(-50)

# print("\nРахунок Ольги:")
# account2.info()
# account2.deposit(100)
# account2.withdraw(200)
# account2.withdraw(1000)
# account2.deposit(0)
# account2.deposit(-200)
# account2.withdraw(0)
# account2.withdraw(-100)

# print("\nКінцевий стан рахунків:")
# account1.info()
# account2.info()