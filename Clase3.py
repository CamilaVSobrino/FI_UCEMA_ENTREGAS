import re
texto = "Estamos aprendiendo a usar expresiones regulares"
patron = "usar"

print(re.search(patron,texto))      #utilizo el metodo de re que busca (search), orden de patron y texto.
print(texto[22:26])

print("este es el resultado de aplicar spam",resultado.spam())  
print("este es el resultado de aplicar start", resultado.start())
print("este es el resultado de aplicar end", resultado.end())
print("este es el resultado de aplicar group", resultado.group())

# el piquito lo puedo usar para buscar la palabra on la que empieza la oracion, puede ser principio de patron o de la linea.
resultado = re.findall("^Estamos", texto)
print(resultado)

texto = "amet lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"

print(re.search(patron, texto).group())
print(re.match(patron, texto))
#Expresiones regualres de python
 
lorem = r "[a - z]{5}"
#r significa que es una expresion regular

#Ej. parcial bajar texto y bucar cosas con expresiones regulares.Saber si el telefono es de capital o cordonba. 

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
