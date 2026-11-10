import sys
import os
import io
import unittest

# Permite importar desde la carpeta src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from producto import Producto


class TestProducto(unittest.TestCase):

    def setUp(self):
        """Configuración previa a cada prueba."""
        self.prod1 = Producto("P001", "Teclado", 350.00, 10)
        self.prod2 = Producto("P002", "Mouse", 180.00, 5)

    def test_CP01_crear_producto(self):
        """CP01: Verificar creación correcta del objeto Producto"""
        self.assertIsNotNone(self.prod1)

    def test_CP02_mostrar_codigo(self):
        """CP02: Verificar almacenamiento y valor del código"""
        self.assertEqual(self.prod1.codigo, "P001")

    def test_CP03_mostrar_nombre(self):
        """CP03: Verificar almacenamiento y valor del nombre"""
        self.assertEqual(self.prod1.nombre, "Teclado")

    def test_CP04_mostrar_precio(self):
        """CP04: Verificar almacenamiento y valor del precio"""
        self.assertEqual(self.prod1.precio, 350.00)

    def test_CP05_mostrar_existencia(self):
        """CP05: Verificar almacenamiento y valor de la existencia"""
        self.assertEqual(self.prod1.existencia, 10)

    def test_CP06_mostrar_informacion_completa(self):
        """CP06: Verificar que la función imprima toda la información"""
        capturar_salida = io.StringIO()
        sys.stdout = capturar_salida
        
        self.prod1.mostrar_informacion()
        sys.stdout = sys.__stdout__  # Restaurar consola
        
        salida = capturar_salida.getvalue()
        self.assertIn("P001", salida)
        self.assertIn("Teclado", salida)
        self.assertIn("350", salida)
        self.assertIn("10", salida)

    def test_CP07_crear_segundo_producto(self):
        """CP07: Verificar independencia de datos en un segundo objeto"""
        self.assertEqual(self.prod2.codigo, "P002")
        self.assertEqual(self.prod2.nombre, "Mouse")
        self.assertEqual(self.prod2.precio, 180.00)
        self.assertEqual(self.prod2.existencia, 5)


if __name__ == '__main__':
    unittest.main()