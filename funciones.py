import json

def agregar_categoria(nombrecategoria):
    with open ("biblioteca.json", mode= "r") as leerjson:
        archivojson= json.load(leerjson)
        indice=len(archivojson["categoria"]) + 1
        nuevaCategoria={
            "categoria": indice,
            "Nombre": nombrecategoria
        }
        leerjson["categoria"].append(nuevaCategoria)
    with open ("biblioteca.json", mode="w") as escribirjson:
        json.dump(archivojson, escribirjson, indent=4)

def editar_categoria(nuevoNombre: str, id: str):
    with open("biblioteca.json", mode="r") as leerjson:
        archivojson = json.load(leerjson)

        contador = 0
        for i in archivojson["Categoria"]:
            if i["CategoriaID"] == id:
                archivojson["Categoria"][contador]["categoriaID"]= nuevoNombre
                contador+=1
    with open ("biblioteca.json", mode="w") as escribirJson:
        json.dump(archivojson,indent=4)

def eliminarCategoria(id:int):
    with open ("biblioteca.json", mode = "r") as leerJson:
        archivoJson= json.load(leerJson)

        contador=0
        for i in archivoJson["Categoria"]:
            if i ["CategoriaID"]== id:
                del archivoJson["Categoria"][contador]
                contador+=1
    with open ("biblioteca.json", mode="w") as escribirJson:
        json.dump(archivoJson, escribirJson, indent=4)

def buscarCategoria(id:int):
    with open ("biblioteca.json", mode="r") as leerjson:
        archivoJson= json.load(leerjson)
        contador = 0

        for i in archivoJson["Categoria"]:
            if i ["CategoriaID"]== id:
                del archivoJson["Categoria"][contador]
                contador +=1
    with open ("biblioteca.json", mode="w") as escribirJson:
        json.dump(archivoJson, escribirJson, indent=4)
    