'''
5. Músicas mais curtas são realmente mais populares ou existe uma faixa de 
duração que se destaca em relação às demais?
'''

import pandas as pd
import matplotlib.pyplot as plt

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# Separando as musicas por duracao
grupo1 = df[df['duration_ms'] < 120000]
grupo2 = df[(df['duration_ms'] >= 120000) & (df['duration_ms'] < 180000)]
grupo3 = df[(df['duration_ms'] >= 180000) & (df['duration_ms'] < 240000)]
grupo4 = df[(df['duration_ms'] >= 240000) & (df['duration_ms'] < 300000)]
grupo5 = df[df['duration_ms'] >= 300000]

# Calculando a popularidade media
media1 = grupo1['popularity'].mean()
media2 = grupo2['popularity'].mean()
media3 = grupo3['popularity'].mean()
media4 = grupo4['popularity'].mean()
media5 = grupo5['popularity'].mean()

print('Popularidade média por duração:')
print('Menos de 2 min:', media1)
print('De 2 a 3 min:', media2)
print('De 3 a 4 min:', media3)
print('De 4 a 5 min:', media4)
print('5 min ou mais:', media5)

# Organizando os resultados
duracoes = ['< 2 min', '2-3 min', '3-4 min', '4-5 min', '5+ min']
medias = [media1, media2, media3, media4, media5]

# Grafico de popularidade por duracao
plt.figure(figsize=(10, 5))
plt.bar(duracoes, medias, color='blue')
plt.title('Popularidade média por duração das músicas')
plt.xlabel('Duração das músicas')
plt.ylabel('Popularidade média')
plt.show()