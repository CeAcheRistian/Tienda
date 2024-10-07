from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario
from werkzeug.security import check_password_hash


class ModeloUsuario:

    @classmethod
    def login(self, db, usuario: Usuario):
        try:
            cursor = db.connection.cursor()
            sql = f"SELECT id, usuario, password FROM usuario WHERE usuario = '{
                usuario.usuario}' "
            cursor.execute(sql)
            data = cursor.fetchone()

            if data != None:
                coincide = check_password_hash(data[2], usuario.password)
                if coincide:
                    usuario_logeado = Usuario(data[0], data[1], None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None

        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT USU.id, USU.usuario, TIP.id, TIP.nombre
                    FROM usuario USU JOIN tipousuario TIP
                    ON USU.tipousuario_id = TIP.id
                    WHERE USU.id = {id}"""

            cursor.execute(sql)
            data = cursor.fetchone()
            tipo_usuario = TipoUsuario(data[2], data[3])
            usuario_logeado = Usuario(data[0], data[1], None, tipo_usuario)

            return usuario_logeado

        except Exception as e:
            Exception(e)
