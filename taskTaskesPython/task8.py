class Customer:
    def __init__(self, full_name, gender, age, device, browser, total_sum, region):
        self.__full_name = full_name
        self.__gender = gender,
        self.__age = age,
        self.__device = device,
        self.__browser = browser,
        self.__total_sum = total_sum,
        self.__region = region

    def check_device(self):
        if self.__device == "desktop":
            return "компьютерного"
        elif self.__device == "mobile":
            return "мобильного"
        else:
            return "планшетного"

    def describe(self):
        device = self.check_device()
        gender = "мужского " if self.__gender == "male" else "женского"
        verb = "совершил" if gender == "мужского" else "совершила"
        return (
            f"Пользователь: {self.__full_name}, {gender} пола, {self.__age} лет {verb} покупку на {self.__total_sum} y.e."
            f"с {device} браузера {self.__browser}. Регион, из которого совершилась покупка: {self.__region}")


def read_customer_file(file_path):
    customers = []

    with open(file_path, encoding="utf-8") as wb_file:
        lines = [line.strip() for line in wb_file if line.strip()]
        for i in range(0, len(lines), 7):
            block = lines[i: i + 7]
            if len(block) < 7:
                print(f"Пропущен блок итерации {i} {block}\n")
                continue
            try:
                customer = Customer(
                    full_name=block[0].split(": ", 1)[1],
                    gender=block[1].split(": ", 1)[1],
                    age=block[2].split(": ", 1)[1],
                    device=block[3].split(": ", 1)[1],
                    browser=block[4].split(": ", 1)[1],
                    total_sum=block[5].split(": ", 1)[1],
                    region=block[6].split(": ", 1)[1]
                )
                customers.append(customer)
            except IndexError as e:
                print(f"Ошибка заполнения пользователя из блока {i}")
    return customers


def write_customer_file_to_txt(customers, output_path):
    with open(output_path, "w", encoding="utf-8") as out_wb_file:
        for customer in customers:
            out_wb_file.write(customer.describe() + "\n")

    print(f"Запись в файл {output_path} завершена!")



if __name__ == "__main__":##=_=
    file_path = f"data_task8/web_clients_formatted.csv"
    output_path = f"descriptions.txt"

    customers = read_customer_file(file_path)
    write_customer_file_to_txt(customers, output_path)
