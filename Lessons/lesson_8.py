#Модули
# import moduls
# print(moduls.add(30, 30))
# print(moduls.hello())
# print(moduls.it)
# print(moduls.lambda_add(40, 50))

######################################

# from moduls import add, hello
# print(add(30, 40))
# print(hello())

#####################################

# from moduls import *
# print(add(30, 40))
# print(hello())
# print(it)
# print(lambda_add(10, 5))

########################################

# from main import choice_name
# from moduls import lst_names

# print(choice_name(lst_names))

#Работа с файлами
# f = open('python.txt', 'w')
# f.write('Geeks Python')
# f.close()

# r = open('python.txt')
# print(r.read())
# r.close()

# py = open('hello.py', 'w')
# py.write("print('Hello World')")
# py.close()

# py_r = open('lesson_8.py')
# print(py_r.read())
# py_r.close()

# write_py = open('lesson_8.py', 'a+')
# write_py.write("""
# py_r = open('lesson_8.py')
# print(py_r.read())
# py_r.close()
# """)
# write_py.close()

# n = 0
# while True:
#     n += 1
#     f = open(f'hello{n}.py', 'w')
#     f.write(f"print('Hello{n}')")
#     f.close()
#     if n == 100:
#         break

# import os
# n = 0
# while True:
#     n += 1
#     os.remove(f'hello{n}.py')
#     if n == 100:
#         break
# os.mkdir('hello')
# os.remove('hello')

# with open('geeks.py', 'w') as f:
#     f.write('it = "Geeks"')

# with open('geeks.py') as r:
#     print(r.read())


while True:
    commands = input("1-добавить, 2-посмореть контакты, 3 - удалить: ")
    if commands == "1":
        add_name = input("Имя: ")
        add_number = input("Номер: ")
        with open('contacts.txt', 'a+') as contacts:
            contacts.write(f'{add_name} {add_number}\n')
        print("Успешно записан")
    elif commands == "2":
        with open('contacts.txt') as read_contact:
            print(read_contact.read())