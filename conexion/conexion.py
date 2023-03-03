import mysql.connector

class conexion:

    def __init__(self):
        self.database = mysql.connector.connect(
            host ="localhost",
            user ="root", 
            password ="1234", 
            database = "bdpruebapatrullaje",
        )

    def buscarPuntoBi(self, codigo):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM datosbi WHERE Cod = "{}"; '''.format(codigo)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset