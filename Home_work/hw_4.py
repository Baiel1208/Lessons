# 1) Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть
# пронумерована. Подсказка: Используйте функцию range() или enumerate()

for i in range(1, 6):
    print(f"Строка {i}: {'0' * 5}")


# 2) Нужно заполнить пустой список от 1 до 100. Полученный результат вывести на
# экран. Подсказка: используйте функцию range() и пустой список

a = []
for aa in range(1, 101):
    a.append(aa)
print(a)

# 3) Вывести на экран все чётные значения в диапазоне от 1 до 497. Подсказка:
# используйте функцию range() или условия

b = []
for bb in range(1, 497):
    if bb % 2 == 0:
        print(bb)

# 4) Суммирование тысячу чисел: создайте список чисел от 1 до 1 000, затем
# воспользуйтесь функциями min() и max() и убедитесь в том, что список действительно
# начинается с 1 и заканчивается 1 000. Вызовите функцию sum() и посмотрите,
# насколько быстро Python сможет просуммировать тысячу чисел

nums = []
for num in range(1, 1001):
    nums.append(num)
print(min(nums))
print(max(nums))
print(sum(nums))

# 5) Заполнить список ста нулями с помощью функции range()

d = []
for c in range(1,2 ):
    d.append(c)
    print(f" {c}: {'0' * 100}")

# 6) Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужно превратить
# кортеж в список и добавить новое значение ‘Tesla’, затем превращаете список обратно
# в кортеж

it_company = ("Google", "Amazon", "Microsoft")
it = list(it_company)
print(it)
it.append("Tesla")
print(it)
it_company = tuple(it)
print(it_company)

# 7) Из 1 задания попробуйте вывести индекс ‘Amazon’

print(it_company.index("Amazon"))
print(it_company[1])

# 8) Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способами

it_company = ("Google", "Amazon", "Microsoft")
company = list(it_company)
company[0] = "Apple"
it_company = tuple(company)
print(it_company)


# 9) Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft’

print(it_company[:: 2])

# 10) Есть кортеж text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
# 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
# 'overview') вам нужно посчитать сколько раз встречается слово python

text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
 'overview')
print(text_tuple.count("Python")) # 2 раза

# ДОП ЗАДАНИЕ:
# 6) Исходные значения двух переменных запросить у пользователя. Поменять значения
# переменных местами. Вывести новые значения на экран. Решите задачу, используя
# только две переменные.

a = input(" ")
b = input(" ")
print("a =", a, "b =", b)
a, b = b, a
print("a =", a, "b =", b)

# 7) Создайте бесконечный цикл. Запросите у пользователя его возраст. Если ему есть
# 18 лет, выведите: "Доступ разрешен" и остановите цикл, иначе "Извините, пользование
# данным ресурсом только с 18 лет" и запросите заново.

while True:
 age = int(input("Сколько вам лет?: "))
 if age >= 18:
    print("Доступ разрешен")
    break
 else:
  print("Извините, пользование данным ресурсом только с 18 лет")