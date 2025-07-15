from datetime import datetime as dt


class DataFormatException(Exception):
    def __init__(self, message="Неверный формат даты"):
        self.message = message
        super().__init__(self.message)


def parse_date(input_date_str: str, source_newspaper: str):
    """
       Парсит дату согласно формату указанной газеты

       Args:
           input_date_str: строка с датой
           source_newspaper: название газеты

       Returns:
           Объект datetime с распарсенной датой

       Raises:
           DataFormatException: при неизвестной газете или неверном формате даты
       """
    formats = {"The Moscow Times": "%A, %B %d, %Y",
               "The Guardian": "%A, %d.%m.%y",
               "The Daily News": "%A, %d %B %Y"
               }
    if source_newspaper not in formats:
        raise DataFormatException("Неизвестная газета!")
    try:
        return dt.strptime(input_date_str, formats[source_newspaper])
    except ValueError as ec:
        raise DataFormatException(f"Неверный формат даты для {source_newspaper}") from ec


def main():
    # Тест данные
    test_data = [
        ("The Moscow Times", "Wednesday, October 2, 2002"),
        ("The Guardian", "Friday, 11.10.13"),
        ("The Daily News", "Thursday, 18 August 1977")
    ]

    print("Тестовые примеры: ")

    for newspaper_name, date_string in test_data:
        try:
            date_obj = parse_date(date_string, newspaper_name)
            print(f"{newspaper_name}: {date_obj.date()}")
        except DataFormatException as e:
            print(f"{newspaper_name}: {e}")

    # Интерактивный режим

    print("\nИнтерактивный режим (для выхода введите \"end\") ")
    while True:

        user_input = input("Введите название газеты в формате: 'Газета, дата ':\n> ")

        if user_input.strip().lower() == "end": break

        parts = [part.strip() for part in user_input.split(", ", 1)]
        if len(parts) != 2:
            print("Ошибка: Используйте формат 'Газета, дата'")
            continue
        newspaper, date_str = parts

        try:
            date_obj = parse_date(date_str, newspaper)
            print(f"Успешно: {newspaper} - {date_obj.date()}")

        except DataFormatException as e:
            print(f"Ошибка: {e}.")


if __name__ == "__main__":
    main()
