class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        # ENCAPSULAMIENTO: La lista de notas es privada (__).
        # Evitamos que se modifique externamente sin validación.
        self.__notas = []

    # Método para agregar notas de forma segura
    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print(f"Error: La nota {nota} no es válida (debe ser 0-10).")

    # Getter (Propiedad) para calcular el promedio al vuelo
    @property
    def promedio(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    # Método base para Polimorfismo (será sobrescrito)
    # Define la nota mínima para aprobar, que cambia según el nivel.
    def obtener_requisito_aprobacion(self):
        return 7.0  # Por defecto

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} (ID: {self.matricula})"