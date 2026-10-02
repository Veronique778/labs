#№1

# n = int(input("Enter a number:"))
# count = 0
# total = 0
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         count += 1
#         total += i


# if count > 0:
#     arf = total / count

        
#     print(round(arf, 2))
#     print(count)
#     print(total)



#№2
# n = int(input("Enter a number:"))
# count = 0
# suma = 0
# max_digit = 0
# min_digit = 9

# if n == 0:
#     count = 1
#     suma = 0
#     max_digit = 0
#     min_digit = 0
# else:
#     while n > 0:
#         digit = n % 10
#         count += 1
#         suma += digit

#         if digit < min_digit:
#             min_digit = digit

#         if digit > max_digit:
#             max_digit = digit

#         n //= 10



# №3
# n = int(input("Enter a number:"))

# for i in range(1, n + 1):
#     temp = i
#     good = True

#     while temp > 0:
#         digit = temp % 10

#         if digit != 0:
#             if i % digit != 0:
#                 good = False

#         temp //= 10

#     if good:
#         print(i)

# № 4

# width = int(input("Width: "))
# height = int(input("Height: "))
# border = input("Контур: ")
# inside = input("Всередині: ")

# if width < 3 or height < 3:
#     print("Помилка: мінімальний розмір — 3 x 3")
# else:
#     for row in range(height):
#         for col in range(width):

#             if row == 0 or row == height - 1 or col == 0 or col == width - 1:
#                 print(border, end='')
#             else:
#                 print(inside, end='')

#         print()
