from datetime import datetime


class StockBajoEvent:
    def __init__(self, producto_id: int, stock_actual: int, timestamp: datetime):
        self.producto_id = producto_id
        self.stock_actual = stock_actual
        self.timestamp = timestamp
