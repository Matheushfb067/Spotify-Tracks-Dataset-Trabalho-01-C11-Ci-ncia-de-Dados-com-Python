'''
2. O que está mais associado à popularidade de uma música: sua dançabilidade, energia, intensidade 
sonora, acústica ou instrumentalidade?
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')

# Selecionando as caracteristicas musicais
dados = df[['popularity', 'danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness']]

# Calculando as correlacoes
correlacao = dados.corr()

# Correlacao com a popularidade
print('Correlação das características com a popularidade:')
print(correlacao['popularity'])

# Grafico das correlacoes
sns.heatmap(correlacao, annot=True, fmt='.2f')

plt.title('Correlação entre popularidade e características musicais')
plt.show()