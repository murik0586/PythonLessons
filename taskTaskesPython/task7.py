import threading
import multiprocessing
import time


def formula1(x):
    return x ** 2 - x ** 2 + x * 4 - x * 5 + x + x


def formula2(x):
    return x + x


# Задание 1: Параллельное выполнение с использованием потоков

def task_with_threads(iterations):
    print(f"\nПотоки: {iterations} итераций:")
    start_time = time.time()

    res1, res2 = None, None

    def calc1():
        nonlocal res1
        start = time.time()
        for i in range(iterations):
            res1 = formula1(i)
        end = time.time()
        print(f"Формула 1: {end - start:.5f} сек")

    def calc2():
        nonlocal res2
        start = time.time()
        for i in range(iterations):
            res2 = formula2(i)
        end = time.time()
        print(f"Формула 2: {end - start:.5f} сек")

    thread1, thread2 = threading.Thread(target=calc1), threading.Thread(target=calc2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    start3 = time.time()
    res3 = res1 + res2

    print(f"Формула 3: {time.time() - start3:.5f} сек")
    print(f"Общее время: {time.time() - start_time:.5f} сек")


def task_with_processing(iterations):
    f1,f2 = 'formula1','formula2'

    print(f"Процессы: {iterations} итераций:")
    start_time = time.time()
    output = multiprocessing.Queue()

    def calc1():
        start = time.time()
        result1 = None
        for i in range(iterations):
            result1 = formula1(i)
        end = time.time()
        output.put((f1, result1, end - start))

    def calc2():
        start = time.time()
        result2 = None
        for i in range(iterations):
            result2 = formula2(i)
        end = time.time()
        output.put((f2, result2, end-start))

    process_one,process_two = multiprocessing.Process(target= calc1()),multiprocessing.Process(target= calc2())
    process_one.start()
    process_two.start()

    results = {}
    for _ in range(2):
        name,result,duration =  output.get()
        results[name]= (result,duration)
    process_one.join()
    process_two.join()

    print(f"Формула 1: {results[f1][1]:.5f} сек")
    print(f"Формула 2: {results[f2][1]:.5f} сек")

    start3 = time.time()

    result3 = results[f1][0] + results[f2][0]

    end3 = time.time()
    print(f"Формула 3: {end3 - start3:.5f} сек")
    total_time = time.time() - start_time
    print(f"Всего времени потрачено: {total_time:.5f} сек")
# def task_with_processing(iterations):
#     print(f"\nПроцессы: {iterations} итераций:")
#     output = multiprocessing.Queue() #заводим очередь
#     start_time = time.time() #Обозначаем начало
#
#     def calc1():
#         start = time.time()
#         result1 = None
#
#         for i in range(iterations):
#             result1 = formula1(i)
#         end = time.time()
#         output.put(('formula1', result1, end - start)) # добавляем в очередь данные
#
#     def calc2():
#         start = time.time()
#         result2 = None
#
#         for i in range(iterations):
#             result2 = formula2(i)
#         end = time.time()
#         output.put(('formula2',result2,end - start))
#
#     process1,process2 = multiprocessing.Process(target= calc1()),multiprocessing.Process(calc2())
#     process1.start()
#     process2.start()
#
#     results = {}
#     for _ in range(2):
#         name,result,duration = output.get()
#         results[name] = (result,duration)
#     process1.join()
#     process2.join()
#     print(f"Формула1: {results['formula1'][1]:.5f} сек")
#     print(f"Формула2: {results['formula2'][1]:.5f} сек")
#
#     start3 = time.time()
#     result3 = results['formula1'][0] + results['formula2'][0]
#     end3 = time.time()
#     print(f"Формула 3: {end3-start3:.5f} сек")
#     total_time = time.time() - start_time
#     print(f"Всего времени: {total_time:.5f} сек")
#


# Основная часть программы
if __name__ == '__main__':
    """
    Точка входа в программу. Выполняем оба задания последовательно.
    Условие if __name__ == '__main__' обязательно для multiprocessing.
    """

    # Задание 1: Выполняем с потоками
    print("\n--- Задание 1: Параллельные вычисления с потоками ---")
    task_with_threads(10_000)  # 10,000 итераций
    task_with_threads(100_000)  # 100,000 итераций

    print("\n--- Задание 2: Параллельные вычисления с процессами ---")
    task_with_processing(10_000)  # 10,000 итераций
    task_with_processing(100_000)  # 100,000 итераций
