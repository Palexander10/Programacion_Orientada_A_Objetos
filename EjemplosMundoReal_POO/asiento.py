# Archivo: asiento.py
# Clase: Asiento
# Descripción:
# Este archivo define la clase Asiento, la cual representa un sitio 
# específico dentro del avión y si esta disponible.

class Asiento:
    """
    Clase que modela un asiento de avión.
    """

    def __init__(self, numero, clase):
        """
        Constructor de la clase Asiento.
        
        Parámetros:
        - numero: identificador del asiento (ej. '12A')
        - clase: categoría del asiento (Turista o Ejecutiva)
        """
        self.numero = numero
        self.clase = clase
        self.ocupado = False  # Indica si el asiento ya fue reservado

    def reservar(self):
        """
        Método que marca el asiento como ocupado si está disponible.
        """
        if not self.ocupado:
            self.ocupado = True
            print(f"Asiento {self.numero} reservado con éxito.")
        else:
            print(f"El asiento {self.numero} ya se encuentra ocupado.")