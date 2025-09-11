#Condicional Simple:
#Se le pide al usuario que ingrese un numero entero y que 
# muestre un mensaje si el numero es divisible por 3.

numero = int(input("Ingrese un número entero: "))
residuo = numero % 3
if residuo == 0:
 print(f"{numero} es divisible entre 3" )
