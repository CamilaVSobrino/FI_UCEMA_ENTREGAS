import re
""""
texto = "Estamos aprendiendo a usar expresiones regulares"

patron = "usar"
#utilizo el metodo de re que busca (search)

print(re.search(patron,texto))
# orden de patron y texto
print(texto[22:26])

#Ejemplo de search
print("este es el resultado de aplicar spam",resultado.spam())  
print("este es el resultado de aplicar start", resultado.start())
print("este es el resultado de aplicar end", resultado.end())
print("este es el resultado de aplicar group", resultado.group())


# el piqyuito lo puedo usar para buscar la palabra on la ue empieza la oracion, puede ser principio de patron o de la liena
resultado = re.findall("^Estamos", texto)

print(resultado)


#que hace match solo da si esta en el principio

import re
texto = "amet lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
 print(re.search(patron, texto).group())
 print(re.match(patron, texto))
 Expresiones regualres de python
 lorem = r "[a - z]{5}"
 r significa que es una expresion regular

#ejercicio de parcial bajar texto y bucar cosas con expresiones regulares. ej saber si el telefono es de capital  cordonba o el mail. 

#print(re.search(r"[a-z]{5}", texto).group())

#resultado = re.search(r"[a-z]{5}", texto).group()
#todos_los_resultados = re.findall(r"[a-z]{5}", texto)
#print(resultado)
#print (todos_los_resultados)

# Probar si da y de lo contrario imprimi esto

try:
    print(re.search(patron, texto).group())
except:
    print("ya termino la clase")
""""