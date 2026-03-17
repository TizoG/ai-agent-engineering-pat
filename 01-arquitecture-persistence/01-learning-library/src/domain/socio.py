#####
# Socio
#####

class Socio:
    def __init__(self, id, nombre, email, prestamos=None):
        self.id = id
        self.nombre = nombre
        self.email = email

        self.prestamos = prestamos if prestamos is not None else []
