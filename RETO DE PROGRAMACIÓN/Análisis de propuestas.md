# Análisis propuestas del RETO:

1. (se encarga Deybid)

2. **Se requiere hacer el registro del mantenimiento de la aeronave de tipo A350-900 para poder autorizar su operación. A dichas aeronaves se les debe hacer un chequeo de mantenimiento del sistema hidráulico cada 600 horas de vuelo, y del sistema eléctrico, cada 400 horas, y además del sistema de aire acondicionado. Si hay una falla en el sistema hidráulico se debe hacer una reparación frenando la operación 2 días, en el sistema eléctrico de 3 días, pero si hay una falla en el sistema de aire acondicionado, el avión puede operar, pero con la restricción de volar hasta los 10.000 pies.**

## Análisis

| Variable | Tipo de Variable | Comentario |
|----------|------------------|------------|
|horas_vuelo |Entrada |Valor ingresado que determina si se debe hacer un mantenimiento de dicho sistema. |
|sistema_H |Entrada |Se indica si el sistema hidráulico tiene una falla o está bien. |
|sistema_E |Entrada |Se indica si el sistema eléctrico tiene una falla o está bien. |
|sistema_A |Entrada |Se indica si el sistema de aire acondicionado tiene una falla o está bien. |
|autorización |Salida | Decide si se autoriza, se restringe o se autoriza con restricciones la operación de la aeronave. |

3. **En la aerolínea KLM se desea calcular el promedio de maletas que un operador de rampa carga en 4 semanas. El operador trabaja 6 días a la semana, por lo que en total son 24 días. Cada día se registra la cantidad de maletas cargadas. Si en algún día supera las 800 maletas, recibe un pago adicional de 50.000. Al final, se debe mostrar el total de maletas cargadas, el promedio diario y el pago adicional.**

## Análisis

| Variable | Tipo de Variable | Comentario |
|----------|------------------|------------|
|maletas_dia |Entrada |Registro de la cantidad de maletas cargadas en un día. |
|dias_t |Control |El total de 24 días. |
|i |Control |Controlador hasta hacerse 24 días. |
|total_maletas |Salida |Suma total de maletas_dia. |
|promedio_d |Salida |El promedio diario de maletas cargadas: total_maletas/dias_t. |
|pago_adicional |Salida |Determina si hay un pago adicional al superar el umbral de las 800 maletas por día. (maletas_dia > 800). |



