import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico
x = np.linspace(0, 5, 11)  # Valores en el rango [0, 5], con 11 puntos
y = np.sin(x)  # Función seno de x

# Crear la figura y los ejes
fig, axes = plt.subplots(2,2)

# Graficar los datos
axes.plot(x, y, "b", label="Seno(x)")  # Línea azul con etiqueta

# Personalizar el gráfico
axes.set_title("Gráfico de Seno", fontsize=14)  # Título
axes.set_xlabel("x", fontsize=12)  # Etiqueta del eje x
axes.set_ylabel("Seno(x)", fontsize=12)  # Etiqueta del eje y
axes.legend()  # Mostrar la leyenda

# Mostrar el gráfico
plt.show()
