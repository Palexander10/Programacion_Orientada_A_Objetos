# main.py
from modelos.unidades import CelsiusAFahrenheit, MetrosAPies
from servicios.calculadora import GestorConversion

def main():
    #Función principal para ejecutar el convertidor POO.

    print("=== SISTEMA DE CONVERSIÓN POO ===")
    
    # Instanciamos el servicio (gestor)
    gestor = GestorConversion()

    # Variables para demostración de tipos de datos
    continuar = True  # Boolean
    contador_usos = 0 # Integer

    while continuar:
        print("\nSeleccione una opción:")
        print("1. Convertir Celsius a Fahrenheit")
        print("2. Convertir Metros a Pies")
        print("3. Salir")

        opcion = input("Ingrese opción: ") # String

        if opcion == "1":
            try:
                val = float(input("Ingrese grados Celsius: "))
                # Creamos objeto específico (Polimorfismo en acción más adelante)
                conversion = CelsiusAFahrenheit(val)
                gestor.procesar(conversion)
                contador_usos += 1
            except ValueError:
                print("Por favor ingrese un número válido.")

        elif opcion == "2":
            try:
                val = float(input("Ingrese metros: "))
                conversion = MetrosAPies(val)
                gestor.procesar(conversion)
                contador_usos += 1
            except ValueError:
                print("Por favor ingrese un número válido.")

        elif opcion == "3":
            continuar = False
            print(f"Saliendo... Realizaste {contador_usos} conversiones hoy.")
        
        else:
            print("Opción no reconocida.")

if __name__ == "__main__":
    main()