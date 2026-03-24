from ..domain.model_StockBajoEvent import StockBajoEvent


def handle_stock_bajo(evento: StockBajoEvent):
    print(
        f"ALERTA: El producto {evento.producto_id} tiene stock bajo. Stock actual: {evento.stock_actual} unidades.")
