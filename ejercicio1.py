nombre = input("ingresa tu nombre y apellido: ")
#Opción2
print("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input("Ingresa tu peso en kilogramos: ")
peso = float(peso)
altura = input("Ingresa tu talla en metros: ")
altura = float(altura)
#Cálculos
imc = peso/altura**2
#Mostrarimc
print("Ti IMC = ", imc)

if imc < 18.5:
    print("Bajo peso ")
elif imc < 25:
    print("Peso normal ")
elif imc < 35:
    print("Obesidad tipo 1")
elif imc < 40:
    print("Obesidad tipo 2 ")
else:
    print("Obesidad extrema ")

print(f"Paciente {nombre}, tiene un IMC de {imc:0.2f} y su condición es {print}. ")

