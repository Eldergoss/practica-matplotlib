import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta del archivo CSV
ruta_csv = "/home/david/Documentos/pypokemtrics/precios de nov 151.csv"

# Leer los datos desde el CSV
df = pd.read_csv(ruta_csv)

#print(df)
#seleccion de cateegorias
categorias = df['Nombre']
valor = df['Precio']

#print(df.columns)

#print(f'aqui va el eje Y {categorias}')
#print(f'aqui va el eje Y {valor}')


#inicializar el barh plot
x = categorias
y = valor

plt.barh(x, y)
plt.show()
