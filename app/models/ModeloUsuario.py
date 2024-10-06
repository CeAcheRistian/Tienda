from .entities.Usuario import Usuario
from werkzeug.security import check_password_hash

class ModeloUsuario:

    @classmethod
    def login(self, db, usuario: Usuario):
        try:
            cursor = db.connection.cursor()
            sql = f"SELECT id, usuario, password FROM usuario WHERE usuario = '{usuario.usuario}' "
            cursor.execute(sql)
            data = cursor.fetchone()
            
            coincide = check_password_hash(data[2], usuario.password)
            if coincide:
                usuario_logeado = Usuario(data[0],data[1],None,None)
                return usuario_logeado
            else:
                return None
        except Exception as e:
            raise Exception(e)
