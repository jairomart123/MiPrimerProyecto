from .entities.User import User
import MySQLdb


class ModelUser():
    
#EndPoint
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)




###_________________________
    @classmethod
    def registro(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO user username, password, fullname, Apellido, Email, Direccion, Detalle, Ciudad, Municipio, Cgpostal ={}".format()
            cursor.execute(sql)
            row = cursor.fetchone()
        except Exception as ex:
            raise Exception(ex)

