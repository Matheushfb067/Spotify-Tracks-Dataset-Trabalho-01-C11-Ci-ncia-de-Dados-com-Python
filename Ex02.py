# Importação das bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# 2. Quais características musicais apresentam maior associação com a popularidade?
# Variáveis: popularity, danceability, energy, valence, acousticness,
# instrumentalness, speechiness, loudness e tempo

# Seleciona as variáveis da questão
variaveis = [
    'popularity',
    'danceability',
    'energy',
    'valence',
    'acousticness',
    'instrumentalness',
    'speechiness',
    'loudness',
    'tempo'
]

# Calcula a correlação entre as variáveis
correlacao = df[variaveis].corr()

# Exibe a correlação de cada característica com a popularidade
correlacao_popularidade = correlacao['popularity'].drop('popularity')
correlacao_popularidade = correlacao_popularidade.sort_values(
    ascending=False
)

print('Correlação das características com a popularidade:')
print(correlacao_popularidade)

# Cria um gráfico de barras com as correlações
plt.figure(figsize=(10, 6))

sns.barplot(
    x=correlacao_popularidade.values,
    y=correlacao_popularidade.index
)

plt.title('Correlação das Características Musicais com a Popularidade')
plt.xlabel('Coeficiente de correlação')
plt.ylabel('Características musicais')
plt.axvline(x=0, color='black', linewidth=1)
plt.tight_layout()
plt.show()

# Cria um mapa de calor com as correlações entre todas as variáveis
plt.figure(figsize=(10, 8))

sns.heatmap(
    correlacao,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlação entre Popularidade e Características Musicais')
plt.tight_layout()
plt.show()