class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print("INFORMACIÓN DEL PRODUCTO")
        print("------------------------")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Precio: $", self.precio)
        print("Existencia:", self.existencia)
        print("Estado: Producto registrado exitosamente")


# Función para el Reto de Búsqueda
def buscar_producto(lista_productos, codigo_buscado):
    for prod in lista_productos:
        if prod.codigo == codigo_buscado:
            return prod
    return None


# Pruebas de la búsqueda
inventario = [
    Producto("P001", "Teclado", 350.00, 15),
    Producto("P002", "Mouse", 150.00, 20)
]

resultado = buscar_producto(inventario, "P001")

if resultado:
    print("¡PRODUCTO ENCONTRADO!")
    resultado.mostrar_informacion()
else:
    print("Producto no encontrado.")