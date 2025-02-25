
list_product = []  # квадратные скобки - это список, это в java - массивы, здесь список(изменяемый)
shops_and_total_prices = []
while True:  # чтобы код повторялся аналогично Котлин
    print("""
1.Добавить товар
2.Добавить магазин и цену
3.Рассчитать выгодный магазин
4.Выход
""")

    operation = input("Выберите действие: ")
    if not operation.isdigit() or int(operation) not in {1, 2, 3, 4}:  # если в operation не число, и не что-то из перечисленных чисел
        print("Введите что-то из меню, пожалуйста!")
        continue

    operation = int(operation)  # переводим в инт
    match operation:  # аналог switch
        case 1:
            list_product.append(input(
                "Введите название продукта! ").strip().capitalize())  # добавляем в список продукт strip - это удаление пробелов,
            # а второй метод - делаем название с заглавной буквы.
            shops_and_total_prices.append([])  # добавляем в список из магазинов и цен - один список (там будет список потому что у каждого магазина еще цена нужна).

        case 2:
            if len(list_product) > 0:
                print("Выберите продукт для добавления магазина и цены ")

                for idx, product in enumerate(list_product,start=1):
                    print(f"{idx}.{product}")
                    # Метод буквально сам индексирует элементы, а старт -
                    # это задаем начальное число индексации.idx - это id,
                    # визуально похоже на перебор с де-структуризацией из котлина.
                      # Собственно выводим все списком

                number_product = input("Введите номер продукта ")  # просим ввести номер продукта
                if not number_product.isdigit() or not (
                    1 <= int(number_product) <= len(list_product)):  # если не число, и не больше 1 или
                    # не равен и не больше или равен размеру списка с продуктами
                    print("Некорректный выбор товара!")
                    continue
                number_product = int( number_product) - 1  # Конечно же минусуем(чтобы не выйти за границы размера списка

                shop = input("Введите название магазина").strip().capitalize()  # Вводим магазин и сохраняем в переменную
                price = input("Введите цену за товар!")  # Добавляем цену
                if not price.isdigit():  # Проверяем что не число!
                    print("цена должна быть числом!")
                    continue
                price = int(price)
                shop_found = False  # Флаг для того, чтобы проверить есть ли этот магазин в списке уже
                for shop_info in shops_and_total_prices[number_product]:  # Ищем этот магазин
                    if shop_info[0] == shop:  # Если есть - то
                        shop_info[1] += price  # Просто увеличиваем цену, которая была!
                        shop_found = True  # Меняем флаг на TRUE
                        break
                if not shop_found:  # Если все таки нет в списке
                            shops_and_total_prices[number_product].append([shop, price])  # Берем и добавляем список магазин + цена в список наш.
            else:
                print("Сначала добавьте продукт!(Хотя бы один!)")
                continue
        case 3:  # ВЫВЕСТИ ИТОГОВЫЕ СУММЫ И РАССЧИТАТЬ ВЫГОДНЫЙ МАГАЗИН ДЛЯ ПОКУПКИ
            # 1. Рассчитываем общую стоимость по магазинам.
            if len(shops_and_total_prices) > 0:
                shop_total = {}  # Словарь для хранения общей стоимости по магазинам
                for product_shops in shops_and_total_prices:
                    for shop, price in product_shops:
                        shop_total[shop] = shop_total.get(shop, 0) + price
                print("\nОбщая стоимость покупок по магазинам:")
                for shop, total_price in shop_total.items():
                    print(f"Магазин:{shop}, итоговая сумма: {total_price}")

                min_shop = min(shop_total, key=shop_total.get)
                print(f"Самый выгодный магазин: {min_shop} c общей стоимостью {shop_total[min_shop]}")
            else:
                print("Вы еще не добавили магазин и цены к ним!")
        case 4:
            print("Выход из программы")
            break



