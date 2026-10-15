'''
9. Quais gêneros musicais apresentam os maiores e menores valores médios de 
andamento (BPM)?
'''

import matplotlib.pyplot as plt
import pandas as pd

ds_spotify = pd.read_csv('SpotifyTracksDataset.csv')
print(ds_spotify)

print()

dados = ds_spotify[['track_genre', 'tempo', 'popularity']]

# Calculando a média de andamento (BPM) para cada gênero musical
medias = dados.groupby('track_genre')['tempo'].mean().sort_values()
print(f'Médias de andamento por gênero musical: \n{medias.round(2)}')

print()

medias = medias.sort_values()

# Identificando os gêneros com os maiores e menores valores médios de andamento
maior_genero = medias.idxmax()
menor_genero = medias.idxmin()

print(f"Menor média: {menor_genero} — {medias.min():.2f} BPM")
print(f"Maior média: {maior_genero} — {medias.max():.2f} BPM")

# medias deve conter a média de tempo para cada track_genre
extremos = pd.concat([medias.nsmallest(5), medias.nlargest(5)])

# Criando gráfico de barras para os gêneros com os maiores e menores valores médios de andamento
plt.bar(extremos.index, extremos.values, color='blue')

plt.title("Gêneros com menores e maiores andamentos médios")
plt.xlabel("Andamento médio (BPM)")
plt.ylabel("Gênero musical")
plt.show()