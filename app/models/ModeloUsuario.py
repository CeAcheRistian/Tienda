class ModeloUsuario:

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = f"SELECT id, usuario, password FROM usuario WHERE usuario = '{usuario.usuario}'"
            cursor.execute(sql)
            data = cursor.fetchone()

        except Exception as e:
            raise Exception(e)
