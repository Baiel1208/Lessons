# Множества set, frozenset

# emails = {'geeks@edu.kg', 'kurmanbek@gmail.com', 'nur@gmail.com', 'geeks@edu.kg'}
# print(emails)

# st = {10, 1.0, 1, True, "Hello", (1, 2, 3), False}
# print(st)

# strange_app = set('TikTok')
# print(strange_app)

# company = {'Google', 'Meta', 'Netfix'}
# company.add('Geeks')
# print(company)
# company.remove('Meta')
# print(company)
# company.pop()
# print(company)

# nums1 = [10, 20, 30, 40, 50]
# nums2 = [30, 40, 50, 60, 70]
# print(nums1 + nums2)
# nums1 = set(nums1 + nums2)
# print(nums1)
# nums3 = {10, 20, 30, 40, 50, 60, "20"}
# print(nums3)

# frzn_set = frozenset({10, 20, 30, 30, 20})
# print(frzn_set)

# import dis
# # dis.dis("{1, 2, 3, 4, 5}")
# dis.dis("frozenset({1, 2, 3, 4, 5})")

# Dictionary - словари
# nums = [40, 50, 10, 20, 5]
# print(len(nums))
# student = {'name' : 'Nurbolot', 'age' : 18}
# print(student['name'])
# print(student['age'])
# student.setdefault('job', 'Python Developer')
# print(student)
# student.pop('age')
# print(student)
# student.popitem()
# print(student)
# student['name'] = 'Anton'
# print(student)

# osh = {
#     'name' : 'Osh',
#     'year' : 3023,
#     'population' : 734000
# }
# print(osh.keys())
# print(osh.values())
# print(osh.items())

# for k, v in osh.items():
#     print(k, v)

# contact = {'MHCS' : 112}
# while True:
#     command = input("1 - посмотреть, 2 - добавить, 3 - удалить, 4 - обновить: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Имя которую надо добавить: ")
#         add_number = input("Номер которую надо добавить: ")
#         contact.setdefault(add_name, add_number)
#         print("Успешно добавлено")
#     elif command == "3":
#         delete_name = input("Кого удалить: ")
#         contact.pop(delete_name)
#         print("Успешно удалено")
#     elif command == "4":
#         update_name = input("Кого обновить: ")
#         new_number = input("Новый номер: ")
#         contact[update_name] = new_number
#         print("Успешно обновлено")

