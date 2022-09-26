# Guia 3: MANIPULACION DE ARCHIVOS

#Ej 1: Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no 
# empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

import os, glob

def empieza_con(letra, archivo):
    suma = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print ("Hay", suma, "archivos que no empiezan con", letra)


# Ej 2: Escribí un programa que lea un archivo e imprima las primeras n líneas.

def leer_imprimir (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[: primeras_lineas]
    print(*linea)

leer_imprimir ("tejer.txt", 4)

# Ej 3: Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def leer_imprimir_ultimas (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[-primeras_lineas:]
    print(linea) #sin el asterico la impirme como una lista 

leer_imprimir_ultimas("tejer.txt", 4)

#Ej 4: Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def leer_palabras_imprimir (archivo):
    palabras = 0
    with open (archivo, "r") as file:
        for line in file:
            palabras += 1
            for i in line:
                if i == " ":
                    palabras += 1
    print("la cantidad es:", palabras)
leer_palabras_imprimir("tejer.txt")

str = "Programming is fun"

# Use split to decompose str into words
# delimiters are assumed to be white space characters
words = str.split()

print("Words count:", len(words))  # Words count: 3


#Ej 5: Escribí un programa que lea un archivo, reemplace una letra por esa misma letra
#más un salto de línea y lo guarde en otro archivo.
""""
def leer_reemplazar_saltar (archivo):
     with open (archivo, "r") as f, open(salida, "w") as s:
        for line in f:
            s.write(line.replace (letra, letra + "\n"))
leer_reemplazar_saltar("documento", "documento2", f)
"""

# Ej 6: strip() str.replace()

# Ej 7 Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir # y decir cuantos caracteres tiene.

def start_with(letra, archivo):
    count = 0
    with open(archivo,"r") as file:
            for line in file:
                    if (line[0] != letra.lower() or line [0] != letra.upper()):
                        count +=1
    print ("el numero de lineas que no empiezan con", letra, "es", count)
start_with("H", "documento")


#Ejercicio 10: escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y 
#los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
# ejercicio de parcial.

def unir_txt(carpeta1, nombre):
    #carpeta1 es la ruta a esa carpeta
    os.chdir(carpeta1)
    textos = glob.glob("*.txt")
    with open ("resultado/" + nombre, "a") as salida:
        for archivo in textos:
            with open (archivo, "r") as texto:
                salida.write(texto.read() + "\n")

# unir_txt(ruta, nombre)

