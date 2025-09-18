<<<<<<< HEAD
# Simulaciones de lanzamiento de cohete

def simular_cohete(combustible_e1, combustible_e2):
    objetivo_alt = 200
    consumo_1 = 800
    consumo_2 = 500
    IA1 = 5
    IA2 = 3

    altitud = 0
    minuto = 0
    etapa = 1

    while altitud < objetivo_alt:
        if etapa == 1:
            if combustible_e1 > 0:
                combustible_e1 -= consumo_1
                altitud += IA1
                minuto += 1
            else:
                etapa = 2
        elif etapa == 2:
            if combustible_e2 > 0:
                combustible_e2 -= consumo_2
                altitud += IA2
                minuto += 1
            else:
                print("\nEl cohete se quedó sin combustible en la etapa 2.")
                print("Altitud alcanzada:", altitud, "km")
                return

    print("\nEl cohete alcanzó la órbita de 200 km en", minuto, "minutos.")

while True:
    print("\n--- Simulación de lanzamiento de cohete ---")
    combustible_e1 = int(input("Ingrese la cantidad de combustible de la etapa 1 (kg): "))
    combustible_e2 = int(input("Ingrese la cantidad de combustible de la etapa 2 (kg): "))

    simular_cohete(combustible_e1, combustible_e2)

    continuar = input("\n¿Desea realizar otra simulación? (SI/NO): ").upper()
    if continuar == "NO":
        print("Simulación finalizada.")
        break

# La sugirió un segundo bucle para poder ofrecerle al usuario volver a registrar los datos para una nueva simulación.
# Además de que se le solicitó una corrección de lo que consideraba innecesario o erróneo.
=======
dias_trabajados = 6  
umbral_diario = 800
pago_diario = 60000
pago_adicional = 50000
total_maletas = 0
total_pago = 0
dias_exceso = 0
i = 1
while i <= dias_trabajados:
    # Simulación determinística: días impares = 750, días pares = 850(apoyo con IA Para la simulacion)
    if i % 2 == 0:
        maletas_dia = 850
    else:
        maletas_dia = 750

    print(f"Día {i}: {maletas_dia} maletas")

    total_maletas += maletas_dia
    total_pago += pago_diario

    if maletas_dia > umbral_diario:
        total_pago += pago_adicional
        dias_exceso += 1
    i += 1
promedio_diario = total_maletas / dias_trabajados
print(f"Total maletas (4 semanas): {total_maletas}")
print(f"Promedio diario: {promedio_diario:.2f}")
print(f"Días con exceso (> {umbral_diario} maletas): {dias_exceso}")
print(f"Pago total recibido: ${total_pago}")
>>>>>>> 84cd4090201caf1a5dc468e8cbac5d0ae6bffa8a
