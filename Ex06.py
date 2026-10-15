'''
6. Músicas com maior valência musical apresentam popularidade diferente das 
músicas com menor valência? 
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

ds_spotify = pd.read_csv('SpotifyTracksDataset.csv')
print(ds_spotify)

print()

# Pegando a coluna de valencia e popularidade 
dados = ds_spotify[['valence', 'popularity']]

# Divide a valência em dois grupos: alta e baixa, com base na mediana
mediana = dados['valence'].median()
print(f"Mediana da valência: {mediana}")

# Para cada musica se a valencia for maior ou igual a mediana, ela será classificada como 'Alta Valência', caso contrário, 'Baixa Valência'
dados['grupo_valencia'] = np.where(dados['valence'] >= mediana, 'Alta Valência', 'Baixa Valência')

medias = dados.groupby('grupo_valencia')['popularity'].mean()

media_alta = medias['Alta Valência']
media_baixa = medias['Baixa Valência']
diferenca = media_alta - media_baixa

print(f"Média de popularidade para músicas com alta valência: {media_alta:.2f}")
print(f"Média de popularidade para músicas com baixa valência: {media_baixa:.2f}")
print(f"Diferença de popularidade: {diferenca:.2f}")

# Criando um gráfico de dispersão para visualizar a relação entre valência e popularidade
sns.boxplot(data=dados, x='grupo_valencia', y='popularity')
plt.title('Relação entre Valência Musical e Popularidade')
plt.xlabel('Grupo de Valência')
plt.ylabel('Popularidade')
plt.show()