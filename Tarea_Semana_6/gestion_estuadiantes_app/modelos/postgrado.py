from modelos.estudiante import Estudiante

# HERENCIA: Hereda de Estudiante
class EstudiantePostgrado(Estudiante):
    def __init__(self, nombre, matricula, maestria):
        super().__init__(nombre, matricula)
        self.maestria = maestria

    # POLIMORFISMO: Sobrescribimos el método.
    # Un estudiante de maestría necesita 8.0 para aprobar (mayor exigencia).
    def obtener_requisito_aprobacion(self):
        return 8.0

    def mostrar_info(self):
        return f"[Maestría en {self.maestria}] {self.nombre}"