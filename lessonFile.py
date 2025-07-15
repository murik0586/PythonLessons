# f = open("visit_log.csv",'r', encoding='utf-8')
#
# print(f.readline())
#
# content = f.readlines()
# f.seek(0)
#
# for i, line in enumerate(f):
#     print(i+1,line)
#     if i >= 4: break
#
# another_line = f.readline().strip().split(',')
#
# print(another_line)
# import json
# i = 0
# with open("purchase_log.txt", encoding='utf-8') as fl:
#     for line in fl:
#         line = line.strip()
#
#         dict_ = json.loads(line)
#         print(dict_)
#
#         i+=1
#         if i > 5: break
#
# data = {}


# import os
#
# # 1. Определяем путь к рабочему столу
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# print(f"Путь к рабочему столу: {desktop}")
#
# # 2. Проверяем существование папки
# target_dir = os.path.join(desktop, "NetMedia")
# if not os.path.exists(target_dir):
#     print(f"Ошибка: Папка не найдена - {target_dir}")
#     print(f"Содержимое рабочего стола: {os.listdir(desktop)}")
# else:
#     # 3. Поиск .kt-файлов
#     kt_files = []
#     for root, dirs, files in os.walk(target_dir):
#         for file in files:
#             if file.lower().endswith(".kt"):
#                 full_path = os.path.join(root, file)
#                 kt_files.append(full_path)
#
#     # 4. Вывод результатов
#     print(f"\nНайдено .kt-файлов: {len(kt_files)}")
#     for i, file_path in enumerate(kt_files, 1):
#         print(f"{i}. {file_path}")
#
#     if not kt_files:
#         print("Файлы .kt не найдены. Содержимое папки:")
#         print(os.listdir(target_dir))
