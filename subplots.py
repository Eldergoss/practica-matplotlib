import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Datos para las gráficas
x = np.linspace(0, 5, 11)
y = x**2

#subplot
plt.subplot(1,2,1)
"""

    plt.subplot: Divide la figura en un conjunto de subgráficos (rejilla).
        Argumentos (1, 2, 1):
            1: Número de filas en la rejilla (en este caso, una fila).
            2: Número de columnas en la rejilla (en este caso, dos columnas).
            1: Índice del subgráfico donde se dibujará el gráfico actual (primer gráfico).

Resultado: Se prepara el espacio para dibujar el primer gráfico en la primera posición de una rejilla de 1 fila y 2 columnas.
"""
plt.plot(x,y, "r--")
plt.subplot(1,2,2)
plt.hist(y)
plt.show()#con show visualizamos la grafica 

