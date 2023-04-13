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
    
    def buscarAnalista(self, corp, ant):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM analistasbi WHERE CORPORATIVO = "{}" AND ANTIGUEDAD = "{}"; '''.format(corp, ant)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset

    
    def analistasBi(self, area):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM analistasbi WHERE AREA = "{}" AND ROL = "ANALISTA"; '''.format(area)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset
    
    def coordinadoresBi(self):
        self.cursor = self.database.cursor()
        sql = 'SELECT * FROM analistasbi WHERE ROL = "COORDINADOR"; '
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset
    
    def analistasCorpBi(self, corp):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM analistasbi WHERE CORPORATIVO = "{}"; '''.format(corp)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset
    
    def registrarAnalista(self, nombre, corp, ant, rol, area):
        self.cursor = self.database.cursor()
        sql = '''INSERT INTO analistasbi(NOMBRE, CORPORATIVO, ANTIGUEDAD, ROL, AREA)
                 VALUES('{}', '{}', '{}', '{}', '{}')'''.format(nombre, corp, ant, rol, area)
        
        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def eliminarAnalista(self, corp):
        self.cursor = self.database.cursor()
        sql = '''DELETE FROM analistasbi WHERE CORPORATIVO = "{}";'''.format(corp)

        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def buscarMotivo(self, motivo):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM motivos WHERE MOTIVO = "{}"; '''.format(motivo)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset

    def agregarMotivo(self, motivo):
        self.cursor = self.database.cursor()
        sql = '''INSERT INTO motivos(MOTIVO)
                 VALUE('{}')'''.format(motivo)
        
        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def descripcionMotivo(self):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM motivos; '''
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset
    
    def eliminarMotivo(self, motivo):
        self.cursor = self.database.cursor()
        sql = '''DELETE FROM motivos WHERE MOTIVO = "{}";'''.format(motivo)

        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def addPatrulla(self, no, fecha, cod, centroCosto, puntoBi, 
                    nombreBi, ubicaion, direccionBi, motivo, autorizadoAbas, 
                    codigoConfirmacion, proveedor, tiempoRespuesta, horaSolicitudCentral):
        self.cursor = self.database.cursor()
        sql = '''INSERT INTO patrullaje(No, Fecha, Codigo, CentroCosto, PuntoBi, 
                                        Nombre, Ubicación, Dirección, Motivo, AutorizadoAbastecimiento, 
                                        CodigoConfirmacion, Proveedor, TiempoRespuesta, HoraSolicitudCentral)
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(no, fecha, cod, centroCosto, puntoBi,
                                                                                                          nombreBi, ubicaion, direccionBi, motivo, autorizadoAbas,
                                                                                                            codigoConfirmacion, proveedor, tiempoRespuesta, horaSolicitudCentral)
        
        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def mostrarPatrulla(self):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM patrullaje; '''
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset


        
