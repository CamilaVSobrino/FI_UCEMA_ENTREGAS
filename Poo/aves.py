
class animal_alado:
  def esta_feliz(self):
    return self.energia>= 500


class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_feliz(self):
    return self.energia >= 500

class Dragon(animal_alado): #hereda una clase de la clase madre
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10


pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)


#Creamos a Hipo que es un entrenador de dragones, sabe aceptar dragones, los hace entrenar, 
# haciendolos dar 20 vueltas en circulos y hacer comer su comida favorita hasta saciarse
# Creamos clase entrenador_de_dragones

class Entrenador: #comienza con mayuscula
  def __inint__(self, equipo): #inicializo
    self.equipo = equipo

  def aceptar_dragones (self, dragon):#creo una lista de dragones que tengo en mi equipo o agrego otro parametro
    self.equipo.append (dragon) #modelando un objeto; tengo que saber que tipo de dato es el argumento, si es un nro por ej no va a entender las funciones de un dragon.

  def entrenar_dragon(self, dragon): #lo hago dar 20 vueltas
    for vueltas in range(20): #en un rango de 0 a 20 (ejecuta esto 20 veces)
      dragon.volar_en_circulos()
    dragon.comer_peces(3)   #lo saco del bucle for sino cada vez que de 20 vueltas comeria 3 peces.

  def entrenar_equipo(self):
    for dragon in self.equipo:
      self.entrenar_dragon(dragon)


#instanciar a Hipo:
hipo = Entrenador(["roberta"])
