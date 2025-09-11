# Análisis propuestas del RETO:

1. **Se consulta el precio de un vuelo para una aerolinea, se necesita identificar el gasto del viaje en base a la variacion del peso en el vuelo por gasto de combustible y la distancia que recorre el avión. Para luego hacer una comparación de la venta de tiquetes y los gastos en combustible y confirmar si el vuelo es rentable para la aerolínea o no.**

## Análisis

**variables de entrada**
|nombre|tipo|comentario|
|--------------------|----|----------|
|PI|float|peso inicial de la aeronave|
|CC|float|cantidad de combustible|
|NT|int|el numero de asientos vendidos|
|T|float|Tiempo de vuelo que recorre el avion|
|VT|float|valor del tiquete|

**variables de control**
|nombre|tipo|comentario|
|------|----|----------|
|PC_U|float|peso por unidad de combustible|
|H|int|hora de vuelo|
|GH|float|gasto de combustible por hora|
|P|float|peso|peso total de la aeronave cada hora|
|VC|float|precio del combustible|
|VV|float|precio del viaje en base al combustible|
|ST|float|la suma de los tiquetes vendidos|

**variables de salida**
|nombre|tipo|comentario|
|------|----|----------|
|R|float|la rentabilidad o perdida resultante|
|E|booleana|determina si es viable o no|

## Pseudocódigo
```
Inicio



2. **Se requiere hacer el registro del mantenimiento de la aeronave de tipo A350-900 para poder autorizar su operación. A dichas aeronaves se les debe hacer un chequeo de mantenimiento del sistema hidráulico cada 600 horas de vuelo, y del sistema eléctrico, cada 400 horas, y además del sistema de aire acondicionado. Si hay una falla en el sistema hidráulico se debe hacer una reparación frenando la operación 2 días, en el sistema eléctrico de 3 días, pero si hay una falla en el sistema de aire acondicionado, el avión puede operar, pero con la restricción de volar hasta los 10.000 pies.**
```

## Análisis

| Variable | Tipo de Variable | Comentario |
|----------|------------------|------------|
|horas_vuelo |Entrada |Valor ingresado que determina si se debe hacer un mantenimiento de dicho sistema. |
|sistema_H |Entrada |Se indica si el sistema hidráulico tiene una falla o está bien. |
|sistema_E |Entrada |Se indica si el sistema eléctrico tiene una falla o está bien. |
|sistema_A |Entrada |Se indica si el sistema de aire acondicionado tiene una falla o está bien. |
|autorización |Salida | Decide si se autoriza, se restringe o se autoriza con restricciones la operación de la aeronave. |

## Pseudocódigo
```
Inicio
Ingresar horas_vuelo 
   LEER horas_vuelo
   SI horasVuelo >= 600 ENTONCES
       MOSTRAR "Debe realizarse chequeo de mantenimiento al sistema hidráulico."
   FIN SI
   SI horasVuelo >= 400 ENTONCES
       MOSTRAR "Debe realizarse chequeo de mantenimiento al sistema eléctrico."
   FIN SI
   MOSTRAR "Debe realizarse chequeo de mantenimiento al sistema de aire acondicionado."
   LEER sistema_H   
   LEER sistema_E   
   LEER sistema_A   
   SI sistema_H = "FALLA" ENTONCES
       MOSTRAR "Reparación de sistema hidráulico: operación detenida por 2 días."
       autorizacionOperacion = "NO AUTORIZADA"
   SINO
 SI sistema_E = "FALLA" ENTONCES
       MOSTRAR "Reparación de sistema eléctrico: operación detenida por 3 días."
       autorización = "NO AUTORIZADA"
   SINO
 SI sistema_A = "FALLA" ENTONCES
       MOSTRAR "Falla en sistema de aire acondicionado: operación restringida a 10.000 pies."
       autorización = "AUTORIZADA CON RESTRICCIÓN"
   SINO
       MOSTRAR "Todos los sistemas están bien."
       autorización = "AUTORIZADA"
   FIN SI
   MOSTRAR "Estado final de la aeronave: ", autorización
FIN
```


3. **En la aerolínea KLM se desea calcular el promedio de maletas que un operador de rampa carga en 4 semanas. El operador trabaja 6 días a la semana, por lo que en total son 24 días. Cada día se registra la cantidad de maletas cargadas. Si en algún día supera las 800 maletas, recibe un pago adicional de 50.000. Al final, se debe mostrar el total de maletas cargadas, el promedio diario y el pago adicional.**

## Análisis

| Variable | Tipo de Variable | Comentario |
|----------|------------------|------------|
|maletas_dia |Entrada |Registro de la cantidad de maletas cargadas en un día. |
|dias_t |Control |El total de 24 días. |
|i |Control |Controlador hasta hacerse 24 días. |
|pago_d |Control | Pago diario fijo que se le hace al trabajador. |
|total_maletas |Salida |Suma total de maletas_dia. |
|promedio_d |Salida |El promedio diario de maletas cargadas: total_maletas/dias_t. |
|pago_adicional |Salida |Determina si hay un pago adicional al superar el umbral de las 800 maletas por día. (maletas_dia > 800). |

## Pseudocódigo
```
   INICIO
dias_t = 4 * 6   // 24
umbraldiario = 800
pago_adicional = 50000
pago_d = 60000
total_maletas = 0
   Para i = 1 Hasta dias_t Hacer
       Leer maletas_dia[i]
       total_Maletas = total_maletas + maletasDia[i]
       Si maletasDia[i] > umbralDiario Entonces
           total = pago_d + pago_adicional
           opcional: SALIR DEL BUCLE si solo se necesita saber si existe al menos un día que excede
       FIN SI
   FIN PARA
   promedio_d = totalMaletas / diasTrabajados
   Mostrar "Total maletas (4 semanas): ", total_maletas
   Mostrar "Promedio diario: ", promedio_diario
   Mostrar "Pago adicional: ", pago_adicional
FIN
```



