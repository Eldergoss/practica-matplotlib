import matplotlib.pyplot as plt
import numpy as np

# Datos para las gráficas
x = np.linspace(0, 5, 11)
y = x**2

# Gráfico de línea (cuadrática)
plt.plot(x, y)
plt.title("Gráfico Lineal de x^2")
plt.xlabel("x")
plt.ylabel("y = x^2")
plt.show()
