import numpy as np
import matplotlib.pyplot as plt

# Входные сигналы X1-X4 (по приоритету: X1 > X2 > X3 > X4)
inputs = [
    (0, 0, 0, 0),  # Нет сигналов (EO = 1)
    (1, 0, 0, 0),  # Только X1 активен (A1A0 = 00)
    (0, 1, 0, 0),  # Только X2 активен (A1A0 = 01)
    (0, 0, 1, 0),  # Только X3 активен (A1A0 = 10)
    (0, 0, 0, 1),  # Только X4 активен (A1A0 = 11)
    (1, 1, 0, 0),  # X1 и X2 активны (A1A0 = 00, приоритет X1)
    (0, 1, 1, 0),  # X2 и X3 активны (A1A0 = 01, приоритет X2)
    (0, 0, 1, 1),  # X3 и X4 активны (A1A0 = 10, приоритет X3)
    (1, 0, 0, 1),  # X1 и X4 активны (A1A0 = 00, приоритет X1)
    (1, 1, 1, 1),  # Все активны (A1A0 = 00, приоритет X1)
]

x1_vals, x2_vals, x3_vals, x4_vals = [], [], [], []
a1_vals, a0_vals, eo_vals = [], [], []

for x1, x2, x3, x4 in inputs:
    x1_vals.append(x1)
    x2_vals.append(x2)
    x3_vals.append(x3)
    x4_vals.append(x4)

    if x1:
        a1, a0 = 0, 0
    elif x2:
        a1, a0 = 0, 1
    elif x3:
        a1, a0 = 1, 0
    elif x4:
        a1, a0 = 1, 1
    else:
        a1, a0 = 0, 0

    eo = 1 if not (x1 or x2 or x3 or x4) else 0

    a1_vals.append(a1)
    a0_vals.append(a0)
    eo_vals.append(eo)

# Визуализация
fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
time = np.arange(len(inputs))

axes[0].step(time, x4_vals, label="X4", linewidth=2, color='purple')
axes[0].step(time, x3_vals, label="X3", linewidth=2, color='orange')
axes[0].step(time, x2_vals, label="X2", linewidth=2, color='blue')
axes[0].step(time, x1_vals, label="X1", linewidth=2, color='red')
axes[0].legend()
axes[0].set_title("Входные сигналы")

axes[1].step(time, a1_vals, label="A1", linewidth=2, color='red')
axes[1].scatter(time, a1_vals, color='r')
axes[1].legend()

axes[2].step(time, a0_vals, label="A0", linewidth=2, color='green')
axes[2].scatter(time, a0_vals, color='g')
axes[2].legend()

axes[3].step(time, eo_vals, label="EO", linewidth=2, color='blue')
axes[3].scatter(time, eo_vals, color='b')
axes[3].legend()

axes[3].set_xlabel("Комбинация входов")
plt.tight_layout()
plt.show()