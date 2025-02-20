import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры
Tc = 1e-3  # Время моделирования (1 мс)
h = 1e-6  # Шаг по времени (1 мкс)
t = np.arange(0, Tc, h)  # Временной массив

# Частоты генераторов
f1 = 5e3  # 5 кГц
f2 = 10e3  # 10 кГц

# Генерируем прямоугольные сигналы
Y1 = 0.5 + 4 * (np.sign(np.sin(2 * np.pi * f1 * t)) > 0)
Y2 = 0.5 + 4 * (np.sign(np.sin(2 * np.pi * f2 * t)) > 0)

# Сигнал на входе логического каскада с учетом емкостной составляющей (Метод Эйлера)
T1, T2 = 1e-5, 2e-5  # Постоянные времени
U1 = np.zeros_like(t)
U2 = np.zeros_like(t)

for i in range(1, len(t)):
    U1[i] = U1[i - 1] + h * (Y1[i] - U1[i - 1]) / T1
    U2[i] = U2[i - 1] + h * (Y2[i] - U2[i - 1]) / T2

# Добавление помехи
A1, A2 = 0.1, 0.3
noise1 = np.random.uniform(-A1, A1, len(t))
noise2 = np.random.uniform(-A2, A2, len(t))
U1_noisy = U1 + noise1
U2_noisy = U2 + noise2

# Логический каскад (обработка запрещенной зоны)
Umin1, Umax1 = 1.5, 3.5
Umin2, Umax2 = 2.0, 4.0
output1 = np.zeros_like(t)
output2 = np.zeros_like(t)

for i in range(1, len(t)):
    if output1[i - 1] == 0 and U1_noisy[i] < Umax1:
        output1[i] = 0
    elif output1[i - 1] == 1 and U1_noisy[i] > Umin1:
        output1[i] = 1
    elif output1[i - 1] == 0 and U1_noisy[i] > Umax1:
        output1[i] = 1
    elif output1[i - 1] == 1 and U1_noisy[i] < Umin1:
        output1[i] = 0

    if output2[i - 1] == 0 and U2_noisy[i] < Umax2:
        output2[i] = 0
    elif output2[i - 1] == 1 and U2_noisy[i] > Umin2:
        output2[i] = 1
    elif output2[i - 1] == 0 and U2_noisy[i] > Umax2:
        output2[i] = 1
    elif output2[i - 1] == 1 and U2_noisy[i] < Umin2:
        output2[i] = 0

# Визуализация
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

axs[0].plot(t, Y1, label='Генератор 5 кГц', color='b')
axs[0].plot(t, Y2, label='Генератор 10 кГц', color='r', linestyle='dashed')
axs[0].set_ylabel('Напряжение (В)')
axs[0].set_title('Исходные импульсные сигналы')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(t, U1, label='Сигнал после емкости (T1)', color='b')
axs[1].plot(t, U2, label='Сигнал после емкости (T2)', color='r', linestyle='dashed')
axs[1].set_ylabel('Напряжение (В)')
axs[1].set_title('Сигнал с учетом емкости')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(t, U1_noisy, label='Сигнал с шумом (A1=0.1)', color='b')
axs[2].plot(t, U2_noisy, label='Сигнал с шумом (A2=0.3)', color='r', linestyle='dashed')
axs[2].set_ylabel('Напряжение (В)')
axs[2].set_title('Сигнал с учетом шума')
axs[2].legend()
axs[2].grid(True)

axs[3].plot(t, output1 * 4 + 0.5, label='Выход 5 кГц', color='b')
axs[3].plot(t, output2 * 4 + 0.5, label='Выход 10 кГц', color='r', linestyle='dashed')
axs[3].set_xlabel('Время (с)')
axs[3].set_ylabel('Напряжение (В)')
axs[3].set_title('Выходной сигнал логического каскада')
axs[3].legend()
axs[3].grid(True)

plt.show()