def start_with(letra, archivo):
    count = 0
    with open(archivo,"r") as file:
            for line in file:
                    if (line[0] != letra.lower() or line [0] != letra.upper()):
                        count +=1
    print ("el numero de lineas que no empiezan con", letra, "es", count)
start_with("H", "documento")


#ejercicio nro 8 practica 2 de listas
lista1= [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [7,9,11,12,15] #tiene que ser el resultado, la suma de posicion a posicion en las dos listas. 
#hay que usar range con un for,  y lo puedo usar porque ambas listas tienen la mismo longitud, voy recorriendo las posiciones o un rango, no una lista.

#ejercicio 6 parte 2

#Ejercicio 10: escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y 
#los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
# ejercicio de parcial.
import os, glob

def unir_txt(carpeta1, nombre):
    #carpeta1 es la ruta a esa carpeta
    os.chdir(carpeta1)
    textos = glob.glob("*.txt")
    with open ("resultado/" + nombre, "a") as salida:
        for archivo in textos:
            with open (archivo, "r") as texto:
                salida.write(texto.read() + "\n")

unir_txt(ruta, nombre)

