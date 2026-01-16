from modelos.pregrado import EstudiantePregrado
from modelos.postgrado import EstudiantePostgrado
from servicios.reporte_service import ReporteService

def main():
    # 1. Instancias y carga de datos
    # Estudiante de Pregrado (necesita 7.0)
    est1 = EstudiantePregrado("Carlos Ramirez", "U001", "Contabilidad")
    est1.agregar_nota(8.0)
    est1.agregar_nota(7.5)
    est1.agregar_nota(9.0) # Promedio: ~7.3 (Debería aprobar)

    # Estudiante de Postgrado (necesita 8.0, exigencia mayor)
    est2 = EstudiantePostgrado("Ana Ocampo", "M505", "Economia")
    est2.agregar_nota(7.5)
    est2.agregar_nota(7.5) 
    est2.agregar_nota(7.0) # Promedio: ~7.3 (Debería reprobar aunque tiene la misma nota que Carlos)

    # 2. Demostración de Encapsulamiento
    # Intentamos meter una nota inválida
    print("--- Test de validación ---")
    est1.agregar_nota(20) # Esto imprimirá error y no se agregará
    
    # 3. Lista Polimórfica
    clase_programacion = [est1, est2]

    # 4. Ejecución del Servicio
    servicio = ReporteService()
    servicio.generar_reporte_final(clase_programacion)

if __name__ == "__main__":
    main()