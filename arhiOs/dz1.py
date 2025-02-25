import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры
Tc = 1e-3  # Время моделирования (1 мс)
h = 1e-6   # Шаг по времени (1 мкс)
t = np.arange(0, Tc, h)  # Временной массив

# Частоты треугольных сигналов
frequencies = [10e3, 5e3, 2e3]  # 10, 5 и 2 кГц
amplitude = 5  # Амплитуда

# Генерируем треугольные сигналы
Y = sum(amplitude * (2 * np.abs(2 * (t * f % 1) - 1) - 1) for f in frequencies)

# Запрещённая зона
Umin, Umax = 2, 4

# Выход логического каскада
output = np.zeros_like(t)
for i in range(len(t)):
    if Y[i] > Umax:
        output[i] = 5
    elif Y[i] < Umin:
        output[i] = 0

# Визуализация
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t, Y, label='Треугольный сигнал', color='b')
axs[0].set_ylabel('Напряжение (В)')
axs[0].set_title('Исходный периодический сигнал')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(t, output, label='Цифровой сигнал', color='r')
axs[1].set_xlabel('Время (с)')
axs[1].set_ylabel('Напряжение (В)')
axs[1].set_title('Выход логического каскада')
axs[1].legend()
axs[1].grid(True)

plt.show()
