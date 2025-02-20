"""Домашнее задание 1"""

# 1-ое задание.
text = "test"
size = len(text)
if size % 2 == 1:
    index = size // 2 # Используем целочисленное деление
    print(text[index])
else:
    index = len(text) // 2
    print(text[index-1] + text[index])

# 2-ое задание.
# boys = ['Alex','Peter','john','Arthur','Richard','Sergei']
boys = ['Alex','Peter','john','Arthur','Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
list_talk = []
if len(boys) != len(girls):
    print("Кто-то может остаться без пары!")


else:

    for index, name in enumerate(boys):
        list_talk.append([name,girls[index]])

    print("результат:")
    for pair in list_talk:
        print(f"{pair[0]} и {pair[1]}")



