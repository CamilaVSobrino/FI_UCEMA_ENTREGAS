# Manejo de Excepciones 
# Ej.1 ¿Es correcto el uso del try...except? Si pero no lo estamos utilizando para salvar un error por lo cual no nos sirve 
# en este ejemplo.
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except:
    print("no puedo agregar arroz")

#Ej.2 

def dividir(lista1 , numero_divisor):
    lista2 = []
    for numero in lista1:
        try:
            numero2 = numero/numero_divisor
            lista2.append(numero2)
        except ZeroDivisionError:
            return "No se puede dividir por cero"
    return lista2

print(dividir([2,4,6,8], 2))
print(dividir([2,4,5,6], 0))

def es_positivo (lista1, numero_incierto):
    try:
        if numero_incierto > 0:
            lista1.append(numero_incierto)
        else:
            raise ValueError("es negativo")
    except TypeError:
        "No es un numero"

print(es_positivo([2,3,4], 5))
