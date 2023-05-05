"""Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.
"""

alfE = "qwertyuiopasdfghjklzxcvbnm"
name_file = input("Введите имя файла: ")
SIMBOLS = "!@#$%^&*()_+=|?><.,;'{}[]"
#
with open(name_file, "r", encoding="UTF-8") as f:
    text = f.read().translate({ord(i): None for i in SIMBOLS}).lower().split(" ")

words_set = set(text)
words_dict = dict.fromkeys(words_set, 0)
for word in text:
    if len(word) > 3:
        words_dict[word] += 1
max_elem = max(words_dict.items(), key=lambda x: x[1])

word_len_dict = {}
for word in text:
    word_en = True
    for char in word:
        if char not in alfE:
            word_en = False
            break
    if word_en:
        word_len_dict[word] = len(word)
long_word = max(word_len_dict.items(), key=lambda x: x[1])

print(f"Самое длинное английское слово: {long_word[0]} длина которго {long_word[1]} символов")
print(f"Слово, длинее 3х букв: {max_elem[0]} встречается {max_elem[1]} раз")
