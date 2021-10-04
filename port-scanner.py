import sys
import socket

NombreHost= socket.gethostname()
DireccionIp= socket.gethostbyname(NombreHost)

objetivo=socket.gethostbyname(DireccionIp)

print("Escaneando...")
print("Este proceso puede llevar unos minutos, por favor paciencia.")

try:
  for port in range(1,150):
      s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      resultado=s.connect_ex((objetivo,port))
      print(".")
      if resultado==0:
         print("El puerto {} está abierto".format(port))
      s.close()
except:
  print("\n Terminando programa...")
  sys.exit(0)
