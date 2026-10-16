'''
10. Como variam a dançabilidade, a energia e a valência das músicas pertencentes aos 
cinco gêneros musicais mais populares?
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# Cinco generos mais populares
popularidade = df.groupby('track_genre')['popularity'].mean()
maiores = popularidade.nlargest(5)

print('5 generos mais populares:')
print(maiores)

# Selecionando os cinco generos
dados = df[df['track_genre'] == maiores.index[0]]

for genero in maiores.index[1:]:
    grupo = df[df['track_genre'] == genero]
    dados = pd.concat([dados, grupo])

# Organizando as tres caracteristicas
caracteristicas = dados[['track_genre', 'danceability', 'energy', 'valence']]

# Boxplot unico
sns.boxplot(data=caracteristicas[['danceability', 'energy', 'valence']])
plt.title('Dancabilidade, energia e valencia dos generos mais populares')
plt.xlabel('Caracteristicas musicais')
plt.ylabel('Valores')
plt.show()