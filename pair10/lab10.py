# #№1

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return self.name


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"{self.name}, {self.group}"


# student1 = Student("Mariana", "IT-10")
# student2 = Student("Illya", "IT-10")

# print(student1.info())
# print(student2.info())

# N2

# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def info(self):
#         return f"{self.name}, {self.subject}"


# person = Person("Ivan")
# teacher = Teacher("Olena", "Python")

# people = [person, student1, student2, teacher]

# for person in people:
#     print(person.info())


# №3

# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         for current in self.students:
#             if current.name.lower() == student.name.lower():
#                 print("Exists")
#                 return

#         self.students.append(student)

#     def remove_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 self.students.remove(student)
#                 return True

#         return False

#     def show_students(self):
#         print(self.title)
#         print(self.teacher.info())

#         for student in self.students:
#             print(student.info())


# teacher = Teacher("Ivan", "Python")
# course = Course("Python", teacher)

# course.add_student(Student("Anna", "IT-10"))
# course.add_student(Student("Myhailo", "IT-10"))
# course.add_student(Student("Mariana", "IT-10"))
# course.add_student(Student("Sophie", "IT-10"))

# course.show_students()

# course.add_student(Student("Anna", "IT-10"))

# print(course.remove_student("Myhailo"))
# course.show_students()


# №4

# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#         self.grades = []

#     def info(self):
#         return f"{self.name}, {self.group}"

#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             print("Invalid grade")

#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)


# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         if self.find_student(student.name):
#             print("Exists")
#         else:
#             self.students.append(student)

#     def remove_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 self.students.remove(student)
#                 return True

#         return False

#     def show_students(self):
#         print(self.title)
#         print(self.teacher.info())

#         for student in self.students:
#             print(student.info())

#     def find_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 return student

#         return None

#     def add_grade_to_student(self, name, grade):
#         student = self.find_student(name)

#         if student:
#             student.add_grade(grade)
#         else:
#             print("Not found")

#     def show_rating(self):
#         rating = self.students.copy()
#         rating.sort(key=lambda student: student.average(), reverse=True)

#         for student in rating:
#             print(student.name, round(student.average(), 2))


# teacher = Teacher("Olena", "Python")
# course = Course("Python", teacher)

# try:
#     with open("course_data.txt", "r", encoding="utf-8") as file:
#         for line in file:
#             try:
#                 name, group, grades_text = line.strip().split(";")
#                 name = name.strip()
#                 group = group.strip()

#                 if not name or not group:
#                     raise ValueError

#                 student = Student(name, group)

#                 if grades_text:
#                     for grade in grades_text.split(","):
#                         grade = int(grade)

#                         if grade < 1 or grade > 12:
#                             raise ValueError

#                         student.add_grade(grade)

#                 course.add_student(student)

#             except ValueError:
#                 print("Invalid line")

# except FileNotFoundError:
#     print("No file")

# except UnicodeError:
#     course.students = []
#     print("Invalid encoding")

# except OSError:
#     print("File error")


# while True:
#     print("\n1 - Show")
#     print("2 - Add")
#     print("3 - Remove")
#     print("4 - Find")
#     print("5 - Grade")
#     print("6 - Rating")
#     print("7 - Save")
#     print("0 - Exit")

#     choice = input("> ").strip()

#     if choice == "1":
#         course.show_students()

#     elif choice == "2":
#         name = input("Name: ").strip()
#         group = input("Group: ").strip()

#         if not name or not group or ";" in name or ";" in group:
#             print("Invalid input")
#         else:
#             course.add_student(Student(name, group))

#     elif choice == "3":
#         name = input("Name: ").strip()

#         if course.remove_student(name):
#             print("Removed")
#         else:
#             print("Not found")

#     elif choice == "4":
#         name = input("Name: ").strip()
#         student = course.find_student(name)

#         if student:
#             print(student.info())
#             print(student.grades)
#             print(round(student.average(), 2))
#         else:
#             print("Not found")

#     elif choice == "5":
#         name = input("Name: ").strip()

#         try:
#             grade = int(input("Grade: "))
#             course.add_grade_to_student(name, grade)

#         except ValueError:
#             print("Invalid grade")

#     elif choice == "6":
#         course.show_rating()

#     elif choice == "7":
#         try:
#             with open("course_data.txt", "w", encoding="utf-8") as file:
#                 for student in course.students:
#                     grades = ",".join(str(grade) for grade in student.grades)
#                     print(f"{student.name};{student.group};{grades}", file=file)

#             print("Saved")

#         except OSError:
#             print("File error")

#     elif choice == "0":
#         break

#     else:
#         print("Invalid choice")