# Programacion Orientada a Objetos (POO)
# Ejemplo: Determinacion del promedio semanal del clima

class ClimaSemanal:
    # El constructor inicializa el objeto y sus atributos
    def __init__(self):
        # Encapsulamiento: La lista 'temperaturas' es parte del estado del objeto
        self.temperaturas = []

    # Metodo para ingresar datos (equivalente a 'deposit' en tu ejemplo bancario)
    def ingresar_temperatura(self, grados):
        self.temperaturas.append(grados)

    # Metodo para calcular el promedio (equivalente a 'calculate_interest')
    def calcular_promedio(self):
        # Verificamos si hay datos para evitar division por cero
        if not self.temperaturas:
            return 0.0
        
        # Sumamos los datos internos del objeto y dividimos
        suma_total = sum(self.temperaturas)
        return suma_total / len(self.temperaturas)

# --- Uso de la Clase (Instanciacion) ---

# 1. Crear una instancia (objeto) de la clase ClimaSemanal
mi_clima = ClimaSemanal()

# 2. Uso de los metodos para ingresar datos
# Simulamos el ingreso de 7 dias (puedes hacerlo manual o con un ciclo)
print("--- Ingresando datos al objeto ---")
mi_clima.ingresar_temperatura(20.5) # Lunes
mi_clima.ingresar_temperatura(22.0) # Martes
mi_clima.ingresar_temperatura(19.5) # Miercoles
mi_clima.ingresar_temperatura(21.0) # Jueves
mi_clima.ingresar_temperatura(23.5) # Viernes
mi_clima.ingresar_temperatura(25.0) # Sabado
mi_clima.ingresar_temperatura(24.0) # Domingo

# 3. Uso del metodo para calcular el resultado
promedio = mi_clima.calcular_promedio()

# Imprimir el saldo final (resultado) accediendo a los atributos o resultados
print("-" * 30)
print(f"Datos almacenados en el objeto: {mi_clima.temperaturas}")
print(f"Promedio Semanal (POO): {promedio:.2f}°")
