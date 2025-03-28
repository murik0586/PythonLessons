import numpy as np
import matplotlib.pyplot as plt

def clock_signal(length, step):
    return np.tile([1, 0], length // 2)

def sdr_signal(data, clock_length):
    signal = []
    for bit in data:
        signal.extend([int(bit)] * 2)  # SDR передает данные на каждом фронте такта
    return np.array(signal[:clock_length])

def ddr_signal(data, clock_length):
    signal = []
    for bit in data:
        signal.append(int(bit))  # DDR передает данные на каждом фронте такта (оба)
    return np.array(signal[:clock_length])

hex_values = ['7A', 'FF', '0F']
binary_values = [bin(int(h, 16))[2:].zfill(8) for h in hex_values]
clock_length = 16  # Длина тактового сигнала
step = 1

clock = clock_signal(clock_length, step)
sdr_signals = [sdr_signal(b, clock_length) for b in binary_values]
ddr_signals = [ddr_signal(b, clock_length) for b in binary_values]

fig, axs = plt.subplots(3, 1, figsize=(10, 6))
axs[0].plot(clock, drawstyle='steps-post', label='Clock')
axs[0].set_title("Синхросигнал")
axs[0].legend()

axs[1].plot(sdr_signals[0], drawstyle='steps-post', label=f'SDR {hex_values[0]}')
axs[1].plot(sdr_signals[1], drawstyle='steps-post', label=f'SDR {hex_values[1]}')
axs[1].plot(sdr_signals[2], drawstyle='steps-post', label=f'SDR {hex_values[2]}')
axs[1].set_title("SDR сигнал")
axs[1].legend()

axs[2].plot(ddr_signals[0], drawstyle='steps-post', label=f'DDR {hex_values[0]}')
axs[2].plot(ddr_signals[1], drawstyle='steps-post', label=f'DDR {hex_values[1]}')
axs[2].plot(ddr_signals[2], drawstyle='steps-post', label=f'DDR {hex_values[2]}')
axs[2].set_title("DDR сигнал")
axs[2].legend()

plt.tight_layout()
plt.show()