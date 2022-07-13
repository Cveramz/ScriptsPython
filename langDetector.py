from langdetect import detect #pip install langdetect
print("Detector de idioma, procure ingresar una cantidad considerable de palabras para ser detectado correctamente.\n\n")
texto=input("Ingrese texto: ")
print(detect(texto))
