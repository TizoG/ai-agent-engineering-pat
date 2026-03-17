class ConsultarEstado:
    def __init__(self, libro_repo, socio_repo):
        self.libro_repo = libro_repo
        self.socio_repo = socio_repo

    def ejecutar(self):
        libros = self.libro_repo.obtener_todos()
        socios = self.socio_repo.obtener_todos()

        return {"libros": libros, "socios": socios}
