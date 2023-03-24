#Functions - функции
# def calc():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1 + num2)

# def add(num1, num2): #num1, num2 параметры функции add
#     print(num1 + num2)
# add(10, 40) #Вызываем функцию add и передаем аргументы 10 и 40
# add(30, 30)
# add(50, 50)
# add(100, 10)

# def welcome():
#     name = input("Ваше имя: ")
#     print("Здраствуйте", name)
# welcome()
# calc()

# def input():
#     print("Input")

# name = input()
# print(name)

# def chet_nechet(lst:list) -> str:
#     for num in lst:
#         if num % 2 == 0:
#             print(num, "четный")
#         else:
#             print(num, "нечетный")
            
# numbers = [1, 3, 10, 1001, 400, 403, 102, 101, 607, 808, 888, 678, 109]
# chet_nechet(numbers)
# chet_nechet([10, 20, 30, 33, 44, 66])

# def add(num1:int, num2:int) -> int:
#     print(num1 + num2)

# def sub(num1:int, num2:int) -> int:
#     print(num1 - num2)

# def mult(num1:int, num2:int) -> int:
#     print(num1 * num2)

# def div(num1:int, num2:int) -> float:
#     print(num1 / num2)

# def main(number1:int, number2:int, operator:str) -> int:
#     if operator == "+":
#         add(number1, number2)
#     elif operator == "-":
#         sub(number1, number2)
#     elif operator == "*":
#         mult(number1, number2)
#     elif operator == "/":
#         div(number1, number2)
#     else:
#         print("Такого оператора не существует")
# main(10, 20, "+")
# main(30, 40, "*")
# main(30, 40, "/")
# main(30, 40, "-")
# main(30, 40, "-=fslkdfghsd")

# def get_name(name:str = "Defolt"):
#     """Hello World Geeks Students"""
#     print(name)
# get_name()
# print()

# def add(num1:int=1, num2:int=1) -> int:
#     return num1 + num2 
# print(add(20, 20))

# def hello():
#     while True:
#         print("Hello")
#         return "Hello"
# hello()

# while True:
#     try:
#         num1 = int(input("Первое число: "))
#         num2 = int(input("Второе число: "))
#         print(num1 / num2)
    # except ZeroDivisionError:
    #     print("Деление на ноль")
    # except ValueError:
    #     print("Пишите только цифры")
    # except Exception:
    #     print("Error")