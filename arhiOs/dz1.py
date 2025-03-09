import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# 1. Формируем массив точек по оси времени
# ------------------------------------------------------
# Допустим, моделируем 0...10 мс с шагом 0.01 мс
t_max = 10e-3  # 10 мс
dt = 0.01e-3   # шаг 0.01 мс (10 микросекунд)
T = np.arange(0, t_max, dt)

# ------------------------------------------------------
# 2. Формируем входной сигнал X
# ------------------------------------------------------
# Пример: прямоугольный сигнал с периодом 2 мс
period = 2e-3
X = np.zeros_like(T)
for i, t in enumerate(T):
    # Для простоты пусть сигнал меняется с 0 на 1 в середине периода
    # Если (t % period) < period/2 -> X=0, иначе X=1
    if (t % period) < (period / 2):
        X[i] = 0
    else:
        X[i] = 1

# ------------------------------------------------------
# 3. Задержки логических элементов и формирование сигналов V1, V2, F
# ------------------------------------------------------
# Допустим, у нас есть два логических элемента с задержками d1 и d2
d1 = 0.5e-3  # 0.5 мс
d2 = 1.0e-3  # 1.0 мс

# Функция для сдвига сигнала на задержку delay (простая модель)
def delayed_signal(input_signal, time_array, delay):
    """
    Возвращает сигнал, сдвинутый во времени на 'delay'.
    Для упрощения используем линейный поиск по времени.
    """
    output = np.zeros_like(input_signal)
    for i, t in enumerate(time_array):
        # Индекс, соответствующий моменту (t - delay)
        shifted_t = t - delay
        if shifted_t < 0:
            # До «начала» — считаем, что сигнал 0 (или можно взять первое значение)
            output[i] = 0
        else:
            # Находим ближайший индекс
            # Можно использовать более точный метод (интерполяцию),
            # но для примера хватит простого подхода
            idx = np.searchsorted(time_array, shifted_t)
            if idx >= len(input_signal):
                idx = len(input_signal) - 1
            output[i] = input_signal[idx]
    return output

V1 = delayed_signal(X, T, d1)
V2 = delayed_signal(X, T, d2)

# Допустим, выходная функция F = V1 AND V2 (логическое И)
# Учтём, что V1, V2 — это 0 или 1, тогда:
F = (V1 * V2).astype(float)  # умножение 0*0=0, 1*1=1, 1*0=0 и т.д.

# ------------------------------------------------------
# 4. Визуализация временных диаграмм
# ------------------------------------------------------
fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

axs[0].plot(T*1e3, X, label='X (Вход)')
axs[0].set_ylabel('Амплитуда')
axs[0].set_title('Входной сигнал X')
axs[0].grid(True)
axs[0].legend()

axs[1].plot(T*1e3, V1, label='V1')
axs[1].set_ylabel('Амплитуда')
axs[1].set_title('Сигнал V1 (задержка = 0.5 мс)')
axs[1].grid(True)
axs[1].legend()

axs[2].plot(T*1e3, V2, label='V2', color='orange')
axs[2].set_ylabel('Амплитуда')
axs[2].set_title('Сигнал V2 (задержка = 1.0 мс)')
axs[2].grid(True)
axs[2].legend()

axs[3].plot(T*1e3, F, label='F = V1 AND V2', color='red')
axs[3].set_xlabel('Время (мс)')
axs[3].set_ylabel('Амплитуда')
axs[3].set_title('Выходная функция F')
axs[3].grid(True)
axs[3].legend()

plt.tight_layout()
plt.show()
