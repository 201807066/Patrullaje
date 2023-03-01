import mysql.connector

class conexion:

    def __init__(self):
        self.database = mysql.connector.connect(
            host ="192.168.1.7",
            user ="root", 
            password ="1234", 
            database = "",
            pool_size = 0
        )