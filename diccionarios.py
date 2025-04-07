##Diccionarios:

##Son colecciones de datos
##Cada elmento de un diccionario
##Se puede dividir en 2 partes
# ## 1. clave: el nombre del elemento
# ## 2. valor: el valor del elemento
## Ejemplo de dicionario:
## Para caracterizar un pais:

pais = {
    "nombre": "Colombia",
    "capital": "Bogotá",
    "idioma": "Español",
    "poblacion": 51,
    "superficie": "1141748",
    "moneda": "Peso Colombiano",
    "ciudades": [
        "bogota",
        "Medellin",
        "Cali",
        "Barranquilla",
        "Cartagena",
    ]
}

#acceder a propiedades
print("Capital de Colombia: " , pais["capital"])
print("Y se habla:" , pais["idioma"])
print("Habitantes" , pais["poblacion"])
print("Y sus ciudades son:")
for ciudad in pais ["ciudades"]:   
    print(ciudad)