### Ejercicio 1: Escribí un programa que verifique si un string tiene al menos un carácter permitido.
#  Estos caracteres son a-z, A-Z y 0-9.
"""""
import re
def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9.9]",string))
print("el string", "ABCDEaaa1234", "tiene caracteres permitidos?")

print(caracteres_permitidos(ABCDEaaa1234))

###Ejercicio2:
def caracteres_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9.9]",string))
print("el string", "ABCDEaaa1234", "tiene caracteres permitidos?")

print(caracteres_permitidos(ABCDEaaa1234))

###Ejercicio3 (*significa 0 o mas veces)

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("a"))

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("a"))

def encontrar_patron (string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:   #el search devuelve un objeto <re.match objet; span=(), match= >
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("he"))
print(encontrar_patron("hheeeeey"))

###Ejercicio 4

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$" # el mas es que aparezca una o mas veces, el signo peso es para delimitar cuando termina y el piquito para arriba onde empieza.
    if re.search(patron,string) is not None:
        return "patron encontrado"
    else:
        return "Patron no encontrado"
print(palabras_unidas("aaab_bagdad"))

def palabras_unidas(string):
    patron = "[a-z]+\.+.+[a-z]+" #Ejemplo que significa: caracteres de a a z mas de una vez, mas un punto y despues lo que quiera y despues un punto y despues un patron de la a a la z una o mas veces-
# .* significa 0 mas veces

###Ejercicio5
def numero_especifico(numero, string):
    if re.match(str(numero), string) is not None:
        return "Empieza con el numero"
    else:
        return "NO empieza con el numero"
print(numero_especifico(5, "5sdfgf"))

###Ejercicio 6  Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada

def frase_dada(string):
    list = [a,b,c,d]
    if re.match(list(), string) is not None:
        return "Se encuentran en la frase"
    else:
        return "NO se encuentran en la frase"
print(frase_dada(a, "Holacamila"))

###Ejercicio 7  Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
def encuentro_string(string):
    patron = [[a-zA-Z0-9.9]]
    if re.match(, string) is not None:
        return "Se encuentran en la frase"
    else:
        return "NO se encuentran en la frase"
print(encuentro_string(a, "Holacamila"))

"""
