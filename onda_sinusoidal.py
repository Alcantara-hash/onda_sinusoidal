import numpy as np
import matplotlib.pyplot as plt
import math

opcion = input("¿Quieres usar seno o coseno? ")
opcion = opcion.lower()

if opcion == "seno":
    funcion_trig = np.sin
elif opcion == "coseno":
    funcion_trig = np.cos
else:
    print("Opción inválida. Se usará seno por defecto.")
    funcion_trig = np.sin

amplitudes = input("Ingresa los valores pico (amplitudes) de las ondas sinusoidales separados por espacios: ")
amplitudes = amplitudes.split()
amplitudes = [float(a) for a in amplitudes]

desfases_grados = [90, 180, 270, 360]
desfases = [math.radians(d) for d in desfases_grados]

frecuencia = 1.0

tiempo_inicio = 0.0
tiempo_final = 5.0
paso_tiempo = 0.01

fig, ax = plt.subplots()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

for i, amplitud in enumerate(amplitudes):
    desfase = desfases[i] if i < len(desfases) else 0.0

    tiempo_actual = np.arange(tiempo_inicio + i, tiempo_final + i, paso_tiempo)

    valores_onda = amplitud * funcion_trig(2 * np.pi * frecuencia * tiempo_actual + desfase)
    ax.plot(tiempo_actual, valores_onda)
