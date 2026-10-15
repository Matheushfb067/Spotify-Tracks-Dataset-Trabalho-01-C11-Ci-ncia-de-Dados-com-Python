'''
10. Os fatores associados à popularidade são os mesmos em todos os gêneros musicais?
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ds_spotify = pd.read_csv("SpotifyTracksDataset.csv")

dados = ds_spotify[["track_genre", "popularity", "danceability", "energy", "valence", "acousticness", "instrumentalness"]]

# Calcula as correlações entre as variáveis numéricas dentro de cada gênero
correlacoes_genero = dados.groupby("track_genre").corr(numeric_only=True)

# Seleciona a correlação de cada fator com popularity, por gênero
correlacoes_popularidade = (correlacoes_genero["popularity"].unstack(level=0).drop(index="popularity").T)

print("Correlação dos fatores com a popularidade por gênero musical:")
print(correlacoes_popularidade.round(2))

plt.figure(figsize=(10, 24))
sns.heatmap(data=correlacoes_popularidade, cmap="coolwarm", center=0, vmin=-1, vmax=1)

plt.title("Correlação dos fatores com a popularidade por gênero")
plt.xlabel("Fator musical")
plt.ylabel("Gênero musical")
plt.tight_layout()
plt.show()
