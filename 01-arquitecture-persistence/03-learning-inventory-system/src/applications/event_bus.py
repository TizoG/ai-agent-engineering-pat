from ..domain.model_producto import Producto


class EventBus:
    def __init__(self):
        self.eventos = {}

    def registrar(self, tipo_evento, handler):
        self.eventos[tipo_evento] = handler

    def despachar(self, producto: Producto):
        eventos = producto.eventos
        for e in eventos:
            handler = self.eventos.get(type(e))
            if handler:
                handler(e)
