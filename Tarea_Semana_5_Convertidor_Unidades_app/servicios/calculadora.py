# servicios/calculadora.py
from modelos.unidades import ConversorBase

class GestorConversion:
    #Clase encargada de ejecutar la lógica de negocio.

    def procesar(self, objeto_conversion: ConversorBase) -> bool:
    #POLIMORFISMO: Recibe un objeto de tipo ConversorBase (puede ser temperatura o longitud).

        
        # Tipo de dato: Float (obtenido del cálculo)
        resultado = objeto_conversion.convertir()
        
        # Tipo de dato: String
        simbolo = objeto_conversion.obtener_simbolo()
        
        # Validación simple (Tipo de dato: Boolean)
        exito = True if result is not None else False

        if exito:
            print(f"--> Resultado: {resultado} {simbolo}")
            return True
        else:
            print("Error en la conversión.")
            return False