import requests

# Vamos a usar Macowins que es una app de juguete de venta de ropa:
# https://macowins-server.herokuapp.com/prendas/1 --> protocolo; dominio; primer recurso de prendas.
# me traigo de la base de datos el primer item de prendas.
# HTTP tiene verbos que me dice que estoy haciendo con los recursos;
# "GET": verbo Hppt para hacer los pedidos al servidor "traeme los recursos"
# r.json() --> formato de dato y se parece a un diccionario
"""
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(r.json())

{
  "id": 1,
  "tipo": "pantalon",
  "talle": 35
}

# DESAFIO I: Hacé otro pedido para traer a la prenda 20. Deberías obtener el siguiente resultado:
r = requests.get('https://macowins-server.herokuapp.com/prendas/20')
print(r.json())

# Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
r = requests.get("https://macowins-server.herokuapp.com/prendas/400")
print(r.json())
print(r.headers)

# Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' 
# ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?

r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
print(r.headers)

#{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 'Date': 'Thu, 03 Nov 2022 23:27:14 GMT', 'Via': '1.1 vegur'}

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? 

r = requests.get("https://macowins-server.herokuapp.com/prindas/1")
print(r.headers)
#HTTP/1.1 404 Not Found

r = requests.get('https://macowins-server.herokuapp.com/nueva-funcionalidad-que-a-veces-no-anda-bien')
print(r.headers)
print(r.content) #b'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>Error</title>\n</head>\n<body>\n<pre>Internal Server Error</pre>\n</body>\n</html>\n'

r = requests.get('https://macowins-server.herokuapp.com/prendas')
print(r.json())

# Desafío VI: Obtené las remeras.
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
print(r.json())

#Desafío VII: Obtené las remeras XS
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
print(r.json())"""

# Ejercicio de Clase:
# En base al siguiente enlace "https://pokeapi.co/api/v2/pokemon/pikachu", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

# a) ¿Cuál es el dominio al que estamos consultando? pokeapi
# b) ¿Qué status_code devuelve el pedido a dicha URL? 200
import requests
r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(r.status_code)
# 200
#¿Y qué Content-Type?
print(r.headers)
# 'Content-Type': 'application/json; charset=utf-8'
# Obtené la información correspondiente al campo "forms".
print(r.json()["forms"])
# [{'name': 'pikachu', 'url': 'https://pokeapi.co/api/v2/pokemon-form/25/'}]

# c) Averigüá cuántos Pokemones almacena la API.
# Cambiar el url 
url2 = requests.get("https://pokeapi.co/api/v2/pokemon")
print(len(url2.json()))
# 4

# d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?
# https://pokeapi.co/api/v2/abilities
# https://pokeapi.co/api/v2/abilities2 
# https://pokeapi.co/api/v2/abilities?abilities=2

# f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".
with open("ficha_tecnica_pokemon.txt", "a")as salida:
  salida.write(str(r.json()))

""" ver esto!!
import 
pikachu = requests.get(“
with open(“ficha_tecnica.txt”, a) as salida:
salida.write(str(pikachu.json())
"""
