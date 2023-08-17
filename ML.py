import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error

def to_dataframe(data): #Cargando la base de datos
    df = pd.read_csv(data)

    return df

def separacion(data): #Separacion de datos para poder comparar las calorias quemadas con el ejercicio
    objetivo = data['Calories Burn']
    caracteristicas = data.drop(columns = ['Calories Burn', 'Exercise'])
    
    X_train, X_test, y_train, y_test = train_test_split(caracteristicas, objetivo, test_size = .3, random_state = 0)

    return X_train, X_test, y_train, y_test

def entrenamiento(train1, train2):
    modelo = MLPRegressor(hidden_layer_sizes=(10, 2), random_state=1, activation='relu')

    # Entrenando el modelo
    modelo.fit(train1, train2)

    return modelo

def evaluacion(model, test1, test2): #Funcion del modelo para empezar el test
    y_eval = model.predict(test1)
    score = mean_absolute_error(test2, y_eval)

    return score

def clasificacion(data):
    dataframe = to_dataframe(data)
    X_train, X_test, y_train, y_test = separacion(dataframe)
    modelo = entrenamiento(X_train, y_train)
    eval = evaluacion(modelo, X_test, y_test)

    return eval
