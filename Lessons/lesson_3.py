#Lists - списки
# name1 = "Nurbolot"
# name2 = "Anton"
# name3 = "Bayzak"
# name4 = "Adilet"

# names = ["Nurbolot", "Anton", "Bayzak", "Adilet"]
# print(names)

# lst = [10, 1.0, "Geeks", False]
# print(lst[2][0])
# print(lst[0:2][0])

# cities = ["Bishkek", "Osh", "Naryn", "Talas"]
# print(cities)
# cities.append("Batken") #Метод append добавляет элемент в конец списка
# print(cities)
# cities.append("Tokmok") #Метод append добавляет элемент в конец списка
# print(cities)
# cities.insert(0, "Karakol") #Метод insert добавляет элемент по индексу и переставляет
# print(cities)
# cities.remove("Bishkek") #Метод remove удаляет элемент по значению, которую мы передаем
# print(cities)
# cities.pop(0) Метод pop удаляет элемент из списка по индексу
# print(cities)

# del cities[1:3] #Оператор del удаляет из списка по индексу и также по срезам
# print(cities)

# cars = ["Toyota", "Honda", "BMW", "Mercedes", "Honda"]
# print(cars.count("Honda"))
# print(cars["Mercedes"])
# cars[0] = "KIA"
# print(cars)
# print(cars[1:4:2])
# print(cars[::-1])
# cars.sort()
# print(cars)

# numbers = [10, 11, 100, 1, 3, 4, 400, 1001, 0.1, 5.0]
# numbers.sort(reverse=True)
# print(numbers)

# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# if 100 in numbers:
#     print(True)
# else:
#     print(False)
# numbers.clear()
# print(numbers)

# nums1 = [10, 20, 30, 40, 50, int("199")]
# nums2 = [60, 70, 80, 90, 100]
# num3 = nums2 + nums1
# print(num3)
# num3.sort()
# print(num3)

# numbers = [2.0, 10, "Hello", True, [10, 20, 30]]
# print(numbers)

#Tuple - кортежи
# tup = (10, 3.0, "Geeks", False)
# print(tup)
# print(tup.count(10))
# print(tup.index("Geeks"))
# print(tup[2])
# print(tup[0:2])
# lst_tup = list(tup)
# print(lst_tup)
# lst_tup.append([1, 2, 3, 4])
# print(lst_tup)
# tup = tuple(lst_tup)
# print(tup)

# import dis

# dis.dis("[1, 2, 3, 4]")
# dis.dis("(1, 2, 3, 4)")

# tup = ("Hello",)
# print(type(tup))
