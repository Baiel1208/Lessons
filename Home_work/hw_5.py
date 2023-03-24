# 1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd':
# 600}. Объедините их в один при помощи встроенных функций языка Python.
# Подсказка: метод update()
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

# 2) Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2,
# ‘num_3’ : 3, ‘num_100’ : 100} Необходимо умножить все числовые значения
# словаря на 5 и вывести в терминал.

numbers = {'num_1': 1, 'num_2': 2, 'num_3': 3, 'num_100': 100}

for key, value in numbers.items():
    if isinstance(value, int):
        numbers[key] = value * 5

print(numbers)


# 3) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза
student = {'name' : 'Askhat', 'age' : 17}
for key, value in student.items():
    if isinstance(value, int):
        student[key] = value * 2
print(student)

# 4) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}. Обновите age в 16
student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
student['age'] = 16
print(student)

# 5) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Удалите ключ и значение age
student = {'name' : 'Askha', 'age' : 17}
student.pop('age')
print(student)

# 6) Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и значение(Западный Анар)
student = {'name' : 'Askhat'}
student.setdefault('address', 'Западный Анар')
print(student)

# ДОП ЗАДАНИЕ:
# 7)Напишите программу, которая имитирует проверку пароля, придуманного
# пользователем. Пользователь вводит пароль, а потом ещё раз его же, для
# подтверждения.
# И пароль который вводит пользователь записывается в пустое множество после
# проверок
# Если первый пароль, который ввел пользователь короче 8 символов, программа
# выводит на экран слово "Короткий пароль!"
# Если же первый пароль достаточно длинный, но в нём содержится сочетание
# символов "123", программа выводит на экран слово "Простой пароль!"
# Если же предыдущие проверки пройдены успешно, но введённые слова-пароли
# не совпадают, то программа выводит на экран слово "Различаются."
# Если же и третья проверка пройдена успешно, программа выводит "OK"
# (латинскими буквами) и выводит “Пароль создан!”

password1 = set()

password2 = input("Введите пароль: ")
password1.add(password2)

if len(password2) < 8:
    print("Короткий пароль!")
else:
    if "123" in password2:
        print("Простой пароль!")
    else:
        password3 = input("Введите пароль ещё раз для подтверждения: ")
        password1.add(password3)
        
        if password2 == password3:
            print("OK")
            print("Пароль создан!")
        else:
            print("Различаются.")


