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


producto1 = Producto("P001", "Teclado", 350.00, 15)

producto1.mostrar_informacion()