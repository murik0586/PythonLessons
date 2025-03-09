import numpy as np
import matplotlib.pyplot as plt

# Параметры моделирования
t_c = 0.00064  # Время моделирования, сек (1 мс)
h = 0.000001  # Шаг по времени, сек (1 мкс)
time = np.arange(0, t_c, h)  # Массив времени

# Логические уровни
logic_0 = 0
logic_1 = 5

# Функция генерации прямоугольных импульсов
def generate_square_wave(freq, time, logic_0, logic_1):
    period = 1 / freq
    return np.array([logic_1 if (t % period) < (period / 2) else logic_0 for t in time])

# Функция ограничения диапазона
def clamp(minimum, maximum, number):
    return max(minimum, min(maximum, number))

# Генерация сигналов
a2 = generate_square_wave(500, time, logic_0, logic_1)
a1 = generate_square_wave(1000, time, logic_0, logic_1)

x4 = generate_square_wave(4000, time, logic_0, logic_1)
x3 = generate_square_wave(8000, time, logic_0, logic_1)
x2 = generate_square_wave(16000, time, logic_0, logic_1)
x1 = generate_square_wave(32000, time, logic_0, logic_1)

# Задержки логических элементов
NOT_lat = 1
AND_lat = 1
OR_lat = 1

e1, e2, e3, e4 = [], [], [], []

for t in range(len(time)):
    t2 = clamp(0, len(time) - 1, t - (OR_lat + NOT_lat))
    logic1, logic2 = a1[t2], a2[t2]
    e1.append(logic_1 if not (logic1 or logic2) else logic_0)

    t2 = clamp(0, len(time) - 1, t - AND_lat)
    t3 = clamp(0, len(time) - 1, t - (NOT_lat + AND_lat))
    logic1, logic2 = a1[t2], a2[t3]
    e2.append(logic_1 if logic1 and not logic2 else logic_0)

    logic1, logic2 = a1[t3], a2[t2]
    e3.append(logic_1 if not logic1 and logic2 else logic_0)

    t2 = clamp(0, len(time) - 1, t - AND_lat)
    logic1, logic2 = a1[t2], a2[t2]
    e4.append(logic_1 if logic1 and logic2 else logic_0)

# Выходной сигнал
F = []
for t in range(len(time)):
    t2 = clamp(0, len(time) - 1, t - (AND_lat + OR_lat))
    F.append(max(
        (e1[t2] and x1[t2]),
        (e2[t2] and x2[t2]),
        (e3[t2] and x3[t2]),
        (e4[t2] and x4[t2])
    ))

# Визуализация сигналов
plt.figure(figsize=(9, 9))

plt.subplot(7, 1, 7)
plt.plot(time, a2, label='a2')
plt.xlabel("Время (с)")
plt.ylabel("Вольт")
plt.grid()
plt.legend()

plt.subplot(7, 1, 6)
plt.plot(time, a1, label='a1')
plt.ylabel("Вольт")
plt.grid()
plt.legend()

plt.subplot(7, 1, 5)
plt.plot(time, x4, label='x4')
plt.plot(time, e4, label='e4 с зад.')
plt.ylabel("Вольт")
plt.grid()
plt.legend()

plt.subplot(7, 1, 4)
plt.plot(time, x3, label='x3')
plt.plot(time, e3, label='e3 с зад.')
plt.ylabel("Вольт")
plt.grid()
plt.legend()

plt.subplot(7, 1, 3)
plt.plot(time, x2, label='x2')
plt.plot(time, e2, label='e2 с зад.')
plt.ylabel("Вольт")
plt.grid()
plt.legend()

plt.subplot(7, 1, 2)
plt.plot(time, x1, label='x1')
plt.plot(time, e1, label='e1 с зад.')
plt.ylabel("Вольт")
plt.grid()
plt.legend()

plt.subplot(7, 1, 1)
plt.plot(time, F, label='F')
plt.ylabel("Вольт")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
