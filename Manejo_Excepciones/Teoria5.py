# Desafios I:

# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d)/(2*a)      #SyntaxError: '(' was never closed
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#Desafio II: nada.

def dividir(num):
    return num / 2
print(dividir(0))
print(dividir(9))

#Desafio III 

def dividir(numero1, numero2):
    try: 
        return numero1 / numero2
    except ZeroDivisionError:
        return "No se puede dividir por cero"

print(dividir(1,0))
print(dividir(9,2))

