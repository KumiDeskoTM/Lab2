import pandas as pd  # Importa la biblioteca pandas
import numpy as np  # Importa la biblioteca numpy

# Carga el archivo CSV llamado games_data.csv
games = pd.read_csv('steam.csv')

print("------Estadisticas descriptivas de las columnas numéricas----------------")
# mostrar las estadisticas descriptivas de las columnas numéricas (media, desviacion estándar, etc.)
print(games.describe())
print("------Tipos de datos de cada columna----------------")

# muestra los tipos de datos de cada columna (int64, float64, object)
print(games.dtypes)

print("------Primeras 5 filas del DataSet----------------")
# Muestra las primeras 5 filas del DataSet
print(games.head())

print("-------Ultimas 5 filas del DataSet---------------")
# Muestra las ultimas 5 filas del DataSet
print(games.tail())
print("----------------------")

GameMedia = games["price"].mean()  # Calcula la media de la columna "price"

GameMediana = games["price"].median()  # Calcula la mediana de la columna "price"

GameEstandar = games["price"].std()  # Calcula la desviación estándar de la columna "price"

print("Media de la columna price:", GameMedia)  # Imprime la media de la columna "price"
print("----------------------")
print("Mediana de la columna price:", GameMediana)  # Imprime la mediana de la columna "price"
print("----------------------")
print("Desviación estándar de la columna price:", GameEstandar)  # Imprime la desviación estándar de la columna "price"
print("----------------------")