import pandas as pd

def extract(ruta_datos):
    dataframe = pd.read_csv(ruta_datos) #sta función toma una ruta de archivo como entrada y carga los datos desde ese archivo CSV en un DataFrame de Pandas.

    return dataframe

def transform_gender(dataframe): #Esto hace que gender se vuelva valores numericos y se ponen en diferentes columnas
    dataframe.drop(columns = ['ID', 'Dream Weight'], inplace = True)

    gender_dummy = pd.get_dummies(dataframe['Gender'], prefix='Gender', drop_first = True)
    data = pd.concat([dataframe, gender_dummy], axis=1).drop(columns = ['Gender'])

    return data

def transform_weather(data): #Esto hace que weather se vuelva valores numericos y se ponen en diferentes columnas
    weather_dummy = pd.get_dummies(data['Weather Conditions'], prefix='Weather Conditions', drop_first = True)
    data = pd.concat([data, weather_dummy], axis=1).drop(columns = ['Weather Conditions'])

    return data

def load(data):
    csv_path = 'datos_transformados.csv'
    data.to_csv(csv_path, index=False)
    return csv_path

def tuberia_de_datos(datos):
    datos_crudos = extract(datos)
    datos_trans1 = transform_gender(datos_crudos)
    datos_trans2 = transform_weather(datos_trans1)
    carga = load(datos_trans2)

    return carga