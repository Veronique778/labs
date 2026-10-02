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
