"""Домашнее задание 3

Описание задания
Прежде чем выполнять задание, установите Jupyter Notebook или используйте Google Colab.

Задание
Написать код на Python в среде Jupyter Notebook для решения задачи.

Необходимо написать программу, которая сформирует словарь данных на основании заданных критериев
(ключ = ключ в исходной структуре, значение = True — если количество ниже 20 , False — остальные случаи).
При разработке использовать dict comprehension.

Исходные данные имеют следующую структуру:

items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34', 'price': 89.9},
 'cheese':{'name': сыр молочный 1 кг.', 'count': 12', 'price': 990.9},
 'sausage':{'name': колбаса 1 кг.', 'count': 122', 'price': 1990.9}
}
Результат:

price_less_20 = {
 'milk15': False,
 'cheese': True,
 'sausage': False
}
"""


items = {"Lays": {"name " : "Зелень и лук 220 грамм", "count" : 22, "price": 150}, "Adrenalin": {"name":"classic 0.47 мл", "count" : 12, "price": 129.9}, "Cheese": {"name":"С грецким орехом", "count" : 22, "price": 333}}

price_product = { key: value["count"]< 20 for key, value in items.items()}
print(price_product)