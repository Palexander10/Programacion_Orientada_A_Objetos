# servicios/calculadora.py
from modelos.unidades import ConversorBase

class GestorConversion:

    #Clase encargada de ejecutar la lógica de negocio.
   
    
    def procesar(self, objeto_conversion: ConversorBase) -> bool:
      
        #POLIMORFISMO: Recibe un objeto de tipo ConversorBase.
       
        
        # 1. Obtenemos el resultado (float)
        resultado = objeto_conversion.convertir()
        
        # 2. Obtenemos el símbolo (string)
        simbolo = objeto_conversion.obtener_simbolo()
        
        # 3. Validación: Aquí estaba el error, usamos 'resultado'
        exito = True if resultado is not None else False

        if exito:
            print(f"--> Resultado: {resultado} {simbolo}")
            return True
        else:
            print("Error en la conversión.")
            return False