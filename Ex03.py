# Importação das bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# 3. Músicas mais dançantes e mais energéticas apresentam maior popularidade?
# Variáveis: danceability, energy, popularity

# Calcula a correlação entre as variáveis
correlacao = df[['danceability', 'energy', 'popularity']].corr()

# Exibe a correlação de cada característica com a popularidade
print('Correlação com a popularidade:')
print(correlacao['popularity'].drop('popularity'))

# Cria gráficos de dispersão
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico de dançabilidade e popularidade
sns.scatterplot(
    data=df,
    x='danceability',
    y='popularity',
    alpha=0.3,
    ax=axes[0]
)

axes[0].set_title('Dançabilidade x Popularidade')
axes[0].set_xlabel('Dançabilidade')
axes[0].set_ylabel('Popularidade')

# Gráfico de energia e popularidade
sns.scatterplot(
    data=df,
    x='energy',
    y='popularity',
    alpha=0.3,
    ax=axes[1]
)

axes[1].set_title('Energia x Popularidade')
axes[1].set_xlabel('Energia')
axes[1].set_ylabel('Popularidade')

plt.tight_layout()
plt.show()