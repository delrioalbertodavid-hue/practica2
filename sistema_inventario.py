class Producto:
    def __init__(self, nombre, precio, cantidad):
        try:
            if not nombre:
                raise ValueError("El nombre del producto no puede estar vacío.")
                    
            if cantidad <0:
                raise ValueError("La cantidad del producto debe ser mayor o igual a cero.")
                
            if precio <0:
                raise ValueError("El precio del producto debe ser mayor o igual a cero.")
        except ValueError as e:
            print(e)
            raise
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio del producto debe ser mayor o igual a cero.")
        else:
            self.precio = nuevo_precio
        return self
    
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad del producto debe ser mayor o igual a cero.")
        else:
            self.cantidad = nueva_cantidad
        return self
    
    def calcular_valor_total(self):
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            raise ValueError("El producto ya existe en el inventario.")
        else:
            self.productos[producto.nombre] = producto
        return self
    
    def buscar_producto(self, nombre):
        nombre = nombre.lower()
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        valor_total = 0
        for producto in self.productos.values():
            valor_total += producto.calcular_valor_total()
        return valor_total
    
    def listar_productos(self):
        return [str(producto) for producto in self.productos.values()]
    
def menu_principal(inventario):
    print("Bienvenido al Sistema de Inventario")
    print("1. Agregar producto")
    print("2. Buscar producto") 
    print("3. Listar productos") 
    print("4. Calcular valor total del inventario") 
    print("5. Salir")

    while True:
        opcion = input("Seleccione una opción (1-5): ")
        #inventario = Inventario()

        if opcion == '1':
            try:
                nombre = input("Ingrese el nombre del producto: ")
                if not nombre:
                    raise ValueError("El nombre del producto no puede estar vacío.")
                    
                precio = float(input("Ingrese el precio del producto: "))
                if precio <0:
                    raise ValueError("El precio del producto debe ser mayor o igual a cero.")
                
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad <0:
                    raise ValueError("La cantidad del producto debe ser mayor o igual a cero.")
                
                producto = Producto(nombre, precio, cantidad)
                       
                inventario.agregar_producto(producto)
                print("Producto agregado exitosamente.")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            producto = inventario.buscar_producto(nombre)
            print(producto if producto else "Producto no encontrado.")

        elif opcion == '3':
            productos = inventario.listar_productos()
            if productos:
                print("\n".join(productos))
            else:
                print("No hay productos en el inventario.")

        elif opcion == '4':
            valor_total = inventario.calcular_valor_inventario()
            print(f"El valor total del inventario es: {valor_total}")

        elif opcion == '5':
            print("Saliendo del sistema de inventario.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)