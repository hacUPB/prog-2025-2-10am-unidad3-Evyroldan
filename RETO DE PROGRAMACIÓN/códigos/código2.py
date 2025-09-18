# Registro de mantenimiento de aeronaves A350-900

def r_mantenimiento():
    while True:
        horas_vuelo = int(input("Ingrese las horas de vuelo: "))

        mantenimiento = False  
        autorizacion = "AUTORIZADA"

        if horas_vuelo >= 600:
            print("Debe realizarse chequeo de mantenimiento al sistema hidráulico.")
            sistema_H = input("Estado del sistema hidráulico (OK/FALLA): ").upper()
            if sistema_H == "FALLA":
                print("Reparación de sistema hidráulico: operación detenida por 2 días.")
                autorizacion = "NO AUTORIZADA"
            mantenimiento = True

        if horas_vuelo >= 400:
            print("Debe realizarse chequeo de mantenimiento al sistema eléctrico.")
            sistema_E = input("Estado del sistema eléctrico (OK/FALLA): ").upper()
            if sistema_E == "FALLA":
                print("Reparación de sistema eléctrico: operación detenida por 3 días.")
                autorizacion = "NO AUTORIZADA"
            mantenimiento = True

        if horas_vuelo >= 70:
            print("Debe realizarse chequeo de mantenimiento al sistema de aire acondicionado.")
            sistema_A = input("Estado del sistema de aire acondicionado (OK/FALLA): ").upper()
            if sistema_A == "FALLA":
                print("Falla en sistema de aire acondicionado: operación restringida a 10.000 pies.")
                if autorizacion == "AUTORIZADA":
                    autorizacion = "AUTORIZADA CON RESTRICCIÓN"
            mantenimiento = True

        if not mantenimiento:
            print("No requiere mantenimiento aún.")
        else:
            print("Estado final de la aeronave:", autorizacion)

        # Preguntar si desea continuar con otra aeronave 
        continuar = input("\n¿Desea registrar otra aeronave? (SI/NO): ").upper()
        if continuar != "SI":
            print("Registro de mantenimiento finalizado.")
            break

r_mantenimiento()





# aquí se hizo uso de la IA para expresar correctamente la función.