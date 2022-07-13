import pyqrcode //pip install pyqrcode
import png //pip install pypng
print("QR GENERATOR\n\n")

link = input("Ingrese un enlace: \n")
url = pyqrcode.create(link)
url.png("image.png", scale = 7)
