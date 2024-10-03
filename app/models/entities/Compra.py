class Compra:
    def __init__(self, uuid, libro, usuario, fecha=None) -> None:
        self.uuid = uuid
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha
