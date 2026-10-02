# #№ 1

# text = input("Введіть довільний текст: ")

# all_vowels = "аеєиіїоуюяaeiou"
# latters = 0
# numbers = 0
# spaces = 0
# vowels = 0
# words = 0

# for char in text:
#     if char.lower() in all_vowels:
#         vowels += 1
#     if char.isdigit():
#         numbers += 1
#     if char.isalpha():
#         latters += 1
#     if char == " ":
#         spaces += 1

# print(len(text))
# print(latters)
# print(numbers)
# print(spaces)
# print(vowels)
# print(len(text.split()))



# #№ 2
# fio = input("Введіть: Прізвище, Ім'я, По-Батькові: ")
# parts = fio.split()

# if len(parts) == 3:
#     lastname = parts[0]
#     firstname = parts[1]
#     surname = parts[2]
#     print(f"{lastname.title()} {firstname[0].upper()}. {surname[0].upper()}.")
# else:
#     print("неправильний формат")


# #№ 3

# text1 = input("Перший рядок: ")
# text2 = input("Другий рядок: ")
# a = text1.lower().replace(" ", "")
# b = text2.lower().replace(" ", "")

# if sorted(a) == sorted(b):
#     print("Анаграми")
# else:
#     print("Не анаграми")

# #№ 4
# sentence = input("Речення: ")

# words = sentence.split()

# longest = words[0]
# shortest = words[0]

# unique_words = ""
# unique_count = 0

# for word in words:
#     if len(word) > len(longest):
#         longest = word
#     elif len(word) == len(longest):
#         longest += ", " + word

#     if len(word) < len(shortest):
#         shortest = word
#     elif len(word) == len(shortest):
#         shortest += ", " + word

#     word_lower = word.lower()

#     if "|" + word_lower + "|" not in unique_words:
#         unique_words += "|" + word_lower + "|"
#         unique_count += 1

# print("Найдовші:", longest)
# print("Найкоротші:", shortest)
# print("Унікальних слів:", unique_count)

# old_word = input("Слово для заміни: ")
# new_word = input("Нове слово: ")

# sentence = sentence.replace(old_word, new_word)

# print("Після заміни:", sentence)

# print("Найдовше слово:", longest)
# print("Найкоротші:", shortest)

