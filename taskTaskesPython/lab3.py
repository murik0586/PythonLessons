n = 3  # Количество строк
m = 3  # Количество столбцов

iter_one = 0

def chocolate_breaking(n: int, m: int) -> int:
    global iter_one
    iter_one+=1
    if n == 1 and m == 1:
        print(f"Попали при {iter_one} вызове в ветку 1: ")
        return 0
    if n == 1:
        print(f"Попали при {iter_one} вызове в ветку 2: ")
        return m - 1
    if m == 1:
        print(f"Попали при {iter_one} вызове в ветку 3: ")
        return n - 1

    print(f"Попали при {iter_one} вызове в последний ретерн: ")
    return  1 + chocolate_breaking(n - 1, m) + chocolate_breaking(1, m)


print(f"Общее количество разломов {chocolate_breaking(n, m)}")
