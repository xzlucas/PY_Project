from mailbox import NoSuchMailboxError


class Persona():

    def __init__(self,nombre, apellido, edad) -> None:
        self.nombre= nombre
        self.apellido= apellido
        self.edad = edad

