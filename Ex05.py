# Importação das bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Leitura do dataset
df = pd.read_csv('SpotifyTracksDataset.csv')


# 5. Existe uma duração de música associada a uma popularidade média maior?
# Variáveis: duration_ms, popularity

# Converte a duração de milissegundos para minutos
df['duration_min'] = df['duration_ms'] / 60000

# Cria faixas de duração das músicas
df['faixa_duracao'] = pd.cut(
    df['duration_min'],
    bins=[0, 2, 3, 4, 5, float('inf')],
    labels=['Até 2 min', '2 a 3 min', '3 a 4 min',
            '4 a 5 min', 'Mais de 5 min']
)

# Calcula a popularidade média de cada faixa de duração
popularidade_duracao = df.groupby(
    'faixa_duracao', observed=False
)['popularity'].mean()

# Exibe os resultados
print('Popularidade média por duração:')
print(popularidade_duracao)

# Identifica a faixa com maior popularidade média
maior_faixa = popularidade_duracao.idxmax()
maior_media = popularidade_duracao.max()

print('\nFaixa de duração com maior popularidade média:', maior_faixa)
print(f'Popularidade média: {maior_media:.2f}')

# Cria um gráfico de barras
plt.figure(figsize=(10, 5))

sns.barplot(
    x=popularidade_duracao.index,
    y=popularidade_duracao.values
)

plt.title('Popularidade Média por Faixa de Duração')
plt.xlabel('Duração da música')
plt.ylabel('Popularidade média')
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()