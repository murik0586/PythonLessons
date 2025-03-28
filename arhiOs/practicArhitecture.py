import matplotlib.pyplot as plt
import numpy as np

#сделаем ввод
A = float(input("Введите амплитуду синусоиды"))
F = float(input("Введите частоту синусоиды"))
# Генерирация..
t = np.linspace(0,1,1000)
y = A * np.sin(2 * np.pi * F * t)

plt.plot(t,y, label = f"Синусоида А = {A},F = {F}")
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.title("График синусоидального сигнала")
plt.legend()
plt.grid()
plt.show()