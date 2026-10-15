'''
7. Músicas com conteúdo explícito apresentam popularidade diferente das músicas 
sem conteúdo explícito?
'''

import matplotlib.pyplot as plt
import pandas as pd

ds_spotify = pd.read_csv('SpotifyTracksDataset.csv')
print(ds_spotify)

print()

dados = ds_spotify[['explicit', 'popularity']]

# Calculando a popularidade media para músicas explícitas e não explícitas
medias = dados.groupby('explicit')['popularity'].mean()

medias.index = ['Não Explícitas', 'Explícitas']
print(f'Popularidade média por grupo: \n{medias.round(2)}')

# Criando grafico de barras 
# medias.index = rotulos para o eixo x e medias.values para o eixo y
plt.bar(medias.index, medias.values, color=['blue', 'orange'])

plt.title('Popularidade média de músicas explícitas e não explícitas')
plt.xlabel('Conteudo Explícito')
plt.ylabel('Popularidade Média')
plt.show()