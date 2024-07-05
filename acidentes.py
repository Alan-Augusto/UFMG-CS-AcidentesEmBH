import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


# geometrias = [Point(float(x), float(y)) for x, y in zip(acidentes['COORDENADA_X'], acidentes['COORDENADA_Y'])]
# gdf_acidentes = gpd.GeoDataFrame(acidentes, geometry=geometrias)

FILEPATH = './data/si-bol-20'
DATAINICIAL = 12
DATAFINAL = 22

def carregarAcidentesTotais():

    acidentesTotais = pd.DataFrame()

    # passar por todas as datas:
    for i in range(DATAINICIAL, DATAFINAL+1):
        acidentes = pd.read_csv(f'{FILEPATH}{i}.csv', delimiter=';', encoding='ISO-8859-1')

        acidentes.columns = acidentes.columns.str.strip()

        acidentesTotais = pd.concat([acidentesTotais, acidentes])

    return acidentesTotais


# Carrega os dados dos semáforos e dos acidentes
acidentesTotais = carregarAcidentesTotais()

# Colocar os dados em um arquivo csv
acidentesTotais.to_csv('./data/acidentesTotais.csv', index=False)


# print(acidentesTotais.head())

# mostrar quantidade de linhas coletadas:
print(f'Quantidade de acidentes coletados: {len(acidentesTotais)}')