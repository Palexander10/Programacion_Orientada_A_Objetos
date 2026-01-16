from models.estudiante import Estudiante

# HERENCIA: Hereda de Estudiante
class EstudiantePregrado(Estudiante):
    def __init__(self, nombre, matricula, carrera):
        super().__init__(nombre, matricula)
        self.carrera = carrera

    # POLIMORFISMO: Sobrescribimos el método.
    # Un estudiante de pregrado aprueba con 7.0
    def obtener_requisito_aprobacion(self):
        return 7.0

    def mostrar_info(self):
        return f"[Pregrado - {self.carrera}] {self.nombre}"