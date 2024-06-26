import json

def cargadatos():
    with open ("biblioteca.json", "r") as file:
    leerjson= json.load(file)


def agregar_categoria(nombre:str, id:str):
    datos= cargadatos
