import matplotlib.pyplot as plt

# Datos
categorias = ['Categoría A', 'Categoría B', 'Categoría C']
valores1 = [10, 20, 15]
valores2 = [25, 30, 35]

# Crear la gráfica de barras horizontal
bars1 = plt.barh(categorias, valores1, color='lightblue', label='Serie 1')
bars2 = plt.barh(categorias, valores2, color='lightgreen', label='Serie 2')

# Añadir título y etiquetas
plt.title('Comparación de dos series de datos', fontsize=16, color='darkblue', fontweight='bold')
plt.xlabel('Valores', fontsize=14, color='gray')
plt.ylabel('Categorías', fontsize=14, color='gray')

# Añadir la leyenda
plt.legend(
    loc='upper left',           # Ubicación de la leyenda
    fontsize=12,                # Tamaño de la fuente
    title='Datos',              # Título de la leyenda
    frameon=True,               # Cuadro alrededor de la leyenda
    borderpad=1,                # Espaciado alrededor del cuadro
    labelspacing=1.2,           # Espaciado entre las etiquetas
    borderaxespad=1.5,          # Espaciado entre la leyenda y el gráfico
    shadow=True                 # Sombra en la leyenda
)

# Añadir las etiquetas sobre las barras
for bar in bars1:
    plt.text(
        bar.get_width() + 0.5,               # Posición horizontal
        bar.get_y() + bar.get_height() / 2,  # Posición vertical (centro de la barra)
        f'{bar.get_width()}',                # Texto (valor de la barra)
        va='center',                         # Alineación vertical
        ha='left',                           # Alineación horizontal
        fontsize=10                           # Tamaño de la fuente
    )

for bar in bars2:
    plt.text(
        bar.get_width() + 0.5,               # Posición horizontal
        bar.get_y() + bar.get_height() / 2,  # Posición vertical (centro de la barra)
        f'{bar.get_width()}',                # Texto (valor de la barra)
        va='center',                         # Alineación vertical
        ha='left',                           # Alineación horizontal
        fontsize=10                           # Tamaño de la fuente
    )

# Añadir grillas
plt.grid(
    which='both',           # Mostrar tanto grillas mayores como menores
    axis='x',               # Grillas solo en el eje X
    color='gray',           # Color de las líneas
    linestyle='--',         # Estilo de línea discontinua
    linewidth=0.5           # Grosor de la línea
)

# Añadir una anotación
plt.annotate(
    'Máximo valor de la Serie 2',          # Texto de la anotación
    xy=(35, 1),                           # Ubicación de la anotación en las coordenadas
    xytext=(40, 1.5),                     # Posición del texto
    textcoords='data',                    # Tipo de coordenadas
    arrowprops=dict(facecolor='red', shrink=0.05),  # Propiedades de la flecha
    fontsize=12,                           # Tamaño de la fuente
    color='blue'                           # Color del texto
)

# Ajustar el espaciado de la gráfica
plt.tight_layout()

# Mostrar la gráfica
plt.show()


import matplotlib.pyplot as plt

# Datos
categorias = ['Categoría A', 'Categoría B', 'Categoría C']  # Nombres de las categorías
valores = [10, 20, 15]  # Valores correspondientes a cada categoría

# Crear la gráfica de barras horizontal
plt.barh(categorias, valores, color='lightblue')  # Creamos la gráfica de barras horizontales con color lightblue

# Quitar el título
plt.title('', fontsize=16)  # Dejamos el título vacío para eliminarlo. Se podría mantener uno con texto si fuera necesario.

# Quitar las etiquetas del eje X e Y
plt.xlabel('')  # Eliminar etiqueta del eje X
plt.ylabel('')  # Eliminar etiqueta del eje Y

# Quitar la leyenda
plt.legend([], loc='best')  # Si no queremos leyenda, usamos un arreglo vacío en lugar de etiquetas.

# Quitar los ticks de los ejes X e Y
plt.xticks([])  # Eliminar las marcas (ticks) del eje X
plt.yticks([])  # Eliminar las marcas (ticks) del eje Y

# Quitar la grilla
plt.grid(False)  # Desactivar la grilla del gráfico

# Quitar los bordes de los ejes
plt.gca().spines['top'].set_visible(False)    # Desactivar el borde superior
plt.gca().spines['right'].set_visible(False)  # Desactivar el borde derecho
plt.gca().spines['left'].set_visible(False)   # Desactivar el borde izquierdo
plt.gca().spines['bottom'].set_visible(False) # Desactivar el borde inferior

# Mostrar la gráfica
plt.show()  # Mostrar el gráfico generado

import matplotlib.pyplot as plt

# Datos
categorias = ['Categoría A', 'Categoría B', 'Categoría C']  # Nombres de las categorías
valores = [10, 20, 15]  # Valores correspondientes a cada categoría

# Crear la gráfica de barras horizontal
plt.barh(categorias, valores, color='lightblue')  # Creamos la gráfica de barras horizontales con color lightblue

# Quitar el título
plt.title('', fontsize=16)  # Dejamos el título vacío para eliminarlo. Se podría mantener uno con texto si fuera necesario.

# Quitar las etiquetas del eje X e Y
plt.xlabel('')  # Eliminar etiqueta del eje X
plt.ylabel('')  # Eliminar etiqueta del eje Y

# Quitar la leyenda
plt.legend([], loc='best')  # Si no queremos leyenda, usamos un arreglo vacío en lugar de etiquetas.

# Quitar los ticks de los ejes X e Y
plt.xticks([])  # Eliminar las marcas (ticks) del eje X
plt.yticks([])  # Eliminar las marcas (ticks) del eje Y

# Quitar la grilla
plt.grid(False)  # Desactivar la grilla del gráfico

# Quitar los bordes de los ejes
plt.gca().spines['top'].set_visible(False)    # Desactivar el borde superior
plt.gca().spines['right'].set_visible(False)  # Desactivar el borde derecho
plt.gca().spines['left'].set_visible(False)   # Desactivar el borde izquierdo
plt.gca().spines['bottom'].set_visible(False) # Desactivar el borde inferior

# Mostrar la gráfica
plt.show()  # Mostrar el gráfico generado
