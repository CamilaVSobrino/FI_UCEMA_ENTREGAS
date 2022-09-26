import os 

def bio(archivo):
    with open ("bio.txt", "w") as miarch:
        miarch.write("Hola mi nombre es Camila Sobrino")
bio("bio.txt")

def leer_imprimir(archivo):
    with open(archivo, "r") as miarch:
        print(miarch.readlines())

leer_imprimir("manipulacion_archivos.txt")
