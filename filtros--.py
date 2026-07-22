import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# 1. Definición de la señal de entrada
# Creamos una señal compuesta combinando frecuencias y agregando ruido blanco
np.random.seed(0)
T = 2.0          # Segundos de duración
fs = 500.0       # Frecuencia de muestreo (Hz)
t = np.linspace(0, T, int(T * fs), endpoint=False)

# Señal limpia (ej: una onda de 5 Hz combinada con una de 50 Hz)
data = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)
# Agregamos ruido blanco
ruido = np.random.normal(0, 0.5, len(t))
senal_con_ruido = data + ruido

# 2. Diseño del filtro (Filtro Pasa-bajas Butterworth)
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Parámetros del filtro
cutoff_frequency = 15.0  # Frecuencia de corte en Hz
order = 6

# 3. Aplicación del filtro a la señal
senal_filtrada = butter_lowpass_filter(senal_con_ruido, cutoff_frequency, fs, order)

# 4. Visualización de los resultados
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, senal_con_ruido, color='gray', label='Señal con Ruido')
plt.plot(t, data, color='blue', linewidth=1.5, label='Señal Original (Limpia)')
plt.title('Señal antes del filtrado')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, senal_filtrada, color='red', linewidth=1.5, label='Señal Filtrada (Pasa-bajas)')
plt.title('Señal después de aplicar el filtro digital')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
