#####
# Socio
#####

class Socio:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

        self.prestamos = []  # Lista de libros prestados al socio
