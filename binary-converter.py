def binario(decimal):
  binario=""
  while (decimal//2) !=0:
    binario=str(decimal%2)+binario
    decimal=decimal//2
  return str(decimal)+binario

numero= int(input("Introducir valor para convertir a binario: "))
print("El valor es en binario es:  ",binario(numero))
