"""
1) Напишите функцию, которая принимает список, из списка выдает случайное
значение из списка и записывает результат в txt файл. Список language =
["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
"""

import random

def random_lan(languages):
    random_language = random.choice(languages)
    
    with open('file.txt', 'w') as f:
        f.write(random_language)
    
    return random_language

language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
random_language = random_lan(language)
print(random_language)

"""
2) У нас есть переменная text которая, хранит в себе текст:
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.
Откройте файл text.txt и запишите текст в файл 2 способами
"""

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum."""

f = open('text.txt' , 'w')
f.write(text)
f.close()


with open('text.txt' , 'w') as r:
    r.write(text)


"""
ДОП ЗАДАЧА:
3) Написать программу, которая откроет созданный в задаче 2 файл text.txt,
скопирует весь текст и запишет его в новый файл wikipedia.txt .
"""

# from hw_8 import text

with open("text.txt", "r") as file:
    text = file.read()

with open("wikipedia.txt", "w") as file:
    file.write(text)