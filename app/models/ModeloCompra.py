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
