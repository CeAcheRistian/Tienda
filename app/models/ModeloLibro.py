from .entities.Autor import Autor
from .entities.Libro import Libro


class ModeloLibro:

    @classmethod
    def listar_libros(self, db) -> list:
        try:
            cursor = db.connection.cursor()
            sql = "SELECT LIB.isbn, LIB.titulo, LIB.anioedicion, LIB.precio, AUT.apellidos, AUT.nombres FROM libro LIB JOIN autor AUT ON LIB.autor_id = AUT.id ORDER BY LIB.titulo ASC"
            cursor.execute(sql)
            data = cursor.fetchall()
            libros = []
            for row in data:
                aut = Autor(0, row[4], row[5])
                lib = Libro(row[0], row[1], aut, row[2], row[3])
                libros.append(lib)
            return libros
        except Exception as e:
            raise Exception(e)
