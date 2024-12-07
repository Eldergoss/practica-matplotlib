import matplotlib.pyplot as plt
import pandas as pd

# Crear DataFrame
df_bar = pd.DataFrame([100, 200, 6000],
                      index=['a', 'b', 'c'],
                      columns=['growth'])

# Configuración de la gráfica
width = 0.8
fig, ax = plt.subplots(figsize=(6, 3))

# Crear el gráfico de barras horizontales
df_bar.plot(kind='barh', legend=False, ax=ax, width=width)
ax.invert_yaxis()

# Ocultar bordes
[spine.set_visible(False) for spine in ax.spines.values()]

# Personalizar las etiquetas
ax.tick_params(axis='y', labelsize='x-large')

# Agregar anotaciones con los valores
vmax = df_bar['growth'].max()
for i, value in enumerate(df_bar['growth']):
    ax.text(value + vmax * 0.02, i, f'{value:,}', fontsize='x-large', 
            va='center', color='darkblue')  # Usar un color válido como 'darkblue'

# Mostrar la gráfica
plt.show()
