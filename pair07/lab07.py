#№1
#  with open("text.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# lines = text.splitlines()
# words = text.split()
# def longest_line(lines):
#     return max(lines, key=len)
# def line_index(lines):
#     return lines.index(longest_line(lines)) + 1

# print(len(lines))
# print(len(words))
# print(len(text))
# print(longest_line(lines))
# print(line_index(lines))
# print(len(longest_line(lines)))

#№2
# fragment = input("Введіть фрагмент тексту: ").lower()
# found = False
# with open("text.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# lines = text.splitlines()
# for number, line in enumerate(lines, start=1):
#     if fragment in line.lower():
#         print(f'№ of the line: {number}')
#         found = True
#         print(line)
# if not found:
#     print("No coincidences")

#№3

# with open("students.txt", "r", encoding="utf-8") as file:
#     lines = file.read().splitlines()

# students = []

# for line in lines:
#     parts = line.split(";")
#     score = int(parts[1])
#     if score > 80:
#         students.append([parts[0], score])

# students.sort(key=lambda student: student[1], reverse=True)

# with open("result.txt", "w", encoding="utf-8") as file:
#     for student in students:
#         file.write(student[0] + ";" + str(student[1]) + "\n")

#№4


# with open("grades.csv", "r", encoding="utf-8") as file:
#     lines = file.read().splitlines()

# grades = {}

# for line in lines:
#     name, subject, grade = line.split(";")
#     grade = int(grade)

#     if name not in grades:
#         grades[name] = []

#     grades[name].append(grade)

# results = []

# for name, marks in grades.items():
#     count = len(marks)
#     average = sum(marks) / count
#     results.append([name, count, average])

# results.sort(key=lambda student: student[2], reverse=True)

# best = results[0][2]

# with open("report.txt", "w", encoding="utf-8") as file:
#     for name, count, average in results:
#         file.write(f"{name} — оцінок: {count} — середній: {average:.2f}\n")

#     winners = [name for name, count, average in results if average == best]
#     file.write(f"Найкращий результат: {' та '.join(winners)} — {best:.2f}")
