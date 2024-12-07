import matplotlib.pyplot as plt

# Datos
categorias = ['Categoría A', 'Categoría B', 'Categoría C']  # Nombres de las categorías
valores = [10, 20, 15]  # Valores correspondientes a cada categoría

# Crear la gráfica de barras horizontal con color personalizado
plt.barh(categorias, valores, color='#282a36')  # Usando el código hexadecimal para el color 'dracula'

# Añadir título
plt.title('Gráfico de Barras Horizontal Básico', fontsize=16)

# Etiquetas de los ejes
plt.xlabel('Valor')
plt.ylabel('Categoría')

# Mostrar la gráfica
plt.show()
