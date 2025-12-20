# Archivo: avion.py
# Clase: Avion
# Descripción:
# Este archivo define la clase Avion, encargada de gestionar
# los asientos y mostrar el estado del vuelo.

class Avion:
    """
    Clase que representa un avión y administra sus asientos.
    """

    def __init__(self, modelo):
        """
        Constructor de la clase Avion.
        
        Parámetros:
        - modelo: nombre o modelo del avión
        """
        self.modelo = modelo
        self.asientos = [] # Lista de objetos Asiento

    def agregar_asiento(self, asiento):
        """
        Añade un objeto Asiento al inventario del avión.
        """
        self.asientos.append(asiento)

    def mostrar_estado_vuelo(self):
        """
        Muestra la lista de asientos y si están disponibles o no.
        """
        print(f"\nEstado del vuelo - Avión: {self.modelo}")
        for asiento in self.asientos:
            estado = "Ocupado" if asiento.ocupado else "Disponible"
            print(f"Asiento: {asiento.numero} | Clase: {asiento.clase} | Estado: {estado}")