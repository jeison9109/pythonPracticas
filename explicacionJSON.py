import json

exampleDic = {
    "lenguaje": "Python",
    "idioma": "Español",
    "programador": "Yeison Serna",
    "fecha": "24/10/2022",
    "usuarios": [
        {"nombre": "Joaquin", "correo": "j@quin.com"},
        {"nombre": "Martin", "correo": "m@tin.com"},
        {"nombre": "luna", "correo": "l@una.com"}
    ]
}

# Acceder a los datos del diccionario
print(exampleDic["usuarios"][0]["correo"])

# Guardar un diccionario como JSON en un archivo en el PC
with open('fileJSON.json', 'w') as jsonFile:
    json.dump(exampleDic, jsonFile)
    jsonFile.close()

# Leer un archivo .json y obtener la info en un diccionario
with open('miSegundoJSON.json') as jsonFile:
    dicProducts = json.load(jsonFile)
    jsonFile.close()
