#№1

# import math


# radius = float(input("Radius: "))
# catets = list(map(float, input("Enter two catets: ").split(",")))
# items = int(input("Number of items: "))
# pack = int(input("Items per pack: "))

# area = math.pi * radius ** 2
# hypotenuse = math.sqrt(catets[0] ** 2 + catets[1] ** 2)
# packs = math.ceil(items / pack)

# print("Circle area:", round(area, 2))
# print("Hypotenuse:", round(hypotenuse, 2))
# print("Required packs:", packs)

#№2


# import random
# import statistics

# n = int(input("Enter the number of grades: "))
# grades = []

# while n <= 0:
#     n = int(input("Enter a positive number: "))
# for _ in range(n):
#     grades.append(random.randint(1, 12))

# count = 0

# for grade in grades:
#     if grade >= 10:
#         count += 1

# print("Grades:", grades)
# print("Min:", min(grades))
# print("Max:", max(grades))
# print("Середнє:", round(statistics.mean(grades), 2))
# print("Медіана:", statistics.median(grades))
# print("Оцінок 10–12:", count)

#№3

from datetime import*

day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))

event = date(year, month, day)
today = date.today()

diff_ce = (event - today).days

if diff_ce > 0:
    print(f"your date is comming in {diff_ce} days")
if diff_ce < 0:
    print(f"your date was {abs(diff_ce)} day ago")
if diff_ce == 0:
    print("it`s today omg!!")