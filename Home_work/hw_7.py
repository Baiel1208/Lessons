"""
1) Есть обычная функция
def hello(x):
print(x * x - 10)
Превратите данную функцию в lambda функцию
"""

def hello(x):
    print(x * x - 10)
hello(1)

print((lambda x: x * x - 10)(1))

"""
2) Есть список name = [“Kuma”, “Nurtilek”, “Zina”, “Edzen”, “Kuma”, “Aitenur”, “Zina” ]
Уберите дубликаты с данного листа с помощью lambda функций
"""

print(set(list(filter(lambda name: name, ['Kuma', 'Nurtilek', 'Zina', 'Edzen', 'Kuma', 'Aitenur', 'Zina' ] ))))

"""
3) Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Выведите с помощью lambda функции чётные числа с списка
"""

print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

"""
4) names = [“azat”, “zina”, “kuma”, “anna”, “sas”]
Вывести с помощью lambda функции имена палиндромы
"""

print(list(filter(lambda names: names, ["azat", "zina", "kuma", "anna", "sas"] )))

"""
ДОП ЗАДАЧА:
5) Дайте пользователю ввести две отметки времени вместе с секундами. Ваша
программа должна найти разницу между двумя отрезками времени и вывести
на экран в секундах.
Условие: Первая отметка должна быть раньше по времени чем вторая.**
Пример:
1-ввод: 10:00:30
2-ввод: 15:05:09
Ответ: 18 279 секунд разница
"""
import datetime

time = input("Первое время (в формате чч:мм:сс): ")
time1 = datetime.datetime.strptime(time, "%H:%M:%S")

time2_2 = input("Второе время (в формате чч:мм:сс): ")
time2 = datetime.datetime.strptime(time2_2, "%H:%M:%S")

a = (time2 - time1).total_seconds()

print("Разница: ", a, " секунд")

