
# 1. ABSTRACCIÓN

# Definimos la clase "Producto" como la plantilla general.
# Representa cualquier objeto vendible. Abstraemos los datos comunes:
# todos tienen nombre, precio y stock, sin importar si son manzanas o televisores.

class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
      
        # 2. ENCAPSULAMIENTO
      
        # Usamos '__' para hacer privadas estas variables.
        # Protegemos el precio y el stock para que no se cambien por error
        # desde fuera (ej: precio negativo).
        self.__precio = precio
        self.__stock = stock

    # Getter para leer el precio de forma segura
    def obtener_precio(self):
        return self.__precio

    # Getter para ver stock
    def obtener_stock(self):
        return self.__stock

    def mostrar_info(self):
        print(f"PRODUCTO: {self.nombre}")
        print(f"· Stock disponible: {self.__stock}")
        print(f"· Precio base: ${self.__precio}")

    def hay_stock(self, cantidad):
        return self.__stock >= cantidad

    # Método para modificar el stock de forma controlada (Encapsulamiento)
    def vender(self, cantidad):
        if self.hay_stock(cantidad):
            self.__stock = self.__stock - cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}.")

    # Lógica base para calcular costo.
    # Este método será modificado por los hijos (Polimorfismo).
    def calcular_costo_final(self, cantidad):
        return self.__precio * cantidad



# 3. HERENCIA

# La clase 'Electronico' hereda todo de 'Producto'.
# Reutiliza la lógica de stock y precio base.

class Electronico(Producto):

    def __init__(self, nombre, precio, stock, garantia_meses):
        # Llamamos al constructor del padre
        super().__init__(nombre, precio, stock)
        self.garantia_meses = garantia_meses

    def mostrar_info(self):
        super().mostrar_info()
        print(f"· Garantía: {self.garantia_meses} meses")

  
    # 4. POLIMORFISMO
    
    # Sobreescribimos el método de cálculo.
    # Los electrónicos pagan un impuesto de lujo (IVA/Tax) del 20%.
    def calcular_costo_final(self, cantidad):
        precio_base = self.obtener_precio()
        impuesto = precio_base * 0.20
        return (precio_base + impuesto) * cantidad



# 3. HERENCIA

# 'Alimento' también es un 'Producto'.

class Alimento(Producto):

    def __init__(self, nombre, precio, stock, fecha_vencimiento):
        super().__init__(nombre, precio, stock)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"· Vence: {self.fecha_vencimiento}")

   
    # 4. POLIMORFISMO
    
    # Los alimentos de canasta básica tienen un DESCUENTO del 10%
    # y no pagan impuestos. La fórmula es diferente a la de Electronico.
    def calcular_costo_final(self, cantidad):
        precio_base = self.obtener_precio()
        descuento = precio_base * 0.10
        return (precio_base - descuento) * cantidad


# --- SIMULACIÓN DE CAJA (Similar a tu función 'combate') ---

def caja_registradora(cliente, carrito_compras):
    print(f"\n=== Iniciando cobro para: {cliente} ===")
    total_a_pagar = 0

    # Iteramos sobre una lista de tuplas: (ObjetoProducto, Cantidad)
    for producto, cantidad in carrito_compras:
        print("\n>>> Escaneando:", producto.nombre)
        
        if producto.hay_stock(cantidad):
            # 1. Ejecutamos la venta (baja stock interno)
            producto.vender(cantidad)
            
            # 2. POLIMORFISMO EN ACCIÓN:
            # Llamamos a .calcular_costo_final().
            # Python decide automáticamente si aplica la fórmula con IMPUESTO (Electrónico)
            # o la fórmula con DESCUENTO (Alimento).
            subtotal = producto.calcular_costo_final(cantidad)
            
            print(f"   Subtotal por {cantidad} unid: ${subtotal:.2f}")
            total_a_pagar += subtotal
        else:
            print("   [!] Producto omitido por falta de stock.")

    print("\n=======================================")
    print(f"TOTAL FINAL A PAGAR: ${total_a_pagar:.2f}")
    print("=======================================")


# --- Creación de Objetos ---

# TV: Precio 500, Stock 10, Garantía 12 meses
prod_1 = Electronico("Smart TV 50'", 500, 10, 12)

# Manzanas: Precio 2, Stock 50, Vence mañana
prod_2 = Alimento("Manzanas Kg", 2, 50, "10-DIC")

# Mostramos sus atributos antes de la venta
prod_1.mostrar_info()
print("---")
prod_2.mostrar_info()

# --- Simulación de Compra ---
# El cliente lleva 2 TVs y 5 Kilos de Manzanas
carrito = [
    (prod_1, 2), 
    (prod_2, 5)
]

caja_registradora("Juan Perez", carrito)