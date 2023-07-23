# pip install rembg

#Link de repositorio: https://github.com/Cveramz/ScriptsPython

from rembg import remove
from PIL import Image

print("Bienvenido al programa de eliminacion de fondo de imagenes")

nombre_entrada=input("Ingrese el nombre de la imagen: ")

#verificar si existe la imagen
try:
    nombre_salida=input("Ingrese el nombre de la imagen de salida: ")
    #verificar que salida tenga la extension .png
    if nombre_salida[-4:]!=".png":
        nombre_salida+=".png"
    entrada = Image.open(nombre_entrada)
    salida= remove(entrada)
    salida.save(nombre_salida)
    print("Imagen procesada con exito")
except:
    print("La imagen no existe")
