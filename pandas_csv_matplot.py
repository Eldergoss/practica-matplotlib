import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv('/home/david/Documentos/pypokemtrics/Main/data/processed/excel/top 10 paradox rif.csv')

# Revisar las columnas del DataFrame para asegurarse de que los nombres sean correctos
print(df.head())  # Muestra las primeras filas para verificar las columnas

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
plt.bar(df["nombre"], df["ventas"], color="skyblue", label="Precios Anuales")

# Personalizar el gráfico
plt.title('Top 10 Precios - Paradox Rift', fontsize=16)
plt.xlabel('Cartas', fontsize=12)
plt.ylabel('Precio (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje X para mayor legibilidad
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
