'''
4. Músicas acústicas ou instrumentais apresentam popularidade diferente das músicas mais convencionais?
'''

# Importação das bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# Calcula a correlação entre as variáveis
correlacao = df[
    ['acousticness', 'instrumentalness', 'popularity']
].corr()

# Exibe a correlação com a popularidade
print('Correlação com a popularidade:')
print(correlacao['popularity'].drop('popularity'))

# Cria os gráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico de acústica e popularidade
sns.scatterplot(
    data=df,
    x='acousticness',
    y='popularity',
    alpha=0.3,
    ax=axes[0]
)

axes[0].set_title('Acousticness x Popularidade')
axes[0].set_xlabel('Acousticness')
axes[0].set_ylabel('Popularidade')

# Gráfico de instrumentalidade e popularidade
sns.scatterplot(
    data=df,
    x='instrumentalness',
    y='popularity',
    alpha=0.3,
    ax=axes[1]
)

axes[1].set_title('Instrumentalness x Popularidade')
axes[1].set_xlabel('Instrumentalness')
axes[1].set_ylabel('Popularidade')

plt.tight_layout()
plt.show()