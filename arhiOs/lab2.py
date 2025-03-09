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


##Версия 2:
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def meandr(time_impulse, time_model, time_step):
#     '''
#     Функция формирования массива точек для построения графика меандра
#     с фиксацией моментов переключения между логическими 0 и 1
#     time_impulse - длительность импульса в мкс;
#     time_step - шаг по времени;
#     time_model - длительность моделирования.
#
#     '''
#     x = np.arange(0, time_model - time_step, time_step)
#     num_points = len(x)
#     trig = False
#     y = [0] * num_points
#     z = [0]
#     k = 0
#     for i in range(num_points):
#         if k == time_impulse:
#             trig = not trig
#             z.append(x[i])
#             k = 0
#         if not trig:
#             y[i] = 0
#         else:
#             y[i] = 1
#         k += 1
#     return x, y, z
#
#
# # задаем настройки общего полотна с 7-ю подграфиками
# fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, figsize=(16, 14), sharex=False, sharey=True)
# fig.tight_layout(pad=3.0)  # отступ между подграфиками
# fig.supylabel('Логический 0/1', x=0, fontsize=16)  # подпись общего графика по оси Y
# fig.supxlabel('Время, мкс', fontsize=16)  # подпись общего графика по оси X
#
# plt.yticks([0, 1])
#
# # вычисляем значения массивов сигналов; массив z - это точки момента переключения сигналов a1 и a2 между 0 и 1
# x1, y1, z1 = meandr(10, 0.001, 0.000001)
# x2, y2, z2 = meandr(20, 0.001, 0.000001)
# x3, y3, z3 = meandr(40, 0.001, 0.000001)
# x4, y4, z4 = meandr(80, 0.001, 0.000001)
# x5, y5, z5 = meandr(160, 0.001, 0.000001)
# x6, y6, z6 = meandr(320, 0.001, 0.000001)
#
# # формируем сигналы E1, E2, E3, E4 с учетом логическиой схемы, как логическое умножение a1 и a2 с учетом инверсии
# ey1 = list((np.ones(len(y5)) - np.array(y5)) * (np.ones(len(y6)) - np.array(y6)))
# ey1 = ey1[:2] + ey1[:-2]  # сдвигаем результат вправо на время задержки (имитация задержки сигнала)
# ey2 = list((np.ones(len(y5)) - np.array(y5)) * (np.array(y6)))
# ey2 = ey2[:2] + ey2[:-2]
# ey3 = list(np.array(y5) * (np.ones(len(y6)) - np.array(y6)))
# ey3 = ey3[:2] + ey3[:-2]
# ey4 = list(np.array(y5) * np.array(y6))
# ey4 = ey4[:1] + ey4[:-1]  # задержка = 1мкс, так как нет инверсии сигнала
#
# # формируем результат работы мультиплексора как логическая сумма результатов логического умножения соответ. сигналов X и E
# f = list((np.array(ey1) * np.array(y1)) + (np.array(ey2) * np.array(y2)) + (np.array(ey3) * np.array(y3)) + (
#             np.array(ey4) * np.array(y4)))
# f = f[:2] + f[:-2]  # задержка = 2мкс (элемент И + элемент ИЛИ)
#
# # построение графиков функции
# ax1.set_title("Сигнал X1", fontdict={'fontsize': 14, 'color': 'black'}, loc='left')
# ax1.set_xticks(z5)  # ось X строим по моментам переключения сигнала a1 (для удобства сравнения)
# ax1.plot(x1, y1)  # сигнал X
# ax1.plot(x1, ey1)  # сигнал E
#
# ax2.set_title("Сигнал X2", fontdict={'fontsize': 14, 'color': 'black'}, loc='left')
# ax2.set_xticks(z5)
# ax2.plot(x2, y2)
# ax2.plot(x2, ey2)
#
# ax3.set_title("Сигнал X3", fontdict={'fontsize': 14, 'color': 'black'}, loc='left')
# ax3.set_xticks(z5)
# ax3.plot(x3, y3)
# ax3.plot(x3, ey3)
#
# ax4.set_title("Сигнал X4", fontdict={'fontsize': 14, 'color': 'black'}, loc='left')
# ax4.set_xticks(z5)
# ax4.plot(x4, y4)
# ax4.plot(x4, ey4)
#
# ax5.set_title("Сигнал a1", fontdict={'fontsize': 14, 'color': 'red'}, loc='left')
# ax5.set_xticks(z5)
# ax5.plot(x5, y5, '-r')
#
# ax6.set_title("Сигнал a2", fontdict={'fontsize': 14, 'color': 'red'}, loc='left')
# ax6.set_xticks(z6)
# ax6.plot(x6, y6, '-r')
#
# ax7.set_title("Сигнал F (выход)", fontdict={'fontsize': 14, 'color': 'green'}, loc='left')
# ax7.set_xticks(z5)
# ax7.plot(x6, f, '-g')  # график сигнала F
# ax7.plot(x6, y5, '-.c', alpha=0.8)  # накладываем сразу a1
# ax7.plot(x6, y6, '-.r', alpha=0.8)  # накладываем сразу a2
#
# plt.show()