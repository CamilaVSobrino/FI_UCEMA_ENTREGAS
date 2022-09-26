# EJERCICIOS DE REPASO PARCIAL 1 POO
class Perro:
    def __init__(self):
        self._alimento = 0          #Creo que el estado es alimento y caricias
        self._caricias = 0          # Interfaz: energia, comer, acariciar, estaDebil

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

# Ej.2 Modificá volar Golondrina, no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, km):
    if (10 + km < self.energia):
        self.energia -= 10 + km
    else:
        print("no puedo volar esta distancia")
  def esta_feliz(self):
    return self.energia >= 500

# Ej. 3: clase Notebook estado: marca, modelo y precio, que le aplique un descuento al precio,tiene que recibir un número entero 
# (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. 
# Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.
# un getter nos devuelve un valor en el mismo momento

class Notebook:
    def __init__(self, marca, modelo, precio):       #son parametros, los estados son los self.algo
        self.marca = marca                           #aca use el mismo nombre para atributo y marca pero podemos usar otro nombre
        self.modelo = modelo                         #si yo paso un string pongo esto sino si es una variable que voy a inicializar en 0, 
        self.precio= precio                          #no pongo todo esto de self.algo

    def descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje/100)
    
    def precioActual(self):     #Creo un metodo getter, para obtener el valor en el momentos
        return self.precio 

# instanciamos: nombre de la variable igual nombre del objeto y los parametros.
#instanciar es usar el objeto digamos, el objeto se crea recien cuando instanciamos, osea, cuando lo usamos

notebook1 = Notebook ("asus", "RRust", 25000)
notebook1.descuento(50)
print (notebook1.precioActual())    # si no tiene argumentos le pongo parentesis si o si

#Ej. 4:
class Contador:
    def __init__(self, valor):
        self.valor = valor
    
    def inc(self):
        self.valor += 1
    
    def reset(self):
        self.valor = 0
    
    def valorActual(self):
        print(self.valor)
    
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor 

# EJ.5  --> Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando
#  que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o 
# "actualización" (para cuando se coloca un valor nuevo). 
# El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de 
# comandos dicha en el ejercicio anterior debería ser "disminución".
#copiar

# tenes que tener la misma cantidad de getters para la cantidad de atributos
#getter metodo que devuelve el valor de un metodo en atributo en particular (creo que es el print final)
# 1 atributo 1 setter
# =! para los setters es un metodo que modifica o asigna un valor a ese atributo

# EJ. 7 --> Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas 
# como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). 
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar,
#  por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando 
# solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez 
# la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, 
# los coeficientes deben ser None(ya que no se puede dividir en cero). 
# Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

# ¿Comparten interfaz o o? si pero parte de la interfaz, el perro tiene interfaz pasear pero el gato no.
# ¿Son polimorficas? necesitas una tercera para saberlo, le puede mandar mensajes tanto a uno como a otro porque
# comparten parte de la interfaz. Somo me importa si puedo mandar el mensaje, despues si el mensaje esta bien 
# ejecutado no me importa porque no lo veo.
#ejercicio perro

# PARCIAL TITANES
# salud siempre esta
# segundo el getter
# los metodos
# cuando hablo de proporcional, caunque sea con comma
