#Lambda фунции
# def mult_two(number:int) -> int:
#     return number * number
# print(mult_two(10))

# lambda_mult_two = lambda number: number * number
# print(lambda_mult_two(10))

# print((lambda number: number * number)(10))

################################

# def add(num1:int=10, num2:int=10) -> int:
#     return num1 + num2
# print(add(5))

# lambda_add = lambda num1=10, num2=10: num1 + num2 
# print(lambda_add(30, 30))
# print(lambda_add())

# print((lambda num1, num2: num1 + num2)(30, 30))

#########################################

# numbers = [10, 20, 30, 40, 50]
# new_numbers = []
# def mult_two_list(nums:list) -> list:
#     for n in nums:
#         new_numbers.append(n * 2)
#     return new_numbers
# print(mult_two_list(numbers))

# numbers = [10, 20, 30, 40, 50]
# lambda_new_numbers = list(map(lambda nums: nums * 2, numbers))
# print(lambda_new_numbers)

# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda nums: nums * 2, numbers)))

# print(list(map(lambda nums: nums * 2, [10, 20, 30, 40, 50])))

############################################

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# chet = []
# def chet_numbers(numbers:list) -> list:
#     for n in numbers:
#         if n % 2 == 0:
#             chet.append(n)
#     return chet
# print(chet_numbers(nums))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lambda_filter_nums = list(filter(lambda numbers: numbers % 2 == 0, nums))
# print(lambda_filter_nums)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda nums: nums % 2 == 0, nums)))

# print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

#Args, Kwargs
# print("Hello", "World", "Geeks", "Python")
# print("Hello World")

# def welcome(*name:str):
#     # print(name)
#     for n in name:
#         print("Здраствуйте", n)
# welcome("Kurmanbek", "Anton", "Anna", "Nurbolot")

# def student_mean_point(name:str, *points:int) -> str:
#     print(name, round(sum(points) / len(points)))
# student_mean_point("Nurbolot", 4, 4, 5, 3, 2, 3, 4, 5)
# student_mean_point("Urmat", 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 3)

# def translate(**words):
#     print(words)
# translate(Apple = "Яблоко", Phone = "Телефон", Car = "Машина")

# def short_word(word:str) -> str:
#     split_word = word.split()
#     res = ""
#     for i in split_word:
#         res += i[0].upper()
#     return res
# print(short_word("Кыргызская Республика"))
# print(short_word("Geeks studio python"))
# print(short_word("Ruby on Rails"))
# print(short_word("For your interest"))
# print(short_word("Geeks Python Studio Hello World"))
# short_word("Geeks studio python")

# def izogramma(word:str) -> bool:
    # if len(word) == len(set(word)):
    #     return True 
    # else:
    #     return False
    # return True if len(word) == len(set(word)) else False
# print(izogramma('hello'))
# print(izogramma('halo'))

# print((lambda word:  True if len(word) == len(set(word)) else False)('hello'))

# def reverse_int(num:int=23) -> int:
#     return int(str(num)[::-1])
# print(reverse_int(27))

def count_words(word:str):
    word_split = word.lower().replace(',', '').split()
    res = {}
    for n in word_split:
        res[n] = word_split.count(n)
    return res
print(count_words("Money, money, money, it's always sunny, in the richmen's world"))
print(count_words("Geeks Studio Python, geeks in Osh"))
# count_words("Money, money, money, it's always sunny, in the richmen's world")")
