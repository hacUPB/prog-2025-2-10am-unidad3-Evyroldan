'''
numero = int(input("ingrese un número entero positivo"))
while numero < 0:
    numero = int(input("ingrese un número entero positivo"))
acum = 0
for cont in range (1,numero+1):
    if cont % 2 == 0:
        acum += cont #acum = acum + cont 
print(f"la suma de los pares es: {acum}")
'''
mensaje = "Universidad Pontificia Bolivariana"
numero = int(input("Ingrese el número positivo"))
# imprimir el mensaje un número de veces
for i in range(numero):
    print(mensaje)