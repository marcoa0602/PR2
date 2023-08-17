import pandas as pd
from ETL import tuberia_de_datos
from ML import clasificacion

url = 'https://drive.google.com/uc?id=1dnvro-P6hLJQ07oWBjFWXdTv6KLTxzkk'

tuberia = tuberia_de_datos(url)

score = clasificacion(tuberia)
print(score)