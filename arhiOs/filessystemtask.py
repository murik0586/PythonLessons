import os
import stat
import platform

# Попробуем использовать psutil, если мы на Windows
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

def print_filesystem_info(path):
    print("📁 Информация о файловой системе:")

    if platform.system() == "Windows":
        if not PSUTIL_AVAILABLE:
            print("psutil не установлен. Установи его командой: pip install psutil")
            return

        partitions = psutil.disk_partitions()
        for p in partitions:
            if path.startswith(p.mountpoint):
                usage = psutil.disk_usage(p.mountpoint)
                print(f"Диск: {p.device}")
                print(f"Файловая система: {p.fstype}")
                print(f"Точка монтирования: {p.mountpoint}")
                print(f"Всего: {usage.total} байт")
                print(f"Свободно: {usage.free} байт")
                print(f"Используется: {usage.used} байт")
                break
    else:
        stats = os.statvfs(path)
        print(f"Размер блока: {stats.f_bsize} байт")
        print(f"Общее количество блоков: {stats.f_blocks}")
        print(f"Свободные блоки: {stats.f_bfree}")
        print(f"Свободные блоки для пользователя: {stats.f_bavail}")
        print(f"Общее количество inode: {stats.f_files}")
        print(f"Свободные inode: {stats.f_ffree}")

def print_file_info(file_path):
    print("\n📄 Информация о файле:")
    st = os.stat(file_path)

    print(f"Inode: {st.st_ino}")
    print(f"Размер: {st.st_size} байт")
    print(f"Атрибуты файла (число): {st.st_mode}")

    if stat.S_ISREG(st.st_mode):
        file_type = "Обычный файл"
    elif stat.S_ISDIR(st.st_mode):
        file_type = "Каталог"
    elif stat.S_ISLNK(st.st_mode):
        file_type = "Символическая ссылка"
    else:
        file_type = "Другой тип файла"

    print(f"Тип файла: {file_type}")

def main():
    file_path = "example.txt"

    # Создание временного файла
    with open(file_path, "w") as f:
        f.write("Пример текста для анализа.\n")

    print_filesystem_info(file_path)
    print_file_info(file_path)

    os.remove(file_path)

if __name__ == "__main__":
    main()
