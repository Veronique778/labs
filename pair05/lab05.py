# №1
# def rectangle_area(width, height):
#     return width * height

# def circle_area(radius):
#     return 3.14159 * (radius ** 2)

# def triangle(side, height):
#     return (side*height)/2

# chose = input("Оберіть круг, трикутник, прямокутник:")

# def main():
#     if chose == 'трикутник':
#         side = int(input('сторона:'))
#         height = int(input('висота:'))
#         print(triangle(side, height))

#     elif chose == 'круг':
#         radius = int(input('радіус:'))
#         print(circle_area(radius))

#     elif chose == 'прямокутник':
#         width = int(input('ширина:'))
#         height = int(input('висота:'))

#         print(rectangle_area(width, height))

#     else:
#         print('Pomilka')

# main()


# №2 


# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# def divisors(n):
#     result = []

#     for i in range(1, n + 1):
#         if n % i == 0:
#             result.append(i)

#     return result


# def digit_sum(n):
#     total = 0

#     while n > 0:
#         total += n % 10
#         n //= 10

#     return total


# def main():
#     n = int(input("Введіть число: "))

#     if is_prime(n):
#         print("так")
#     else:
#         print("ні")

#     print(divisors(n))
#     print(digit_sum(n))


# main()

# №3 


# def average(grades):
#     return sum(grades) / len(grades)


# def minimum(grades):
#     return min(grades)


# def maximum(grades):
#     return max(grades)


# def count_above(grades, value):
#     count = 0

#     for n in grades:
#         if n > value:
#             count += 1

#     return count


# def main():
#     grades = []

#     for i in range(5):
#         grades.append(float(input("Grade: ")))

#     value = float(input("Limit: "))

#     print("Average:", average(grades))
#     print("Minimum:", minimum(grades))
#     print("Maximum:", maximum(grades))
#     print("Above limit:", count_above(grades, value))


# main()

# № 4

# def len_password(password):
#     return len(password) >= 8


# def has_uppercase(password):
#     for char in password:
#         if char.isupper():
#             return True
#     return False


# def has_lowercase(password):
#     for char in password:
#         if char.islower():
#             return True
#     return False


# def has_digit(password):
#     for char in password:
#         if char.isdigit():
#             return True
#     return False


# def has_special_char(password):
#     for char in password:
#         if not char.isalnum():
#             return True
#     return False


# def validate_password(password):
#     errors = []

#     if not len_password(password):
#         errors.append("Password is too short")

#     if not has_uppercase(password):
#         errors.append("No uppercase letter")

#     if not has_lowercase(password):
#         errors.append("No lowercase letter")

#     if not has_digit(password):
#         errors.append("No digit")

#     if not has_special_char(password):
#         errors.append("No special character")

#     return errors


# def main():
#     password = input("Password: ")

#     errors = validate_password(password)

#     if len(errors) == 0:
#         print("Password is strong")
#     else:
#         print("Password does not meet requirements")
#         print("Not completed:", errors)


# main()
