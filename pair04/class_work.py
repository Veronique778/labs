# # list  - список впоряддкована змінна колекція
# grades = [10, 8, 9]
# numbers = []
# numbers_new = list()

# grades[1] = 12
# print(grades)
# numbers.append(10) # додовання одного елементу
# numbers.append([11, 4]) # додовання одного елементу - списку
# numbers.insert(1, [5, 6]) # додовання елементу за індексом
# numbers.extend([7, 8, 9, 7]) # додовання декількол елементів
# numbers.remove(7) # видалення елементу за значенням
# numbers.pop(1) # видалення елементу за індексом
# del numbers[1] # видалення елементу за індексом, може видалити весь список
# numbers.clear() # очищення списку
# print(numbers.count(7))  # рахує кількість елементів 
# print(numbers.index(7)) # повертає індекс елементів 

# print(8 in numbers) # перевірка на наявність



# # len()
# # min()
# # max()
# # sum()

# print(min("a", "b"))







# print(numbers)



# numbers = [1, 4, 6, 8, 3]
# numbers.sort(reverse=True)
# print(numbers)
# new_numbers = sorted(numbers)
# new_numbers.reverse()
# print(new_numbers)

# for number in numbers:
#     print(number)


# numbers = [1, -9, 5, -4, 34, 5, 0, -3]
# positive = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)
# print(positive)




#tuple - кортеж - не змінювана колекція
# point = (-10, 12)
# rgb = (255, 0, 0)
# data = ()
# student = ("Veronika", "Plushch")
# print(student)
# a = (10,)
# point = point + (30,)

# # print(point + a)
# point =  point[:1] + point[2:]
# print(point)
# point = (-12, 6)
# x, y = point
# print(x)
# print(y)


# set - множини
# subjects = {"Python", "HTML", "CSS", "JavaScript"}
# data = {}
# print(type(data))
# subjects.add("C++")
# subjects.update(["Java", "Python"])
# subjects.remove("Java")
# subjects.discard("C#")
# print(subjects)
# # pop, clear теж тут працюють
# if "Python"in subjects:
#     print("Python")

# name = ["Veronika", "Oleg", "Olha", "Ivan", "Maria", "Maria"]
# unique_name = set(name)
# print(unique_name)

# group1 = {"Veronika", "Oleg", "Olha"}
# group2 = {"Ivan", "Maria", "Ann"}

# group3 = group1 & group2 # перетин
# print(group3)
# group4 = group1 | group2 # об'єднання
# group5 = group1 - group2 # різниця




#dict - словник
# student = {
#     "name": "Veronika",
#     "grade": 12
# }

# student2 = {}
# student3 =dict()
# print(student['name'])
# student["age"] = 18
# student["age"] = 19
# print(student)
# student_update = student.pop('age')
# print(student_update)
# popitem =student.popitem()


# student = {
#     "name": "Veronika",
#     "grade": 12
# }

# print(student.get('age', "Age not found"))
# if "grade" in student:
#     print(student.get("grade"))
# if "Ivan" in student.values():
#     print(student.get("name"))
# if "Ivan" in student.keys():
#     print(student.get("name"))
# print(student.items())

# for key, value in student.items():
#     print(key, value)


# prices = {
#     'apple': 45,
#     'banana':70,
#     'kiwi': 70,
#     'mango': 150,
#     'orange':100
# }

# print("All items:")
# for name, price in prices.items():
#     print(f"{name}: {prices}uah")

# print("from 50 to 100 uah")
# for name, prices