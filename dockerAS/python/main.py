from pymemcache.client.base import Client
import requests

def getPokemon(pokeName):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokeName.lower()
    request = requests.get(url)
    urlTipo = request.json()['forms'][0]['url']
    requestTipo = requests.get(urlTipo)

    tipos = requestTipo.json()['types']
    tipo = ""
    for i in tipos:
        tipoNuevo = i['type']['name']
        tipo += str(tipoNuevo) + " / "
    return tipo
#  Mamcachearekin lotu
client = Client(('basededatos', 11211))

def hacer():
    num = ""
    print("Qué quieres hacer?")
    print("1. Meter un nuevo Pokémon en la base de datos")
    print("2. Buscar el tipo de un Pokémon en concreto")
    try:
        num = input("Mete en número por favor... \n")
    except EOFError as e:
        num = 1
    if num == '1':
        try:
            pokeName = input("Mete el nombre de un Pokémon \n")
        except EOFError as e:
            pokeName = "jynx"
        tipo = getPokemon(pokeName)
        client.set(pokeName, tipo)
    else:
        try:
            pokeName = input("Mete el nombre de un Pokémon \n")
        except EOFError as e:
            pokeName = "pikachu"
        tipo = client.get(pokeName)
        if tipo == None:
            print("El pokémon " + pokeName + " no está en la base de datos, se va a añadir")
            tipo = getPokemon(pokeName)
            client.set(pokeName,tipo)

        print("El tipo del Pokemon es: ")
        print(tipo)

if __name__=="__main__":
    while True:
        hacer()
