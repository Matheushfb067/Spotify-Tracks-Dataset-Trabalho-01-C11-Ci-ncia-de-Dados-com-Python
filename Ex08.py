'''
8. Existe relação entre o volume percebido da música e sua popularidade? 
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

ds_spotify = pd.read_csv('SpotifyTracksDataset.csv')
print(ds_spotify)

print()

dados = ds_spotify[['popularity', 'loudness']]

# Calculando relação entre volume percebido em DB e popularidade
correlação = dados['loudness'].corr(dados['popularity'])
print(f'Correlação entre volume percebido e popularidade: {correlação:.2f}')

# Cria um dataframe de amostra para plotar o gráfico, limitando a 5000 registros para melhor visualização
amostra = dados.sample(n = min (5000, len(dados)), random_state=42)

# Grafico de dispersão com uma linha de tendência para visualizar a relação entre volume percebido e popularidade
plt.title("Relação entre volume percebido e popularidade das músicas")
plt.xlabel("Volume percebido (dB)")
plt.ylabel("Popularidade")

sns.regplot(
    data = amostra,
    x = 'loudness',
    y = 'popularity',
    line_kws = {'color': 'red'}
)

plt.show()