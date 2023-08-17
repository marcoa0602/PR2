import pandas as pd

url = 'https://drive.google.com/uc?id=1dnvro-P6hLJQ07oWBjFWXdTv6KLTxzkk'
df_exercise = pd.read_csv(url)
df_exercise

from ETL import tuberia_de_datos

tuberia_de_datos(df_exercise)