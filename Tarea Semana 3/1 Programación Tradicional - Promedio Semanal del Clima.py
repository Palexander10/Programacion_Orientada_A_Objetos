# Programación Tradicional
# Ejemplo: Promedio semanal del clima

# Definicion de variables globales
# Lista para almacenar las temperaturas de los 7 dias
weekly_temperatures = []

# Función para la entrada de datos diarios (temperaturas)
def input_temperatures():
    global weekly_temperatures
    print("--- Entrada de Datos ---")
    # Ciclo para pedir la temperatura de los 7 dias de la semana
    for day in range(1, 8):
        # Solicitamos el dato al usuario y lo convertimos a flotante
        temp = float(input(f"Ingrese la temperatura del día {day}: "))
        weekly_temperatures.append(temp)

# Funcion para calcular el promedio semanal
def calculate_average():
    global weekly_temperatures
    
    # Verificamos si la lista no esta vacia para evitar errores
    if len(weekly_temperatures) == 0:
        return 0.0
    
    # Sumamos todas las temperaturas acumuladas
    total_sum = sum(weekly_temperatures)
    
    # Calculamos el promedio dividiendo la suma entre la cantidad de días
    average = total_sum / len(weekly_temperatures)
    return average

# Uso de las funciones en la programacion tradicional

# 1. Llamamos a la función para llenar los datos
input_temperatures()

# 2. Llamamos a la función para realizar el cálculo
# Guardamos el resultado en una variable local para imprimirlo
final_average = calculate_average()

# Imprimimos el resultado final
print("-" * 30)
print(f"Temperaturas registradas: {weekly_temperatures}")
print(f"Promedio Semanal (Traditional): {final_average:.2f}°")
