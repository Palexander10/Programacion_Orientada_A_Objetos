class ReporteService:
    def generar_reporte_final(self, lista_estudiantes):
        print("\n--- BOLETÍN DE CALIFICACIONES ---")
        
        for est in lista_estudiantes:
            promedio = est.promedio
            # POLIMORFISMO: Cada objeto sabe cuál es su nota mínima (7 u 8)
            nota_minima = est.obtener_requisito_aprobacion()
            
            estado = "APROBADO" if promedio >= nota_minima else "REPROBADO"
            
            print(est.mostrar_info())
            print(f"   Promedio: {promedio:.2f} / Mínimo requerido: {nota_minima}")
            print(f"   Estado Final: {estado}")
            print("-" * 40)