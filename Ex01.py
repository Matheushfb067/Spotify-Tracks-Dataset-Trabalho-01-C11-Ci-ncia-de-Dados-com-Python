# Importação das bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# 1. Quais gêneros musicais apresentam a maior e a menor popularidade média?
# Variáveis: track_genre, popularity

# Calcula a popularidade média de cada gênero
popularidade_media = df.groupby('track_genre')['popularity'].mean()

# Encontra o gênero com maior popularidade média
maior_genero = popularidade_media.idxmax()
maior_media = popularidade_media.max()

# Encontra o gênero com menor popularidade média
menor_genero = popularidade_media.idxmin()
menor_media = popularidade_media.min()

# Exibe os resultados
print('Gênero com maior popularidade média:', maior_genero)
print(f'Popularidade média: {maior_media:.2f}')

print('\nGênero com menor popularidade média:', menor_genero)
print(f'Popularidade média: {menor_media:.2f}')

# Cria um gráfico comparando os dois gêneros
plt.figure(figsize=(8, 5))

sns.barplot(
    x=[maior_genero, menor_genero],
    y=[maior_media, menor_media]
)

plt.title('Maior e Menor Popularidade Média por Gênero')
plt.xlabel('Gênero musical')
plt.ylabel('Popularidade média')
plt.show()