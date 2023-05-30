import mysql.connector

class conexion:

    def __init__(self):
        self.database = mysql.connector.connect(
            host ="localhost",
            user ="root", 
            password ="1234", 
            database = "bdpruebapatrullaje",
            pool_size = 10
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

    #Tabla de patrullaje
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
                    nombreBi, direccionBi, ubicaion, motivo, autorizadoAbas, 
                    codigoConfirmacion, proveedor, tiempoRespuesta, horaSolicitudCentral, horaLlegada, 
                    tiempoRealRespuesta, excedenteTiempo, retiro, duracionServicio, operadorBi, operadorCRC, 
                    numeroBoleta, nombrePatrullero, observacionServicio, coordinadorCargo,descripcion, areaOperador):
        self.cursor = self.database.cursor()
        sql = '''INSERT INTO patrullaje(No, Fecha, Codigo, CentroCosto, PuntoBi, 
                                        Nombre, Dirección, Ubicación, Motivo, AutorizadoAbastecimiento, 
                                        CodigoConfirmacion, Proveedor, TiempoRespuesta, HoraSolicitudCentral, HoraLlegada,
                                        TiempoRealRespuesta, ExcedenteTiempo, Retiro, DuracionServicio, OperadorBi, OperadorCRC, 
                                        NumeroBoleta, NombrePatrullero, ObservacionServicio, CoordinadorCargo, Descripcion, Area)
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
                        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(
                                                                                        no, fecha, cod, centroCosto, puntoBi,
                                                                                        nombreBi, direccionBi, ubicaion, motivo, autorizadoAbas,
                                                                                        codigoConfirmacion, proveedor, tiempoRespuesta, horaSolicitudCentral, horaLlegada,
                                                                                        tiempoRealRespuesta, excedenteTiempo, retiro, duracionServicio, operadorBi, operadorCRC, 
                                                                                        numeroBoleta, nombrePatrullero, observacionServicio, coordinadorCargo, descripcion, areaOperador)
        
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

    def buscarPatrulla(self, no, cod, motivo, operador):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM patrullaje WHERE No = "{}" AND Codigo = "{}" AND Motivo = "{}" AND OperadorBi = "{}"; '''.format(no, cod, motivo, operador)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset   

    def buscarPatrullaFecha(self, fecha):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM patrullaje WHERE Fecha = "{}" ; '''.format(fecha)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset    

    def editarDatosPatrulla(self, no, cod, 
                            motivo, codigoConfirmacion, 
                            horaSolicitud, horaLlegada,
                            tiempoRealRespuesta, excedenteTiempo,
                            horaRetiro, duracionServicio, nombreOperador,
                            numeroBoleta, nombrePatrullero,
                            observacionServicio, descripcion,):
        self.cursor = self.database.cursor()
        sql = '''UPDATE patrullaje SET Motivo = '{}', CodigoConfirmacion = '{}',
                                        HoraSolicitudCentral = '{}', HoraLlegada = '{}',
                                        TiempoRealRespuesta = '{}', ExcedenteTiempo = '{}',
                                        Retiro = '{}', DuracionServicio = '{}', OperadorCRC = '{}', 
                                        NumeroBoleta = '{}', NombrePatrullero = '{}',
                                        ObservacionServicio = '{}', Descripcion = '{}'
                WHERE No = '{}' AND Codigo = '{}'; '''.format(motivo, codigoConfirmacion,
                                                              horaSolicitud, horaLlegada,
                                                              tiempoRealRespuesta, excedenteTiempo,
                                                              horaRetiro, duracionServicio, nombreOperador,
                                                              numeroBoleta, nombrePatrullero,
                                                              observacionServicio, descripcion,
                                                              no, cod)
        
        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def eliminarPatrulla(self, no, cod):
        self.cursor = self.database.cursor()
        sql = '''DELETE FROM patrullaje WHERE No = "{}" AND Codigo = "{}";'''.format(no, cod)

        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def searchPatrulla(self, cod):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM patrullaje WHERE Codigo = "{}"; '''.format(cod)
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset
    
    # Tabla de patrullas eliminadas
    def addPatrullaEliminada(self, no, fecha, cod, nombre, motivo, area):
        self.cursor = self.database.cursor()

        sql = '''INSERT INTO patrullaeliminada(No, Fecha, Codigo, Nombre, Motivo, Area) VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(no, fecha, cod, nombre, motivo, area)
        
        self.cursor.execute(sql)
        self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def mostrarPatrullasEliminadas(self):
        self.cursor = self.database.cursor()
        sql = '''SELECT * FROM patrullaeliminada; '''
        self.cursor.execute(sql)
        resultset = self.cursor.fetchall()
        self.cursor.close()
        self.database.commit()
        self.database.close()

        return resultset