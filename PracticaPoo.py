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

