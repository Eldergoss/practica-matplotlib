import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos
data = {
    'Game': ['Slither.io (2016)', 'Clash Royale (2016)', 'Draw Something (2012)', 
             'Candy Crush Saga (2013)', 'Pokémon GO (2016)'],
    'Users': [5, 10, 15, 20, 23]
}
df = pd.DataFrame(data)

# Colores personalizados (gris para todos menos Pokémon GO)
colors = ['#bfbfbf', '#bfbfbf', '#bfbfbf', '#bfbfbf', '#a3c100']  # Pokémon GO en verde

# Estilo de Seaborn
sns.set(style="whitegrid")

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(
    data=df, 
    x='Game', 
    y='Users', 
    ax=ax, 
    color=None,  # Usamos None para especificar colores personalizados
    dodge=False
)

# Asignar los colores manualmente
for bar, color in zip(ax.patches, colors):
    bar.set_facecolor(color)

# Títulos
ax.set_title("Pokémon GO is the biggest US mobile game ever", 
             fontsize=14, fontweight='bold', loc='left', pad=20)
ax.text(-0.5, 25, "Peak daily active users (millions)", fontsize=12, va='center')

# Personalizar ejes
ax.set_ylim(0, 25)
ax.set_ylabel("")
ax.set_xlabel("")
ax.set_yticks(range(0, 26, 5))
ax.set_yticklabels(range(0, 26, 5), fontsize=10)
ax.set_xticks(range(len(df['Game'])))
ax.set_xticklabels(df['Game'], fontsize=10, rotation=45, ha='right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Fondo gris claro
ax.set_facecolor('#f2f2f2')

# Etiquetas en la parte superior de cada barra
for i, value in enumerate(df['Users']):
    ax.text(i, value + 0.5, f"{value}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()
