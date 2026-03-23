from .model_StockBajoEvent import StockBajoEvent
from datetime import datetime


class Producto:
    def __init__(self, id: int, nombre: str, sku: str, stock: int = 0, stock_min: int = 1):
        self.id = id
        self.nombre = nombre
        self.sku = sku
        self.stock = stock
        self.stock_min = stock_min
        self.eventos = []

    def aumentar_stock(self, cantidad):
        if cantidad < 0:
            raise ValueError("Introduce una cantidad positiva.")
        self.stock += cantidad

    def restar_stock(self, cantidad):
        if self.stock < cantidad:
            raise ValueError(
                f"No podemos sacar esa cantidad. No tenemos tanto producto, actualmente podemos sacar un max de {self.stock}")
        minimo = self.stock - cantidad
        if minimo < self.stock_min:
            min_stock = StockBajoEvent(
                producto_id=self.id,
                stock_actual=minimo,
                timestamp=datetime.now()
            )
            self.eventos.append(min_stock)

        self.stock -= cantidad
