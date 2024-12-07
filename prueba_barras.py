import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4]
height = [5, 7, 3, 4]

# Crear el gráfico de barras
plt.bar(x, height, 
        width=0.6, 
        color='skyblue', 
        edgecolor='black', 
        linewidth=1.2, 
        align='center', 
        label='Ventas 2024')

# Personalización de los ejes y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Ejemplo')
plt.legend()

# Mostrar el gráfico
plt.show()
