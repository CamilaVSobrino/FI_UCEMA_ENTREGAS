# Guia 3: MANIPULACION DE ARCHIVOS

import os , glob

# Ej 1: lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (ej:"P").

def empieza_con(letra, archivo):
    suma = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print ("Hay", suma, "archivos que no empiezan con", letra)

empieza_con('C', "tejer.txt")

# Ej 2: lea un archivo e imprima las primeras n líneas.

def leer_imprimir (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[: primeras_lineas]
    print(*linea)

leer_imprimir ("tejer.txt", 4)

# Ej 3:lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def leer_imprimir_ultimas (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[-primeras_lineas:]
    print(linea)            #sin el asterico la impirme como una lista 

leer_imprimir_ultimas("tejer.txt", 4)

#Ej 4: lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def contar_palabras(archivo):
    file = open(archivo,'r')        #opern, read, split
    leer = file.read()
    dividir = leer.split()  # Use split to decompose str into words, delimiters are assumed to be white space characters
    print('El archivo tiene', len(dividir), 'palabras')
contar_palabras('tejer.txt')

#Ej 5: lea un archivo, reemplace una letra por esa misma más un salto de línea y lo guarde en otro archivo.

def reemplazar(entrada, salida, letra):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for line in file:
            file2.write(line.replace(letra, letra + '\n'))  #Reemplazo y lo escribo en el nuevo archivo
reemplazar('texto1.txt', 'texto2.txt', 'n')

# Ej 6: lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo

def sin_saltos(entrada, salida):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for letra in file.read():
            if letra == '\n':
                pass
            else:
                file2.write(letra)
sin_saltos('texto1.txt', 'texto2.txt')

# Ej 7: lea un archivo e identifique la palabra más larga, debe imprimir, decir cuantos caracteres tiene.

def palabra_larga(archivo):
    file = open(archivo,'r') # abro
    leer = file.read()       # leo
    dividir = leer.split()   # separa en palabras
    larga = ''               # El espacio es 1 caracter
    for palabra in dividir:
        if len(palabra) > len(larga):
            larga = palabra
    print('La palabra mas larga es', larga, 'con', len(larga), 'letras')

palabra_larga('tejer.txt')

#Ej 8: abra dos documentos y guarde el contenido de ambos en un otro documento ya existente

def juntar(archivo1, archivo2, archivo3):
    with open(archivo1, 'r') as file, open(archivo2, 'r') as file2, open(archivo3, 'w') as file3:
        file3.write(file.read())    #en el 3 agregro lo de los dos 
        file3.write(file2.read())
juntar('texto1.txt','texto2.txt','texto3.txt')     

#Ej 9: lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# (Recordá que la frecuencia es la relación entre veces que aparece con respecto a la cantidad total)

def frecuencia(archivo):
    with open(archivo, 'r') as file:    #Lo abro para leer
        palabras = file.read()          #Amo la logica de leer y separar y guardar
        lista = palabras.split()
        dic = {}
        for palabra in lista:
            dic[palabra] = int(lista.count(palabra)) / int(len(lista))
        print(dic)

frecuencia('tejer.txt')

#Ej 10:lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

def unir_txt(Carpeta1, nombre):
    os.chdir(Carpeta1)               #cambiamos de directorio a la Carpeta 1
    textos = glob.glob('*.txt')      #Busco todos los txt y armo una lista automatica
    os.mkdir('Resuelto')            #Creo un directorio en la capeta donde estoy
    with open('Resuelto/' + nombre, 'a') as salida: #tengo que poner resuelto/ para que se dirija hacia alla.
        for archivo in textos:
            with open(archivo, 'r') as texto:
                salida.write(texto.read() + '\n')
unir_txt('Carpeta1', 'archivo2.txt')
