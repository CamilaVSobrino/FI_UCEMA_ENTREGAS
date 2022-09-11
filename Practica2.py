#Guia 2 - INTRODUCCION PARTE 2 

#Ej 1: Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula

cadena_por_teclado = input("Cadena: ")
if cadena_por_teclado[0] == cadena_por_teclado[0].upper:
    print("la primer letra es mayuscula")
else:
    print("la primer letra es minuscula")

#Ej 2: Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

numero = int(input("inserte numero: "))
numero_par = (numero % 2) == 0
numero_impar = (numero % 2) != 0
numero_pos = numero > 0
numero_neg = numero < 0
if numero_par and numero_pos:
    print("el numero es positivo y par")
elif numero_impar and numero_pos:
    print("el numero es positivo e impar")
elif numero_neg and numero_par:
    print("el numero es negativo y par")
else:
    print("el numero es negativo e impar")

#Ej 3: Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. 
# Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.
# la cara opuesta del 6 es el 1, la del 5 es el 2 y la del 4 es el 3.
# se podria resolver con 7 - el dado pero no se me ocurrio.
numero = int(input("ingrese un numero: "))
if numero == 1:
    print("6")
elif numero == 2:
    print("5")
elif numero == 3:
    print(4)
elif numero == 4:
    print("3")
elif numero == 5:
    print("2")
elif numero == 6:
    print("1")
else:
    print("numero incorrecto ingresado")

#Ej 4: El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Costo/gramo.
# paquetes con un peso superior a 5 kg no son transportados, l cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

Zona_entrega = int(input("Ingrese destino de entrega: "))
Gramos_entrega = int(input("Peso del paquete en gramos: "))

if Gramos_entrega < 5000:
    if Zona_entrega == 1:
        print("El valor de la entrega es de:", Gramos_entrega * 10)
    elif Zona_entrega == 2:
        print("El valor de la entrega es de:", Gramos_entrega * 15)
    elif Zona_entrega == 3:
        print("El valor de la entrega es de:", Gramos_entrega * 18)
    elif Zona_entrega == 4:
        print("El valor de la entrega es de:", Gramos_entrega * 24)
    elif Zona_entrega == 5:
        print("El valor de la entrega es de:", Gramos_entrega * 30)
    else:
        print("No esta dentro de la zona de envios")
else:
    print("Exceso de peso")

#Ej 5:Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
# Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

numero_dia = int(input("Inserte numero de dia: "))
if numero_dia <= 7 and numero_dia > 0:
    if numero_dia == 1:
        print("El dia es lunes")
    elif numero_dia == 2:
        print("El dia es martes")
    elif numero_dia == 3:
        print("El dia es miercoles")
    elif numero_dia == 4:
        print("El dia es jueves")
    elif numero_dia == 5:
        print("El dia es viernes")
    elif numero_dia == 6:
        print("El dia es sabado")
    else:
        print("El dia es domingo")
else:
    print("Numero incorrecto")


# LISTAS
# Ej. 6: Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
# Recordá que la manera de copiar una lista en otra es: lista2 = list(lista1)

lista = input(" 5 caracteres: ")
lista2 = lista[::-1]
print(lista2)

#Ej. 7: Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. 
# Una vez hecho esto se deben imprimir los elementos de la lista
#PREGUNTAR

#Ej. 8: Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 
# (es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)

# lista1= [1,2,3,4,5]
# lista2 = [6,7,8,9,10]
# lista3 = [7,9,11,12,15] 
# tiene que ser el resultado, la suma de posicion a posicion en las dos listas. 
# hay que usar range con un for,  y lo puedo usar porque ambas listas tienen LA MISMA LONGITUD 
# voy recorriendo las posiciones o un rango, no una lista.

lista1 = []
lista2 = []
lista3 = []

for indice in range(5):
    lista1.append(int(input("Introduce un numero entero lista 1: ")))
for indice in range(5):
    lista2.append(int(input("Introduce un numero entero lista 2: ")))
for indice in range(5):
    lista3.append(lista1[indice] + lista2 [indice])
print(lista3)

# Ej. 9: Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad 
# de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). 
# Al finalizar se deben mostrar los siguientes datos:
# La edad máxima de todos los alumnos.
# Los alumnos que tengan la edad máxima


