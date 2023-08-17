import pandas as pd
import os

def extract_from_csv(archivo):
    dataframe = pd.read_csv(archivo)
    return dataframe

def extract(ruta_datos):
    data = extract_from_csv(ruta_datos)

    return data

def transform(ruta_datos):
    data = pd.read_csv(ruta_datos)
    
    data.drop(columns = ['ID', 'Dream Weight'], inplace = True)

    gender_dummy = pd.get_dummies(data['Gender'], prefix='Gender', drop_first = True)
    data = pd.concat([data, gender_dummy], axis=1).drop(columns = ['Gender'])

    
    weather_dummy = pd.get_dummies(data['Weather Conditions'], prefix='Weather Conditions', drop_first = True)
    data = pd.concat([data, weather_dummy], axis=1).drop(columns = ['Weather Conditions'])

    return data

def load(data):
    archive_path = 'PR2\PR2\Datos'
    csv_path = 'datos_transformados'
    output_path = os.path.join(archive_path, csv_path)

    data.to_csv(output_path, index = "False")
    return output_path

def tuberia_de_datos(ruta_datos):
    datos_crudos = extract(ruta_datos)
    datos_trans = transform(datos_crudos)
    carga = load(datos_trans)

    return carga