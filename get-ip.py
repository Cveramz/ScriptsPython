from socket import gethostname, gethostbyname

NombreHost= gethostname()
DireccionIp= gethostbyname(NombreHost)

print("El nombre del host es: ",NombreHost)
print("La dirección Ip es: ", DireccionIp)
