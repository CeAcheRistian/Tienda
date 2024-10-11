from .entities.Compra import Compra
from .entities.Libro import Libro


class ModeloCompra():

    @classmethod
    def registrar_compra(self, db, compra):
        try:
            cursor = db.connection.cursor()
            sql = f"INSERT INTO compra (uuid, libro_isbn, usuario_id) VALUES (uuid(), '{
                compra.libro.isbn}', '{compra.usuario.id}')"
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as e:
            print(e)

    @classmethod
    def listar_compras_usuario(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = f'SELECT COM.fecha, LIB.isbn, LIB.titulo, LIB.precio FROM compra COM JOIN libro LIB ON COM.libro_isbn = LIB.isbn WHERE COM.usuario_id = {
                usuario.id}'
            cursor.execute(sql)
            data = cursor.fetchall()
            compras: list = []
            for row in data:
                libro = Libro(row[1], row[2], None, None, row[3])
                compra = Compra(None, libro, usuario, row[0])
                compras.append(compra)
            return compras
        except Exception as e:
            print(e)
