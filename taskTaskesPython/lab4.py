import json
import xml.etree.ElementTree as ET
from pathlib import Path
import yaml


def read_xml(file_path):
    try:
        tree = ET.parse(file_path)  # создаем дерево элементов
        root = tree.getroot()  # получаем корневой элемент документа
        data = []
        for item in root:
            entry = {}
            for field in item:
                entry[field.tag] = field.text
            data.append(entry)  # Переносим за пределы внутреннего цикла
        return data
    except ET.ParseError as e:
        raise ValueError(f"Ошибка парсинга XML: {e}")


def read_json(file_path):
    with open(file_path, 'r',
              encoding='utf-8') as fl:  # r - это для чтения, нам нужно сначала прочитать и потом уже записать.
        return json.load(fl)


def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_xml(data, name_file):
    root = ET.Element("Люди")
    for element in data:
        person = ET.SubElement(root, "Человек")
        for key, value in element.items():
            field = ET.SubElement(person, key)
            field.text = str(value)
    tree = ET.ElementTree(root)
    ET.indent(tree, space='    ')  # Добавляем отступы
    tree.write(f"{name_file}", encoding="utf-8", xml_declaration=True)


def write_json(data, name_file):
    with open(name_file, "w", encoding="utf-8") as fl:
        json.dump(data, fl, ensure_ascii=False, indent=2)


def write_yaml(data, name_file):
    with open(name_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)


def convert_file(input_path, output_format):
    try:
        input_format = Path(input_path).suffix[1:].lower()
        if input_format == "json":
            data = read_json(input_path)
        elif input_format == "xml":
            data = read_xml(input_path)
        elif input_format in ("yaml", "yml"):
            data = read_yaml(input_path)
        else:
            raise ValueError(f"Некорректный входной формат : {input_format}")

        output_path = Path(input_path).with_suffix(f".{output_format}")
        if output_format == "xml":
            write_xml(data, output_path)
        elif output_format == "json":
            write_json(data, output_path)
        elif output_format == "yaml":
            write_yaml(data, output_path)
        else:
            raise ValueError(f"Некорректный выходной формат: {output_format}")

        print(f"Конвертация успешна: {input_path} -> {output_path}")
        return True
    except Exception as e:
        print(f"Ошибка при конвертации: {str(e)}")
        return False


def main():
    convert_file("data_lab4/jsonHuman.json", "xml")
    convert_file("data_lab4/jsonHuman.xml", "json")
    convert_file("data_lab4/jsonHuman.xml", "yaml")


if __name__ == "__main__":
    main()
