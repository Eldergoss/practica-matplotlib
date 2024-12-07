import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico
x = np.linspace(0, 5, 11)  # Valores en el rango [0, 5], con 11 puntos
y = np.sin(x)  # Función seno de x

# Crear la figura y los ejes (una matriz 2x2 de gráficos)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Graficar en cada subgráfico (individualmente)
axes[0, 0].plot(x, y, "b", label="Seno(x)")
axes[0, 0].set_title("Gráfico de Seno")
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("Seno(x)")
axes[0, 0].legend()

# Opcional: llenar los demás subgráficos con algo diferente o dejarlos vacíos
axes[0, 1].plot(x, np.cos(x), "g--", label="Coseno(x)")
axes[0, 1].set_title("Gráfico de Coseno")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("Coseno(x)")
axes[0, 1].legend()

axes[1, 0].plot(x, np.tan(x), "r", label="Tangente(x)")
axes[1, 0].set_title("Gráfico de Tangente")
axes[1, 0].set_xlabel("x")
axes[1, 0].set_ylabel("Tangente(x)")
axes[1, 0].legend()

# Dejar un subgráfico vacío
axes[1, 1].axis("off")  # Desactiva el cuarto gráfico

# Ajustar los espacios entre subgráficos
plt.tight_layout()

# Mostrar el gráfico
plt.show()
