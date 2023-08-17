import pandas as pd
import os

def extract(ruta_datos):
    dataframe = pd.read_csv(ruta_datos)

    return dataframe

def transform_gender(dataframe):
    dataframe.drop(columns = ['ID', 'Dream Weight'], inplace = True)

    gender_dummy = pd.get_dummies(dataframe['Gender'], prefix='Gender', drop_first = True)
    data = pd.concat([dataframe, gender_dummy], axis=1).drop(columns = ['Gender'])

    return data

def transform_weather(data):
    weather_dummy = pd.get_dummies(data['Weather Conditions'], prefix='Weather Conditions', drop_first = True)
    data = pd.concat([data, weather_dummy], axis=1).drop(columns = ['Weather Conditions'])

    return data

def load(data):
    archive_path = 'C:\PR2\PR2\Datos'
    csv_path = 'datos_transformados'
    output_path = os.path.join(archive_path, csv_path)
    output_path = data.to_csv(output_path, index = "False")

    return output_path

def tuberia_de_datos(datos):
    datos_crudos = extract(datos)
    datos_trans1 = transform_gender(datos_crudos)
    datos_trans2 = transform_weather(datos_trans1)
    carga = load(datos_trans2)

    return carga