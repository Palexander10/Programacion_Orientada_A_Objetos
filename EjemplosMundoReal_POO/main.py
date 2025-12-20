# Archivo: main.py
# Programa principal
# Descripción:
# Este archivo ejecuta el sistema de voletos, creando los
# objetos necesarios y demostrando la interacción entre ellos.

from avion import Avion
from asiento import Asiento

# Creación del objeto Avion
mi_avion = Avion("Aeroregional 123")

# Creación de objetos Asiento
asiento1 = Asiento("1A", "Ejecutiva")
asiento2 = Asiento("15C", "Turista")

# Asociación de los asientos al avión
mi_avion.agregar_asiento(asiento1)
mi_avion.agregar_asiento(asiento2)

# Muestra el estado inicial
mi_avion.mostrar_estado_vuelo()

# Reserva de un asiento
print("\n--- Realizando reserva ---")
asiento1.reservar()

# Muestra el estado final tras la reserva
mi_avion.mostrar_estado_vuelo()