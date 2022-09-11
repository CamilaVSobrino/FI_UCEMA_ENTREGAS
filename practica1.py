#Guia 1 - INTRODUCCION PARTE 1 
#Ej 1:escribir un programa que imprima la longitud de un string.

def imprimir_longitud (palabra):
    longitud = len (palabra)
    print (longitud)
imprimir_longitud ("Camila")
imprimir_longitud("Sobrino")

#Ej 2: realizar un programa donde se imprima la 5ta y 6ta letra EN MAYUSCULA (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

def quinta_sexta(palabra):
    longitud = len(palabra)
    if (longitud > 5):      #Restringir palbras con menos de 6. Consguir 5ta y 6ta letraen MAYUSCULA
        quinta = palabra[4].upper()    
        sexta = palabra[5].upper()
        print(quinta)
        print(sexta)
    else:
        print("invalid word")    
quinta_sexta("camila") 
quinta_sexta ("sobrino")

#Ej 3: escribir un programa que pregunte el nombre y apellido al usuario y lo salude.

nombre = input('Ingresar nombre y apellido: ')
print (f"saludos {nombre}")

#Ej 4: pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayusculas

nombre = input('Teclear nombre: ')
apellido = input('Teclear apellido: ')
print(nombre[0].upper(),apellido[0].upper() )

#Ej 5: realizar un programa que lea tres numeros por teclado y calcule el promedio de ellos.

numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
numero3 = int(input('Numero 3: '))
print((numero1+numero2+numero3)/3)

#Ej 6: dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuantas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.


minutos = int(input('Ingrese minutos: '))
hora = minutos/60
resto = minutos%60  #el porcentaje sirve para ver el resto o lo que sobra
print (f"Son {hora} horas y {resto} minutos ")


#Ej 7: un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comision por cada venta que realiza. 
# Realizar un programa que devuelva el dinero que recibira por comision luego de 4 ventas y el total de dinero que ganara ese mes, 
# teniendo en cuenta estas ventas y su sueldo base.

sueldo = int(input("ingrese sueldo: "))
comision = (sueldo*10)/100
cuatro_comision = (comision * 4)
total_sueldo = int(cuatro_comision) + int(sueldo)
print(total_sueldo)


#Ej 8: escribir un programa para calcular la nota final de un estudiante, correcta x 4 puntos,  incorrecta se le resta 1 punto y si la respuesta esta en blanco nada.

respuestas_correcta = int(input('Cuantas correctas: '))
respuestas_incorrecta = int(input('Cuantas incorrectas: '))
respuestas_blanco = int(input('Cuantas en blanco: '))
contador = 4*respuestas_correcta - respuestas_incorrecta
print (contador)    

#Ej Grupal: 

costo_total= int(input('Valor de la casa: '))
porcentaje_deposito = costo_total/4
cantidad_ahorrada = 0
g = 4
sueldo_anual =int(input('Sueldo anual: '))
porcentaje_ahorrado = int(input('Cuanto queres ahorrar: '))
sueldo_mensual = sueldo_anual/12

ahorro_mensual = sueldo_mensual * (porcentaje_ahorrado / 10)
mes = 0
while porcentaje_deposito > cantidad_ahorrada:
    mes += 1
    cantidad_ahorrada += ahorro_mensual + (cantidad_ahorrada * g / 12)
else:
    print('Tenes que ahorar por', mes, 'meses')

