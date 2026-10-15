# №1
# try:
#     a = int(input("Please enter first number: "))
#     b = int(input("Please enter second number: "))
# except ValueError:
#     print("Please enter valid numbers!")
# else:
#     operation = input("Choose action (+, -, *, /): ")

#     if operation == "+":
#         print(a + b)
#     elif operation == "-":
#         print(a - b)
#     elif operation == "*":
#         print(a * b)
#     elif operation == "/":
#         if b == 0:
#             print("I will divide you by zero!")
#         else:
#             print(a / b)
#     else:
#         print("Unknown operation")

# №2
# def input_grade():
#     while True:
#         try:
#             grade = int(input("Grade 1..12: "))
#             if grade < 1 or grade > 12:
#                 raise ValueError("False grade")
#             return grade
#         except ValueError as error:
#             print("Error:", error)
# grade = input_grade()
# print("Your grade:", grade)

# №3

# with open("students.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# students = []
# grades = {}

# for student in text.splitlines():
#     parts = student.split(";")

#     if len(parts) != 2:
#         print(student)
#         continue

#     name = parts[0].strip()

#     try:
#         grade = int(parts[1])
#     except ValueError:
#         print(student)
#         continue

#     students.append(name)
#     grades[name] = grade

# try:
#     choice = int(input("1 — пошук учня за індексом, 2 — оцінка за ім'ям: "))

#     if choice == 1:
#         index = int(input("індекс: "))
#         print("yчень:", students[index])

#     elif choice == 2:
#         name = input("ім'я: ")
#         print("Оцінка:", grades[name])

#     else:
#         print("error, incorect type")

# except IndexError:
#     print("Error, theres no one with this index")

# except KeyError:
#     print("Error there no one like it ih this list")

# except ValueError:
#     print("Error, invalid number")

# №4

# try:
#     with open("students.txt", encoding="utf-8") as file:
#         students = file.readlines()

#     valid = []
#     skipped = 0

#     for student in students:
#         parts = student.strip().split(";")

#         if len(parts) != 2 or not parts[0].strip():
#             skipped += 1
#             continue

#         try:
#             name, grade = parts[0].strip(), int(parts[1])

#             if 0 <= grade <= 100:
#                 valid.append((name, grade))
#             else:
#                 skipped += 1
#         except ValueError:
#             skipped += 1

#     valid.sort(key=lambda x: x[1], reverse=True)

#     with open("report.txt", "w", encoding="utf-8") as file:
#         for name, grade in valid:
#             file.write(f"{name};{grade}\n")

#     print("Valid:", len(valid), "Skipped:", skipped)

# except FileNotFoundError:
#     print("Error: students.txt not found")