import json
import os

from ..repository.product_repository import ProductRepository
from ..domain.model_producto import Producto


class JsonProductoRepositorio(ProductRepository):

    def __init__(self, archivo="producto.json"):
        self.archivo = archivo
        self.productos = self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            return {}

        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                resultados = {}
                for id, p in datos.items():
                    producto = Producto(
                        p["id"], p["nombre"], p["sku"], p["stock"], p["stock_min"])
                    resultados[producto.id] = producto

                return resultados

        except IOError as e:
            raise IOError(str(e))

    def _guardar_datos(self):
        try:
            with open(self.archivo, "w") as f:
                datos_guardar = {str(id): {
                    "id": p.id,
                    "nombre": p.nombre,
                    "sku": p.sku,
                    "stock": p.stock,
                    "stock_min": p.stock_min
                } for id, p in self.productos.items()}

                json.dump(datos_guardar, f, indent=4)
        except:
            raise IOError("Error al guardar datos.")

    def get_by_id(self, id: int):
        if not self.productos.get(id):
            raise KeyError("El producto no existe.")
        return self.productos.get(id)

    def get_all(self):
        return list(self.productos.values())

    def guardar(self, producto: Producto):
        self.productos[producto.id] = producto
        self._guardar_datos()
