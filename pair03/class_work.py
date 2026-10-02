# name = "Veronika"
# city = "Kuiv"
# message = "Hello world"

# print(len(message)) #лен повертає кількість символів у рядку 

# print(name[0])
# print(name[-1])
# print(message[len(message)-1])
# print(city[10])

# text = input()

# if len(text) > 0:
#     print(text[0])

# else:
#     print("empty string")

# print(text[:2])
# print(text[2:5])
# print(text[2:5])
# print([text[::2]])
# print(text[::-1])

# text[3] = '3'
# print(text)

# text = "hello world"
# text2 = text.upper()
# print(text2)
# print(text2.lower()) # lower() це метод рядка який повертає копію рядка де всі символи перетворені на нижній регістр
# print(text.upper())
# print(text.capitalize())
# print(text.title())

# text = "python programming"
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())
# login = 'admin'
# user_login = input("enter your login: ")
# if user_login.strip().lower() == login:
#     print("hello admin!")

# text = 'python'
# for char in text:
#     print(char)

# password = '123qwerty123'
# # print(password.isdigit())
# digits = 0
# for i in password:
#     if i.isdigit():
#         digits += 1
# print(digits)



# letters = 0
# for i in password:
#     if i.isdigit():
#         digits += 1
#     if i.isalpha():
#         letters += 1

# print(f"digits:{digits}, letters: {letters}")

# print(password.isalpha())
# print(password.isdigit())
# print(password.isalnum())


# text = input("enter the sentenses:")
# golosni = 'аеєиіїоуюя'
# counter_golosni = 0
# for i in text:
#     if i in golosni:
#         counter_golosni += 1
# print(counter_golosni)

# text = "привіт світ"
# words = text.split()
# print(words)

# text_new = ' '.join(words)
# print(text_new)

# text = 'python is easy to learn'
# new_text = text.replace("python", "javascript")
# print(new_text)

# word = "дід "
# word_norm = word.strip().lower()
# if word_norm == word_norm[::-1]:
#     print("паліндром")
# else:
#     print(" не поліндром ")

# text = "world"
# print(text.find("0"))
# print(text.count('l'))

# email = 'user@example.com'
# if email.lower().endswith('gmail.com'):
#     print(" you have gmail account")

