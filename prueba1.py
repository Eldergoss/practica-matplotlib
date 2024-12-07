import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame
data = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
        'Ventas': [200, 300, 400, 500]}
df = pd.DataFrame(data)

# Graficar
df.plot(x='Mes',
        y='Ventas',
        kind='bar', #tipo de grafico en este caso es de lineas
        title='Ventas por Mes',
        )#marker='o'
plt.show()
"""
    kind define el tipo de gráfico (bar, line, hist, pie, etc.).
    bins ajusta la cantidad de intervalos en un histograma (más bins = más precisión).
    autopct muestra y personaliza porcentajes en gráficos de pastel.
"""