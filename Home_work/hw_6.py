# 1) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
# FYI и т.п.


def a(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    print(acronym)
a("Кыргызская Республика")
a("Ruby on Rails")
a("For your interest")
a("ваша работа Айбек")

# 2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано. Например: “Money, money, money, it’s always sunny, in
# the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
# world: 1.

def count_words(string):
    word_counts = {}
    for word in string.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1      
    return word_counts
string = ("Money, money, money, it's always sunny, in the richmen's world")
print(count_words(string))

# 3) Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.

def is_isogram(word):
    word = word.lower()
    letters = set(word)
    print(len(letters) == len(word))
is_isogram("hello")
is_isogram("world")
is_isogram("Python")
is_isogram("aab")

# 4) Напишите функцию где мы передаем через аргументы число n как целое
# integer, надо вывести целое число в перевернутом виде
# например: n = 27, тогда перевёрнутое n это 72

def reverse_number(n):
    r = str(n)[::-1]
    num = int(r)
    print(num)
reverse_number(342)
reverse_number(96)
reverse_number(321)

# ДОП ЗАДАНИЕ:
# 5) Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
# духе!” Если вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что

def chat_bot():
    while True:
        user = input("Вы: ")
        if "?" in user:
            print("Бот: Конечно!")
        elif user.isupper():
            print("Бот: Успокойся")
        elif not user:
            print("Бот: Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("Бот: ну и что")
chat_bot()