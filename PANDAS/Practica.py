# Ej3: 
import pandas as pd
dict1 ={"a": 10, "b": 20, "c": 30, "d": 40, "e":50}

nueva_serie= pd.Series(dict1)
print(nueva_serie)

#Ej1:
ser1 = [3, 7, 12, 15, 21]
ser2 = [1, 4, 10, 14, 19]

ds1 = pd.Series(ser1)
ds2 = pd.Series(ser2)

print("Suma: ")
print(ds1 + ds2)
print("\nResta")
print(ds1 - ds2)
print("\nmultiplicacion")
print(ds1 *ds2)
print ("\division")
print(ds1/ds2)

#Ej4: Realizá un programa para crear y mostrar un DataFrame a partir de un diccionario y de unas etiquetas (o labels).

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

result = pd.DataFrame(datos_ejemplo)
print(result)

# Ej6: Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#4 de dos en dos empezando en 0 o el 1 --> RANGE