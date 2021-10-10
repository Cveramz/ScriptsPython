#Crear calculadora que transforme un decimal a cualquier base.


def decimal_a_binario(decimal):
  binario= bin(decimal)
  binario=binario.replace("0b","")
  return(binario)



def decimal_a_hexa(decimal):
  return hex(decimal)

def decimal_a_octal(decimal):
  octal= oct(decimal)
  octal=octal.replace("0o","")
  return octal



print("============================")
print("Calculadora que transforma entero a cualquier base")
print("")
print("Aviso: Este programa funciona solo con numeros enteros")
print("============================")
i=0
while (i==0):
  try: 
    numero= int(input("Ingrese un valor para transformar: "))
  except:
    numero=0
  if (numero<0):
    print("El valor ingresado es negativo")
  elif (numero==0):
    print("El valor ingresado no es entero.")
  else:
    i=1
i=0
while (i==0):
  print("\n============================")
  print("MENÚ:")
  print("[1]DECIMAL A BINARIO")
  print("[2]DECIMAL A HEXADECIMAL")
  print("[3]DECIMAL A OCTAL")
  print("[4]Todas las anteriores")
  print("============================")
  opcion= int(input("Ingrese una opción: "))
  if (opcion==1):
    print(decimal_a_binario(numero))
    i=i+1
  elif (opcion==2):
    print(decimal_a_hexa(numero))
    i=i+1
  elif (opcion==3):
    print(decimal_a_octal(numero))
    i=i+1
  elif (opcion==4):
    print("******************************")
    print("Numero ingresado: ", numero)
    print("Binario: ",decimal_a_binario(numero))
    print("Hexadecimal: ",decimal_a_hexa(numero))
    print("Octal: ",decimal_a_octal(numero))
    print("******************************")
    i=i+1
  else:
    print("\n****Valor ingresado no valido****")
