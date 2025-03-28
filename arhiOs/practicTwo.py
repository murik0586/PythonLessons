import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

T1 = 1e-3  # длительность визуализации
dt = 1e-6  # шаг моделирования
A = 5  # Амплитуда
F1 = 5e3  # 5 кГц
F2 = 10e3  # 10 кГц


t = np.arange(0, T1, dt)

# Меандр
meandr_5kHz = A * square(2 * np.pi * F1 * t)
meandr_10kHz = A * square(2 * np.pi * F2 * t)

rect_5kHz = A * square(2 * np.pi * F1 * t, duty=0.25)
rect_10kHz = A * square(2 * np.pi * F2 * t, duty=0.25)

fig, axs = plt.subplots(2, 2, figsize=(12, 6))

axs[0, 0].plot(t, meandr_5kHz)
axs[0, 0].set_title("Меандр 5 кГц")
axs[0, 0].grid()

axs[0, 1].plot(t, meandr_10kHz)
axs[0, 1].set_title("Меандр 10 кГц")
axs[0, 1].grid()

axs[1, 0].plot(t, rect_5kHz)
axs[1, 0].set_title("Прямоугольный сигнал 5 кГц, скважность 4")
axs[1, 0].grid()

axs[1, 1].plot(t, rect_10kHz)
axs[1, 1].set_title("Прямоугольный сигнал 10 кГц, скважность 4")
axs[1, 1].grid()

plt.tight_layout()
plt.show()
