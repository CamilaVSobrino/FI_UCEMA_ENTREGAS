########Guia 1:
###Ejercicio 1: escribir un programa que imprima la longitud de un string el cual se lee por teclado. 
# Primero sacar longitud de string,

"""
def imprimir_longitud (palabra):
    longitud = len (palabra)
    print (longitud)

imprimir_longitud ("Camila")
"""

###Ejercicio 2: realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayuscula 
#(Asegurarse de que el string tenga la cantidad de caracteres suficientes).

"""
def quinta_sexta(palabra):
    ####restringir palbras con menos de 6.
    longitud = len(palabra)
    if (longitud > 5):
        ####Consguir 5ta y 6ta letra.
        quinta = palabra[4].upper()
        sexta = palabra[5].upper()
        print(quinta)
        print(sexta)
    else:
        print("invalid word")    

quinta_sexta("camila") """

###Ejercicio 3: escribir un programa que pregunte el nombre y apellido al usuario y lo salude.
"""
def pregunta():
    nombre = input('Teclear nombre completo: ')
    print (f"saludos {nombre}")
    
"""
###Ejercicio 4: pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayusculas

"""
def pregunta():
    nombre = input('Teclear nombre: ')
    apellido = input('Teclear apellido: ')
    primera_N = nombre[0].upper()
    primera_A  = apellido[0].upper()
    nombre[0] = primera_N
    apellido[0] = primera_A
    print(nombre)
    print(apellido)

pregunta()
"""
###Ejercicio 5: realizar un programa que lea tres numeros por teclado y calcule el promedio de ellos.
"""
def lector():
    numero1 = int(input('Numero 1: '))
    numero2 = int(input('Numero 2: '))
    numero3 = int(input('Numero 3: '))
    promedio = (numero1+numero2+numero3)/3

    print(promedio)
lector() """

###Ejercicio 6: dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuantas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

"""
def contador():
    minutos = int(input('cuantos minutos: '))
    hora = minutos/60
    resto = minutos%60  #el porcentaje sirve para ver el resto o lo que sobra
    
    print (f"Son {hora} horas y {resto} minutos ")
    

contador()    
"""

###Ejercicio 7: un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comision por cada venta que realiza. 
# Realizar un programa que devuelva el dinero que recibira por comision luego de 4 ventas y el total de dinero que ganara ese mes, 
# teniendo en cuenta estas ventas y su sueldo base.
"""
def total_dinero():
    sueldo = 1000
    comision = (1000*10)/100
    cuatro_comision = (comision)*4
    total_sueldo = int(cuatro_comision) + int(sueldo)

    print(total_sueldo)
total_dinero() 
"""

###Ejercicio 8: escribir un programa para calcular la nota final de un estudiante, 
# teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, 
# por cada incorrecta se le resta 1 punto y si la respuesta esta en blanco no se le suma ni se le resta.
"""

def nota_final():
    respuestas_correcta = int(input('Cuantas correctas: '))
    respuestas_incorrecta = int(input('Cuantas incorrectas: '))
    respuestas_blanco = int(input('Cuantas en blanco: '))
    contador = 4*respuestas_correcta - respuestas_incorrecta
    
    print (contador)    

nota_final()

"""
#######Guia 2
"""""
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

#######Guia 3

###Ejercicio 1: Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no 
#empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

import os, glob

def empieza_con(letra, archivo):
    suma = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print ("Hay", suma, "archivos que no empiezan con", letra)



###Ejercicio 2 Escribí un programa que lea un archivo e imprima las primeras n líneas.

def leer_imprimir (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[: primeras_lineas]
    print(*linea)

leer_imprimir ("tejer.txt", 4)

# Ejercicio 3 Escribí un programa que lea un archivo, guarde las líneas del 
# archivo en una lista y luego imprima las n últimas.

def leer_imprimir_ultimas (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[-primeras_lineas:]
    print(linea) #sin el asterico la impirme como una lista 

leer_imprimir_ultimas("tejer.txt", 4)

#Ejercicio 4 Hacé un programa que lea un archivo, cuente la cantidad de 
# palabras del archivo y luego imprima el resultado.

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


#Ejercicio 5 Escribí un programa que lea un archivo, reemplace una letra por esa misma letra
#más un salto de línea y lo guarde en otro archivo.

def leer_reemplazar_saltar (archivo):
     with open (archivo, "r") as f, open(salida, "w") as s:
        for line in f:
            s.write(line.replace (letra, letra + "\n"))
leer_reemplazar_saltar("documento", "documento2", f)

"""""
###Ejercicio 6: strip() str.replace()

###Ejercicio 7 Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir 
# y decir cuantos caracteres tiene.
