# N°4. debe crear una nueva carpeta en la  posición actual llamada _Resultado_ y, por otro, que lea todos los archivos con extensión `.txt` 
# y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*, que tiene que estar 
# dentro de la carpeta _Resultado_. **NO se pueden usar rutas absolutas**
# ruta_relativa = os.path.join("Documentos", "UCEMA", "Fundamentos", "Práctica4", "archivo.txt")
# >>> print(ruta_relativa)
"""
import os, glob

def crear():
    os.mkdir('_Resultado_')
    lista_archivos = glob.glob("*.txt")
    for archivo in lista_archivos:

        with open(archivo, "r") as archivo_entrada:
            leer = archivo_entrada.read()

            with open(r"_Resultado_\nuevo_texto.txt", "a") as archivo_salida:
                archivo_salida.write(leer)
    
crear()

#N°1 (RE) Escribir funciones que dado un string, permitan obterner Cuantas veces aparece el string bc9.ej. aparece 2 veces en xsabc9cabcb3sabc9 y ninguna en hola amigos mios. 
#La lista de los substrings delimitadso entre "aa" y "gg" que no inculyan ninguna "c". P.ej. en "ttaatatggttaacatgg", debe tomar solamente "tat", rechazando "cat"

import re

def cuantas_veces(string):
    resultado = re.findall("bc9",string)
    return len(resultado)

def sin_c (string):
    return re.findall("aa([^c]*?)gg", string)


print(sin_c("ttaatatggttaacatgg"))
print(cuantas_veces("xsabc9cabcb3sabc9 "))


#N°3(Manejo de exepciones) Ejecutá el script_misterioso.py y realizá resolvé: 
# 1. ¿Qué tipo de exepción arroja la corrida del script? 
# 2. Mejorá el código para que capture dicho error especificamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error 
# 3. ¿Qué otras excepciones deberias considerar?

#1. ZeroDivisionError
#2. 
def obtener_media(lista):
    sumatoria = 0

    for valor in lista :

        sumatoria += valor
    longitud = len (lista)

    try:
        return sumatoria / longitud
    except ZeroDivisionError:
        print("No se puede dividir por cero")

print(obtener_media([2,3,4]))
"""
# N° 4: debe crear una nueva carpeta en la posición actual llamada Resultado y que lea todos los archivos con extensión . txt y 
# escriba el contenido de todos en un único archivo llamado texto_completo.txt, que tiene que estar dentro de la carpeta Resultado. 
# NO se pueden usar rutas absolutas

import os, glob

def unir_txt():
    os.mkdir("Resultado")           #Creo la carpeta de resultados
    lista_txt = glob.glob ("*.txt") #Armo lista con todos los txt
    salida = open ("Resultado/texto_completo.txt", "a")
    for txt in lista_txt:
        archivo = open (txt, "r")
        salida.write (archivo.read())
        archivo.close()
    salida.close()


#Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor. El prototipo de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 rpm.
#La velocidad del auto se calcula así: *(rpm / 100) * (0.5 + (cambio / 2))*. Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40.
#También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes:

#* Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
#* Si el motor está en primera, entonces se multiplica por 3.
#* Si el motor está en segunda, entonces se multiplica por 2.

#Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.
#El modelo debe entender estos mensajes:

#arrancar() , se pone en primera con 500 rpm.
#subirCambio()
#bajarCambio()
#subirRPM(cuantos)
#bajarRPM(cuantos)
#velocidad()
#consumoActualPorKm(), calcula el consumo actual y lo devuelve

#Al ejecutar esto:

#python
#auto1 = Auto()
#auto1.arrancar()
#auto1.subirRPM(3500)
#auto1.subirCambio()
#auto1.subirCambio()
#auto1.subirCambio()
#auto1.bajarCambio()

#la velocidad debería ser 80 y el consumo 0.15 litros/km.

class Auto():
    def __init__(self):
        self.consumo = 0.05
        self.rpm = 0
        self.cambio = None
    
    def arrancar (self):
        self.cambio = 1
        self.rpm = 500
    
    def subirCambio (self):
        if self.cambio < 5:
            self.cambio +=1

    def bajarCambio (self):
        if self.cambio > 1:
            self.cambio -= 1
    
    def subirRPM (self, cantidad):
        if self.rpm + cantidad <= 5000:
            self.rpm += cantidad
        else:
            self.rpm = 5000

    def bajarRPM (self, cantidad):
        if self.rpm - cantidad >= 0:
            self.rpm -= cantidad
        else:
            self.rpm = 0

    
    def velocidad (self):
        return ((self.rpm / 100)*(0.5 + (self.cambio / 2)))
    
    def consumoActualPorKm (self):
        if self.rpm > 3000:
            if self.cambio == 1:
                return (self.consumo * ((self.rpm - 2500)/ 500) * 3)
            elif self.cambio ==2:
                return (self.consumo * ((self.rpm - 2500)/ 500) * 2)
            elif self.cambio <= 5:
                return (self.consumo * ((self.rpm - 2500)/ 500))
        elif self.cambio == 1:
            return (self.consumo * 3)
        elif self.cambio == 2:
            return (self.consumo * 2)
        else:
            return (self.consumo)
 
 #Si los rpm son menores a 3000 y el auto esta en 3ra, 4ta o 5ta el consumo es el base
 