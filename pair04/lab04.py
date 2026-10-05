#№1

#  numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# positive = []
# negative = []
# even = []
# multiples = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)
#     if number < 0:
#         negative.append(number)
#     if number % 2 == 0:
#         even.append(number)
#     if number % 3 == 0:
#         multiples.append(number)

# print(positive)
# print(negative)
# print(even)
# print(multiples)
# print(min(numbers), max(numbers), sum(numbers), round(sum(numbers) / len(numbers), 2))

#№2

# group1 = {'Anna', 'Ivan', 'Olha'}
# group2 = {'Ivan', 'Maksym', 'Olha'}

# joint = group1 | group2
# intersection = group1 & group2
# only_group1 = group1 - group2
# only_group2 = group2 - group1

# print("Спільні:", ", ".join(intersection))
# print("Тільки group1:", ", ".join(only_group1))
# print("Тільки group2:", ", ".join(only_group2))
# print("Усі:", ", ".join(joint))



# №3
# prices = {
#     "milk": 20,
#     "bread": 15,
#     "eggs": 30,
#     "chocolate": 120,
#     "mango": 150
# }

# name = input("Enter product name: ")
# price = int(input("Enter product price: "))
# prices[name] = price

# name = input("Enter product name to search: ")
# price = prices.get(name)

# if price is not None:
#     print("Price:", price)
# else:
#     print("Product not found")

# min_price = float(input("min: "))
# max_price = float(input("max: "))

# print("Products in diapazon:")

# for name, price in prices.items():
#     if min_price <= price <= max_price:
#         print(name, "-", price)



# №4

# students = {
#     'Ivan': [10, 11, 12, 9, 10],
#     'Anna': [8, 9, 10, 11, 9]
# }

# group = ('10-IT', '2026\\2027')

# best_name = ""
# best_grade = 0

# print(f"Group: {group[0]}, {group[1]}")

# print("Group book:")
# for name, marks in students.items():
#     print(f"{name}: {marks}")

# name = input("Enter the name of the new student: ")
# marks = input("Enter 5 grades separated by comma: ")

# grades = []

# for mark in marks.split(','):
#     grades.append(int(mark.strip()))

# correct = True

# if len(grades) != 5:
#     correct = False
# else:
#     for mark in grades:
#         if mark < 1 or mark > 12:
#             correct = False
#             break

# if correct:
#     students[name] = grades

#     print(f"Student {name} added")

#     print("Updated group book:")
#     for name, marks in students.items():
#         print(f"{name}: {marks}")

#     print("Average grades:")
#     rating = []

#     for name, marks in students.items():
#         average = sum(marks) / len(marks)

#         print(f"{name}: {average}")

#         rating.append((average, name))

#         if average > best_grade:
#             best_grade = average
#             best_name = name

#     rating.sort(reverse=True)

#     print("Rating:")
#     for average, name in rating:
#         print(f"{name}: {average}")

#     print("The best student is:", best_name, best_grade)

# else:
#     print("Error")