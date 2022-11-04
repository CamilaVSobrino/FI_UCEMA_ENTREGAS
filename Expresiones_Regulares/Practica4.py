# GUIA 4: EXPRESIONES REGULARES

.* significa "Cualquier cosa"
import re
# Ej 1: verifique si un string tiene al menos un carácter permitido, estos son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]",string))

print(caracteres_permitidos("ABCDEaaa1234"))

# Ej 2: verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9.9]",string))

print(caracteres_permitidos("ABCDEaaa1234"))

# Ej 3:

def encontrar_patron(string):
    patron = "he*"          #string dado tiene una h seguida de ninguna o más e.(*significa 0 o mas veces)
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("a"))

def encontrar_patron(string):
    patron = "he+"  #string dado tiene una h seguida de una o más e
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("a"))

def encontrar_patron (string):
    patron = "he{2,3}"  #string dado tiene una h seguida de dos o tres e.
    if re.search(patron, string) is not None:            #el search devuelve un objeto <re.match objet; span=(), match= >
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("he"))
print(encontrar_patron("hheeeeey"))

# Ej 4: palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$" # + = aparezca una o mas veces, el $ =  cuando termina y el ^ donde empieza.
    if re.search(patron,string) is not None:
        return "patron encontrado"
    else:
        return "Patron no encontrado"
print(palabras_unidas("aaab_bagdad"))

def palabras_unidas(string):
    patron = "[a-z]+\.+.+[a-z]+" #Ej: caracteres de a a z mas de una vez, mas un punto y despues lo que quiera y despues un punto y despues un patron de la a a la z una o mas veces-


#Ej 5:  diga si un string empieza con un número específico.

def numero_especifico(numero, string):
    if re.match(str(numero), string) is not None:
        return "Empieza con el numero"
    else:
        return "NO empieza con el numero"
print(numero_especifico(5, "5sdfgf"))

# Ej 6: dada una lista de strings verifique si se encuentran en una frase dada

def frase_dada(string):
    list = ["a","b","c","d"]
    if re.match(list(), string) is not None:
        return "Se encuentran en la frase"
    else:
        return "NO se encuentran en la frase"
print(frase_dada("a", "Holacamila"))

# Ej 7: encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

def encuentro_string(string):
    patron = ["\w+\s+"]
    if re.match(patron, string) is not None: 
        return "Se encuentran en la frase"
    else:
        return "NO se encuentran en la frase"
print(encuentro_string("a", "Holacamila"))

# Ej 8: que separe y devuelva los caracteres númericos de un string.

def separar(string):
    numeros = re.findall(r'\d+', string)
    print("Los números de", string,"son:",*numeros)

separar('string')

# Ej 9:  extraiga los caracteres que estén entre guiones en un string.

def extraer(string):
    caracteres = re.findall("[-\]+[a-z]+[\-]", string)  #acordarme de la \
    print(caracteres)

extraer("hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

# Ej 10: Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

def delimitados (string):
    caracteres = re.findall ("[\@|\&]+[\w]+[\@|\&]", string)  #ver.
    print (caracteres)
delimitados('jajaja$jajaj$jaj&ja&jejeje')

#Ej 11: dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima.
# (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

def verificar_imprimir(lista):
    for string in lista:
        palabras = re.findall('[P][\w]+', string)
        if len(palabras) == 2:
            print (palabras)

verificar_imprimir(["Práctica Python", "Práctica C++", "Práctica Fortran"])

#Ej 12: reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|)

def reemplazar_ocurrencias (string):
    como_nuevo = re.sub('[\s|\_|\:]', '|', string)  #el | para separar dentro del corchete
    print(como_nuevo)
reemplazar_ocurrencias('hola_camila :como_estas')

#Ej 13: reemplace los dos primeros caracteres no alfanúmericos por guiones bajos

def reemplazar_dos(string):
    reemplazado = re.sub('[\W]{2,}', '_', string)
    print(reemplazado)
reemplazar_dos('$$camila')

#Ej 14: reemplace los espacios y tabulaciones por punto y coma.

def reemplazar_esp(string):
    reemplazado_pto = re.sub('[\s]',';',string)
    print(reemplazado_pto)
reemplazar_esp('    camila sobrino')    #ver si el tab tiene que representar muchos ;;;;; o solo 1

#Ej 15: validar si una cuenta de mail está escrita correctamente.

def escrito_correcto(string):
    if re.search('[a-zA-Z0-9_\.\-]+[@][a-z]+[\.][a-z]{2,}', string) is not None: 
        return "El mail esta correctamente escrito"
    else:
        return "No esta correctamente escrito"

print(escrito_correcto('camusobrino@gmail.com'))



