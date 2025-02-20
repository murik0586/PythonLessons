import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
period = 0.0004  # 0.4 мс
step = 1e-6  # 1 мкс шаг
simulation_duration = 1e-3  # 1 мс длительность визуализации
v_low = 0.5  # Логический 0
v_high = 4.0  # Логическая 1

axisX = np.arange(0, simulation_duration, step)
axisY = []
t = 0

for i in range(len(axisX)):
    if t >= period:
        t -= period
    if t < 0.3 * period:
        axisY.append(v_low)
    elif t < 0.35 * period:
        axisY.append((t - 0.3 * period) * ((v_high - v_low) / (0.05 * period)) + v_low)
    elif t < 0.4 * period:
        axisY.append((-(t - 0.35 * period)) * ((v_high - v_low) / (0.05 * period)) + v_high)
    else:
        axisY.append(v_low)
    t += step

plt.figure(figsize=(10, 5))
plt.plot(axisX * 1e3, axisY, label='Треугольный сигнал')  # Перевод в мс
plt.axhline(v_low, color='red', linestyle='--', label='Лог. 0 (0.5 В)')
plt.axhline(v_high, color='green', linestyle='--', label='Лог. 1 (4 В)')
plt.xlabel('Время (мс)')
plt.ylabel('Напряжение (В)')
plt.title('Треугольный сигнал')
plt.legend()
plt.grid()
plt.show()