import re

# Desafios:
#Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
# \d{4,}

#Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
# [a-z]{3,6}

#Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
# ab*

#Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
# texto = 'En la clase de Introducción a la programación hay 30 estudiantes' 
# \d{1} o \d+

# Clase practica
texto = "Estamos aprendiendo a usar expresiones regulares"
patron = "usar"

print(re.search(patron,texto))     #utilizo el metodo de re que busca (search), orden de patron y texto.
print(texto[22:26])

print("este es el resultado de aplicar spam", resultado.spam())  
print("este es el resultado de aplicar start", resultado.start())
print("este es el resultado de aplicar end", resultado.end())
print("este es el resultado de aplicar group", resultado.group())

#el piquito lo uso para buscar la palabra que empieza la oracion, puede ser principio de patron o de la linea.
resultado = re.findall("^Estamos", texto)
print(resultado)

texto = "amet lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"

print(re.search(patron, texto).group())
print(re.match(patron, texto))
 
lorem = r"[a - z]{5}"   #r significa que es una expresion regular

print(re.search(r"[a-z]{5}", texto).group())

resultado = re.search(r"[a-z]{5}", texto).group()
todos_los_resultados = re.findall(r"[a-z]{5}", texto)
print(resultado)
print (todos_los_resultados)

# Probar si da y de lo contrario imprimi esto
try:
    print(re.search(patron, texto).group())
except:
    print("ya termino la clase")