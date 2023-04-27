import tkinter
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import datetime
from conexion import conexion
import xlsxwriter


class VentanaPatrullaje:

    def __init__(self, login, nombreAnalista, coordinador, areaAnalista, rolAnalista):
    #def __init__(self):
        #VENTANA
        self.login = login
        self.ventana = Toplevel(login)
        #self.ventana = Tk()
        self.ventana.title('Patrullaje Bi')
        self.ventana.resizable(False, False)
        self.ventana.geometry("1350x650")

        #Variables
        fecha = datetime.datetime.now()
        self.fechaPrincipal = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year)
        self.opc = IntVar()

        #Datos de usuario login
        #self.usuario = user
        self.coordinador = coordinador
        self.nombreAnalista = nombreAnalista
        self.areaAnalista = areaAnalista
        self.rolAnalista = rolAnalista

        self.no = StringVar()
        self.codigo = StringVar()
        self.fechaCordinacion = ""
        self.excedente = ""
        self.duracion = ""
        self.areaAnalistaAux = ""


        #Variables de patrullaje
        self.codigoBi = StringVar()
        self.centroCosto = StringVar()
        self.puntoBi = StringVar()
        self.nombreBi = StringVar()
        self.ubicacion = StringVar()
        self.direccion = StringVar()
        self.autorizado = StringVar()
        self.proveedor = "Ebano"
        self.tiempoRespuesta = StringVar()
        self.tiempoRealRespuesta = ""
        self.excedenteTiempo = ""
        self.retiro = StringVar()
        self.duracionServicio = ""

        self.codigoConfirmacion = StringVar()

        self.horaSolicitud = StringVar()
        self.horaLlegada = StringVar()
        self.horaRetiro = StringVar()
        
        self.nombreOperador = StringVar()
        self.numeroBoleta = StringVar()
        self.nombrePatrullero = StringVar()

        self.observacionServicio = StringVar()
        self.descripcion = StringVar()

        #Contador 
        self.i = 1
        self.iEliminadas = 1


        #Barra de menu
        self.barraMenu = Menu()
        self.menuArchivo = Menu(self.barraMenu, tearoff=False)

        self.menuArchivo.add_command(label = "Reporte", command=self.reportesPatrullaje)
        self.menuArchivo.add_command(label = "Eliminados", command=self.reportesEliminados)
        self.menuArchivo.add_command(label="Cerrar Sesión", command=self.ventana.destroy)

        self.barraMenu.add_cascade(menu=self.menuArchivo, label="Archivo")
        self.ventana.config(menu=self.barraMenu)


        #Widgets -----> Apartado 1
        self.marcoPrincipal = Frame(self.ventana)
        self.marcoPrincipal.config(bg="#dcffff", width=1350, height=750)
        self.lblTitulo = Label(self.marcoPrincipal, text="\t\t\t\tSeguridad Corporativa" + "\t\t\t    Fecha: " + self.fechaPrincipal)
        self.lblTitulo.config(bg="#325795", width=1350, anchor="w", height=1, font=("Rockwell", 20, 'bold'), foreground="#FFFFFF", relief=RAISED)

        self.marcoTitulo = Frame(self.marcoPrincipal)
        self.marcoTitulo.config(bg="#325795", width=570, height=85)


        self.lblNombreOperadorBi = Label(self.marcoTitulo, text="Hola "+ self.nombreAnalista)
        self.lblNombreOperadorBi.config(bg="#325795",anchor="w", height=1, font=("Rockwell", 10, 'bold'), foreground="#FFFFFF")
        self.lblBI = Label(self.marcoTitulo, text="  BI")
        self.lblBI.config(bg="#325795",anchor="w", height=1, font=("Rockwell", 50, 'bold'), foreground="#FFFFFF")
        self.lblSeguridad = Label(self.marcoTitulo, text="    </Patrullaje>")
        self.lblSeguridad.config(bg="#325795",anchor="w", height=1, font=("Rockwell", 30, 'bold'), foreground="#FFFFFF")


        #Widgets -----> Apartado 2
        self.lblNombreBi = Label(self.marcoPrincipal, text="Nombre:")
        self.lblNombreBi.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'), foreground="#0e326e")
        self.lblCodigo = Label(self.marcoPrincipal, text="Código:")
        self.lblCodigo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigo = Entry(self.marcoPrincipal, textvariable=self.codigo)
        self.txtCodigo.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=10)
        self.txtCodigo.bind("<Return>", self.buscarPuntoBi)

        self.btnDetalles = Button(self.marcoPrincipal, text="Detalles", command=self.informacioPuntoBi)
        self.btnDetalles.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.lblAutorizado = Label(self.marcoPrincipal, text="Autorizado para abastecimiento:")
        self.lblAutorizado.config(bg="#dcffff", font=("Comic Sans MS", 11))
        self.lblAutorizadoSINO = Label(self.marcoPrincipal, text="SI/NO")
        self.lblAutorizadoSINO.config(bg="#dcffff", font=("Comic Sans MS", 15, 'bold'))
        self.lblMotivo = Label(self.marcoPrincipal, text="Motivo")
        self.lblMotivo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.cbxMotivo = ttk.Combobox(self.marcoPrincipal, background="#F4F4F4", state="readonly", width=25)
        self.cbxMotivo.config(font=("Comic Sans MS", 12), width=15)
        self.lblCodigoConfirmacion = Label(self.marcoPrincipal, text="Código de confirmación")
        self.lblCodigoConfirmacion.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigoConfirmacion = Entry(self.marcoPrincipal, textvariable=self.codigoConfirmacion)
        self.txtCodigoConfirmacion.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=8)
        self.txtCodigoConfirmacion.insert(END, "N/A");

        #Widgets -----> Apartado 3
        self.lblHoraSolicitud = Label(self.marcoPrincipal, text="Hora solicitud central Bi\n(Formato 24 horas)")
        self.lblHoraSolicitud.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtHoraSolicitud = Entry(self.marcoPrincipal, textvariable=self.horaSolicitud)
        self.txtHoraSolicitud.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=12)
        self.lblHoraLlegada = Label(self.marcoPrincipal, text="Hora llegada")
        self.lblHoraLlegada.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtHoraLlegada = Entry(self.marcoPrincipal, textvariable=self.horaLlegada)
        self.txtHoraLlegada.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=12)     
        self.lblHoraRetiro = Label(self.marcoPrincipal, text="Hora retiro")
        self.lblHoraRetiro.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtHoraRetiro = Entry(self.marcoPrincipal, textvariable=self.horaRetiro)
        self.txtHoraRetiro.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=12)

        #Widgets -----> Apartado 4
        self.lblNombreOperador = Label(self.marcoPrincipal, text="Nombre operador")
        self.lblNombreOperador.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtNombreOperador = Entry(self.marcoPrincipal, textvariable=self.nombreOperador)
        self.txtNombreOperador.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblNumeroBoleta = Label(self.marcoPrincipal, text="Número de boleta")
        self.lblNumeroBoleta.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtNumeroBoleta = Entry(self.marcoPrincipal, textvariable=self.numeroBoleta)
        self.txtNumeroBoleta.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblNombrePatrullero = Label(self.marcoPrincipal, text="Nombre patrullero")
        self.lblNombrePatrullero.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtNombrePatrullero = Entry(self.marcoPrincipal, textvariable=self.nombrePatrullero)
        self.txtNombrePatrullero.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)

         #Widgets -----> Apartado 5

        self.lblObservacionServicio = Label(self.marcoPrincipal, text="Observaciones del servicio")
        self.lblObservacionServicio.config(bg="#dcffff", font=("Comic Sans MS", 12, "bold"), foreground="#0e326e")
        self.txtObservacionServicio = Text(self.marcoPrincipal)
        self.txtObservacionServicio.config(bg="#F4F4F4", font=("Comic Sans MS", 12), height = 13, width = 40)
        self.lblDescripcion = Label(self.marcoPrincipal, text="Descripción")
        self.lblDescripcion.config(bg="#dcffff", font=("Comic Sans MS", 12, "bold"), foreground="#0e326e")
        self.txtDescripcion = Text(self.marcoPrincipal)
        self.txtDescripcion.config(bg="#F4F4F4", font=("Comic Sans MS", 12), height = 8, width = 40)

        self.btnEliminar = Button(self.marcoPrincipal, text="Eliminar", command=self.eliminarPatrulla)
        self.btnEliminar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnAceptar = Button(self.marcoPrincipal, text="Aceptar", command=self.addPatrulla)
        self.btnAceptar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnGuardar = Button(self.marcoPrincipal, text="Guardar", command=self.editarPatrulla)
        self.btnGuardar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))

        self.lblSearchCodigo = Label(self.marcoPrincipal, text="Buscar por código")
        self.lblSearchCodigo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigoSearch = Entry(self.marcoPrincipal)
        self.txtCodigoSearch.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=10)
        self.txtCodigoSearch.bind("<Return>", self.searchPatrulla)

        #Creacion de la tabla de patrullas enviadas
        columnas = ('#0', '#1', '#2')
        self.tabla = ttk.Treeview(self.marcoPrincipal, height=20,  columns=columnas)
        self.tabla.bind("<Double-Button-1>", self.doubleClickTabla)
        self.tabla.column('#0', width=40)       
        self.tabla.heading('#0', text='No.', anchor=CENTER)
        self.tabla.column('#1', width=50)
        self.tabla.heading('#1', text='Cod', anchor=CENTER)
        self.tabla.column('#2', width=110)        
        self.tabla.heading('#2', text='Motivo', anchor=CENTER)
        self.tabla.column('#3', width=100)        
        self.tabla.heading('#3', text='Operador', anchor=CENTER)

        self.lblPatrullasEnviadas = Label(self.marcoPrincipal, text="Patrullas enviadas")
        self.lblPatrullasEnviadas.config(bg="#dcffff", font=("Comic Sans MS", 12, "bold"), foreground="#0e326e")

        #separador-----> Apartado 1
        self.separador1v = ttk.Separator(self.marcoPrincipal, orient="vertical")
        #separador-----> Apartado 2
        self.separador2h = ttk.Separator(self.marcoPrincipal, orient="horizontal")
        self.separador2v = ttk.Separator(self.marcoPrincipal, orient="vertical")

        self.separador3v = ttk.Separator(self.marcoPrincipal, orient="vertical")

    def mostrarVentana(self):
        self.marcoPrincipal.place (x=0,y=0)
        self.lblTitulo.place(x=0, y=0)

        self.marcoTitulo.place(x=0, y=38)
        self.lblNombreOperadorBi.place(x=250, y=0)
        self.lblBI.place(x=0, y=0)
        self.lblSeguridad.place(x=150, y=20)

         #Widgets -----> Apartado 2
        self.lblNombreBi.place(x=10, y=135)
        self.lblCodigo.place(x=10, y=205)
        self.txtCodigo.place(x=90, y=205)
        self.btnDetalles.place(x=210, y=200)
        self.lblAutorizado.place(x=300, y=175)
        self.lblAutorizadoSINO.place(x=380, y=225)
        self.lblMotivo.place(x=125, y=285)
        self.cbxMotivo.place(x=200, y=285)
        self.lblCodigoConfirmacion.place(x=100 , y=345)
        self.txtCodigoConfirmacion.place(x=300, y=345)

         #Widgets -----> Apartado 3
        self.lblHoraSolicitud.place(x=50 , y=405)
        self.txtHoraSolicitud.place(x=80 , y=460)
        self.lblHoraLlegada.place(x=90 , y=490) 
        self.txtHoraLlegada.place(x=80 , y=520)
        self.lblHoraRetiro.place(x=90 , y=550)
        self.txtHoraRetiro.place(x=80 , y=580)

        #Widgets -----> Apartado 4
        self.lblNombreOperador.place(x=365, y=415)
        self.txtNombreOperador.place(x=325,y=460)
        self.lblNumeroBoleta.place(x=365, y=490)
        self.txtNumeroBoleta.place(x=325,y=520)
        self.lblNombrePatrullero.place(x=365,y=550)
        self.txtNombrePatrullero.place(x=325,y=580)

        #Widgets -----> Apartado 5
        self.lblObservacionServicio.place(x=700,y=50)
        self.txtObservacionServicio.place(x=588,y=85)
        self.lblDescripcion.place(x=750,y=400)
        self.txtDescripcion.place(x=588,y=437)

        self.btnEliminar.place(x=1255,y=550)
        self.btnAceptar.place(x=1100,y=600)
        self.btnGuardar.place(x=1200,y=600)

        # ** Creacion de la tabla con los datos de las patrullas enviadas **
        self.lblSearchCodigo.place(x=1075, y=50)
        self.txtCodigoSearch.place(x=1225, y=55)
        self.lblPatrullasEnviadas.place(x=1125, y=90)
        self.tabla.place(x=1032, y=120)

        #Separador -----> Apartado 1
        self.separador1v.place(relx=0.42, rely=0.052, relheight=1, relwidth=0.002)
        self.separador2h.place(relx=0, rely=0.525, relheight=0.002, relwidth=0.420)

        self.separador2v.place(relx=0.21, rely=0.525, relheight=0.4, relwidth=0.002)
        self.separador3v.place(relx=0.75, rely=0.052, relheight=1, relwidth=0.002)

        self.btnGuardar["state"] = "disable"
        self.btnEliminar["state"] = "disable"

        self.motivosPatrulla()
        self.mostrarPatrullas()
        self.ventana.mainloop()
    #Se obtienen las variables de la ventana de patrullaje
    
    def buscarPuntoBi(self, event):
        self.conexion = conexion.conexion().buscarPuntoBi(self.codigo.get())
        self.txtHoraSolicitud.delete(0, END)

        if self.conexion == []:
            messagebox.showerror("Error", "Punto de servicio no encontrado")
            self.txtCodigo.delete(0, END)
        else:
            for i in self.conexion:
                self.codigoBi = i[1]
                self.centroCosto = i[2]
                self.puntoBi = i[3]
                self.nombreBi = i[4]
                self.ubicacion = i[5]
                self.direccion = i[6]
                self.tiempoRespuesta = i[7]
                self.autorizado = i[9]


                if i[9] == "SI":
                    self.lblAutorizadoSINO['text'] = "SI"
                    self.lblAutorizadoSINO.config(fg="#008000", font=("Comic Sans MS", 15, 'bold'))
                elif i[9] == "NO":
                    self.lblAutorizadoSINO['text'] = "NO"
                    self.lblAutorizadoSINO.config(fg="#cc0605", font=("Comic Sans MS", 15, 'bold'))
                else:
                    self.lblAutorizadoSINO['text'] = "N/A"
                    self.lblAutorizadoSINO.config(fg="#000000", font=("Comic Sans MS", 15, 'bold'))

                self.lblNombreBi['text'] = "Nombre: \t"+i[4]

            
                self.txtHoraSolicitud.insert(0, datetime.datetime.now().strftime("%H:%M"))

    def informacioPuntoBi(self):

        horaActualAux = datetime.datetime.now().strftime("%H:%M")
        tiempoRealRespuestaAux = ""
        excedenteTiempoAux = self.excedente
        duracionServicioAux = self.duracion

        self.conexion = conexion.conexion().buscarPuntoBi(self.codigo.get())
        name = ""
        direccion = ""
        tiempoRespuesta = ""
        puntoBi = ""

        if self.fechaCordinacion == self.fechaPrincipal:

            if self.txtHoraSolicitud.get() != "" and self.txtHoraLlegada.get() == "":
                tiempoRealRespuestaAux = str(self.restarHoras(horaActualAux, self.txtHoraSolicitud.get()))
            
            #Se calcula el tiempo de excedente de la patrualla
                excedenteTiempoAux = str(self.restarHoras(tiempoRealRespuestaAux[:-3], self.tiempoRespuesta[:-3]))

                if excedenteTiempoAux < "00:00:00":
                    excedenteTiempoAux = "00:00:00"
                if self.txtHoraLlegada.get() == "":
                    duracionServicioAux = "Patrullero aun no ha llegado al punto de servicio Bi"
                    print("duracion servicio: ", duracionServicioAux)
            elif self.txtHoraLlegada.get() != "" and self.txtHoraRetiro.get() == "":
                duracionServicioAux = str(self.restarHoras(horaActualAux, self.txtHoraLlegada.get()))

        for i in self.conexion:
            puntoBi = i[3]
            name = i[4]
            direccion = i[6]
            tiempoRespuesta = i[7]
        

        messagebox.showinfo(puntoBi, "Nombre: {} \nDirección: {} \nTiempo de respuesta: {}\n--------------------------------\nFecha de coordinación: {} \nExcedente de tiempo: {}\nDuración del servicio: {}\nÁrea: {}".format(name, direccion, tiempoRespuesta, self.fechaCordinacion, excedenteTiempoAux, duracionServicioAux, self.areaAnalistaAux))
        
    def motivosPatrulla(self):
        motivos = []

        self.motivos = conexion.conexion().descripcionMotivo()

        for i in self.motivos:
            motivos.append(i[1])
        self.cbxMotivo["values"] = motivos

    #********** REPORTES EXCEL **********
    def reportesPatrullaje(self):
        fila = 1
        columna = 0
        fecha = simpledialog.askstring("Reporte", "¿Fecha de reporte día-mes-año?")

        if fecha == NONE:
            pass
        elif fecha == "":
            self.reportePatrulla = conexion.conexion().mostrarPatrulla()

            workbook = xlsxwriter.Workbook('patrullaje_total.xlsx')
            sheet = workbook.add_worksheet()

            bold = workbook.add_format({'bold': True})

            sheet.write('A1', 'No.', bold)
            sheet.write('B1', 'Fecha', bold)
            sheet.write('C1', 'Código', bold)
            sheet.write('D1', 'Centro de costo', bold)
            sheet.write('E1', 'Punto BI', bold)
            sheet.write('F1', 'Nombre', bold)
            sheet.write('G1', 'Dirección', bold)
            sheet.write('H1', 'Ubicación', bold)
            sheet.write('I1', 'Motivo', bold)
            sheet.write('J1', 'Autorizado para abastecimiento', bold)
            sheet.write('K1', 'Codigo de confirmación (Jefe/Patrullero)', bold)
            sheet.write('L1', 'Proveedor', bold)
            sheet.write('M1', 'Tiempo de respuesta Ebano', bold)
            sheet.write('N1', 'Hora solicitud central Bi', bold)
            sheet.write('O1', 'Hora llegada', bold)
            sheet.write('P1', 'Tiempo real de respuesta', bold)
            sheet.write('Q1', 'Excedente de tiempo', bold)
            sheet.write('R1', 'Retiro', bold)
            sheet.write('S1', 'Duración del servicio', bold)
            sheet.write('T1', 'Operador BI', bold)
            sheet.write('U1', 'Nombre de operador', bold)
            sheet.write('V1', 'Número de boleta', bold)
            sheet.write('W1', 'Nombre patrullero', bold)
            sheet.write('X1', 'Observaciones de servicio', bold)
            sheet.write('Y1', 'Coordinador a cargo', bold)
            sheet.write('AA1', 'Área', bold)
            sheet.write('Z1', 'Descripción', bold)

            for i in self.reportePatrulla:                    
                if i[26] == self.areaAnalista and self.rolAnalista == "ANALISTA":
                    incremento = 0
                    for j in i:
                        sheet.write(fila, columna + incremento, str(j))
                        incremento += 1
                    fila += 1
                elif self.rolAnalista == "COORDINADOR":
                    incremento = 0
                    for j in i:
                        sheet.write(fila, columna + incremento, str(j))
                        incremento += 1
                    fila += 1
                
            workbook.close()
        else:  
            self.reportePatrulla = conexion.conexion().buscarPatrullaFecha(fecha)

            if self.reportePatrulla == []:
                messagebox.showinfo("Patrullas", "No se coordinaron patrullas en esta fecha: {}".format(fecha))
            else:
                workbook = xlsxwriter.Workbook('patrullaje_'+fecha+'.xlsx')
                sheet = workbook.add_worksheet()

                bold = workbook.add_format({'bold': True})

                sheet.write('A1', 'No.', bold)
                sheet.write('B1', 'Fecha', bold)
                sheet.write('C1', 'Código', bold)
                sheet.write('D1', 'Centro de costo', bold)
                sheet.write('E1', 'Punto BI', bold)
                sheet.write('F1', 'Nombre', bold)
                sheet.write('G1', 'Dirección', bold)
                sheet.write('H1', 'Ubicación', bold)
                sheet.write('I1', 'Motivo', bold)
                sheet.write('J1', 'Autorizado para abastecimiento', bold)
                sheet.write('K1', 'Codigo de confirmación (Jefe/Patrullero)', bold)
                sheet.write('L1', 'Proveedor', bold)
                sheet.write('M1', 'Tiempo de respuesta Ebano', bold)
                sheet.write('N1', 'Hora solicitud central Bi', bold)
                sheet.write('O1', 'Hora llegada', bold)
                sheet.write('P1', 'Tiempo real de respuesta', bold)
                sheet.write('Q1', 'Excedente de tiempo', bold)
                sheet.write('R1', 'Retiro', bold)
                sheet.write('S1', 'Duración del servicio', bold)
                sheet.write('T1', 'Operador BI', bold)
                sheet.write('U1', 'Nombre de operador', bold)
                sheet.write('V1', 'Número de boleta', bold)
                sheet.write('W1', 'Nombre patrullero', bold)
                sheet.write('X1', 'Observaciones de servicio', bold)
                sheet.write('Y1', 'Coordinador a cargo', bold)
                sheet.write('Z1', 'Descripción', bold)
                sheet.write('AA1', 'Área', bold)
                
                

                for i in self.reportePatrulla:                    
                    if i[26] == self.areaAnalista and self.rolAnalista == "ANALISTA":
                        incremento = 0
                        for j in i:
                            sheet.write(fila, columna + incremento, str(j))
                            incremento += 1
                        fila += 1
                    elif self.rolAnalista == "COORDINADOR":
                        incremento = 0
                        for j in i:
                            sheet.write(fila, columna + incremento, str(j))
                            incremento += 1
                        fila += 1
                
                workbook.close()

    def reportesEliminados(self):
        fila = 1
        columna = 0

        self.reportePatrullaEliminado = conexion.conexion().mostrarPatrullasEliminadas()

        workbook = xlsxwriter.Workbook('patrullaje_eliminados.xlsx')
        sheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        sheet.write('A1', 'No.', bold)
        sheet.write('B1', 'Fecha', bold)
        sheet.write('C1', 'Código', bold)
        sheet.write('D1', 'Nombre', bold)
        sheet.write('E1', 'Motivo', bold)
        sheet.write('F1', 'Área', bold)

        for i in self.reportePatrullaEliminado:
            incremento = 0
            for j in i:
                sheet.write(fila, columna + incremento, str(j))
                incremento += 1
            fila += 1
        workbook.close()
 
    #***************************************

    def addPatrulla(self):
        if self.txtCodigo.get() == "":  
            messagebox.showerror("Error", "Debe ingresar un codigo")
        elif self.cbxMotivo.get()=="":
            messagebox.showerror("Error", "Debe seleccionar un motivo")
        elif self.txtCodigo.get() == "" and self.cbxMotivo.get()=="":
            messagebox.showerror("Error", "Debe llenar los campos codigo y motivo")
        else:
            self.cantidadPatrullas()
            self.i += 1

            #Se calcula el tiempo de respuesta en que llego la patrulla
            if self.txtHoraLlegada.get()=="":
                pass
            else:   
                self.tiempoRealRespuesta = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))

                #Se calcula el tiempo de excedente de la patrualla
                self.excedenteTiempo = str(self.restarHoras(self.tiempoRealRespuesta[:-3], self.tiempoRespuesta[:-3]))

                if self.excedenteTiempo < "00:00:00":
                    self.excedenteTiempo = "00:00:00"

                if self.txtHoraRetiro.get() != "":             
                    self.duracionServicio = str(self.restarHoras(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))

        

            fecha = datetime.datetime.now()
            fechaAux = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year) 
            self.patrulla = conexion.conexion().addPatrulla(self.i, fechaAux, self.codigoBi, self.centroCosto, self.puntoBi, 
                                                            self.nombreBi, self.ubicacion, self.direccion, self.cbxMotivo.get(), 
                                                            self.autorizado, self.txtCodigoConfirmacion.get(), self.proveedor, 
                                                            self.tiempoRespuesta, self.txtHoraSolicitud.get(), self.txtHoraLlegada.get(), 
                                                            self.tiempoRealRespuesta, self.excedenteTiempo, self.txtHoraRetiro.get(), 
                                                            self.duracionServicio, self.nombreAnalista,self.txtNombreOperador.get(), self.txtNumeroBoleta.get(), 
                                                            self.txtNombrePatrullero.get(), self.txtObservacionServicio.get(1.0, END+"-1c"), 
                                                            self.coordinador, self.txtDescripcion.get(1.0, END+"-1c"), self.areaAnalista)
            self.mostrarPatrullas()
            self.limpiarCampos()
       
    def cantidadPatrullas(self):
        self.mPatrulla = conexion.conexion().mostrarPatrulla()

        if self.mPatrulla == []:
            self.i = 0
        else:
            patrullaAux = self.mPatrulla[-1]

            self.i = patrullaAux[0]

    def mostrarPatrullas(self):
        
        registros = self.tabla.get_children()
        for registro in registros:
            self.tabla.delete(registro)
        
        self.mPatrulla = conexion.conexion().mostrarPatrulla()

        for i in self.mPatrulla:
            if i[26] == self.areaAnalista and self.rolAnalista == "ANALISTA":
                if i[1] == self.fechaPrincipal:
                    #14 -> llegada i[17]-> Retiro #21 -> Numero de Boleta -> Observacion del servicio
                    if i[14] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')
            elif self.rolAnalista == "COORDINADOR":
                if i[1] == self.fechaPrincipal:
                    #14 -> llegada i[17]-> Retiro #21 -> Numero de Boleta -> Observacion del servicio
                    if i[14] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')

    def limpiarCampos(self):
        self.lblNombreBi['text'] = "Nombre: "
        self.lblAutorizadoSINO['text'] = "N/A"
        self.lblAutorizadoSINO.config(fg="#000000", font=("Comic Sans MS", 15, 'bold'))
        self.txtCodigo.delete(0, END)
        self.txtCodigo.focus()
        self.txtCodigoConfirmacion.delete(0, END)
        self.txtCodigoConfirmacion.insert(END, "N/A");
        self.txtHoraSolicitud.delete(0, END)
        self.txtHoraLlegada.delete(0, END)
        self.txtHoraRetiro.delete(0, END)
        self.txtNombreOperador.delete(0, END)
        self.txtNumeroBoleta.delete(0, END)
        self.txtNombrePatrullero.delete(0, END)

        self.txtObservacionServicio.delete(1.0, END)
        self.txtDescripcion.delete(1.0, END)
        #self.txtCodigoSearch.delete(1.0, END)

    def editarPatrulla(self):

        if self.txtHoraLlegada.get()!="": 
            self.tiempoRealRespuesta = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))
            
            #Se calcula el tiempo de excedente de la patrualla
            self.excedenteTiempo = str(self.restarHoras(self.tiempoRealRespuesta[:-3], self.tiempoRespuesta[:-3]))

            if self.excedenteTiempo < "00:00:00":
               self.excedenteTiempo = "00:00:00"

            if self.txtHoraRetiro.get() != "":             
                self.duracionServicio = str(self.restarHoras(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))

        self.editPatrulla = conexion.conexion().editarDatosPatrulla(self.no, self.codigoBi, 
                                                                    self.cbxMotivo.get(), self.txtCodigoConfirmacion.get(),
                                                                    self.txtHoraSolicitud.get(), self.txtHoraLlegada.get(), 
                                                                    self.tiempoRealRespuesta, self.excedenteTiempo,
                                                                    self.txtHoraRetiro.get(), self.duracionServicio, self.txtNombreOperador.get(),
                                                                    self.txtNumeroBoleta.get(), self.txtNombrePatrullero.get(),
                                                                    self.txtObservacionServicio.get(1.0, END+"-1c"), self.txtDescripcion.get(1.0, END+"-1c"))
        self.txtCodigoSearch.delete(0, END)
        self.limpiarCampos()
        self.mostrarPatrullas()
        self.btnEliminar["state"] = "disable"
        self.btnAceptar["state"] = "normal"
        self.btnGuardar["state"] = "disable"

    def doubleClickTabla(self, event):
        self.limpiarCampos()
        self.txtCodigoConfirmacion.delete(0, END)
        
        #Agregar los campos para vaciar
        self.btnEliminar["state"] = "normal"
        self.btnAceptar["state"] = "disable"
        self.btnGuardar["state"] = "normal"

        self.no=self.tabla.item(self.tabla.selection())["text"]
        self.codigoBi=self.tabla.item(self.tabla.selection())["values"][0]
        motivo=self.tabla.item(self.tabla.selection())["values"][1]
        analista=self.tabla.item(self.tabla.selection())["values"][2]

        self.patrullaEdit = conexion.conexion().buscarPatrulla(self.no, self.codigoBi, motivo, analista)

        for opciones in self.cbxMotivo["values"]:
            if opciones == motivo:
                self.cbxMotivo.current(self.cbxMotivo["values"].index(opciones))

        for i in self.patrullaEdit:

            self.fechaCordinacion = str(i[1])
            self.txtCodigo.insert(END, i[2])
            self.nombreBi = str(i[5])
            self.txtCodigoConfirmacion.insert(END, i[10])
            
            self.tiempoRespuesta = str(i[12])

            horaSolicitudAux = str(i[13])
            self.txtHoraSolicitud.insert(END, horaSolicitudAux[:-3])

            horaLlegadaAux = str(i[14])
            if horaLlegadaAux == "0:00:00":
                self.txtHoraLlegada.insert(END, "")
            else:
                self.txtHoraLlegada.insert(END, horaLlegadaAux[:-3])

            self.excedente = str(i[16])
            self.duracion = str(i[18])


            horaRetiroAux = str(i[17])
            if horaRetiroAux == "0:00:00":
                self.txtHoraRetiro.insert(END, "")
            else:
                self.txtHoraRetiro.insert(END, horaRetiroAux[:-3])


            self.txtNombreOperador.insert(END, i[20])
            self.txtNumeroBoleta.insert(END, i[21])
            self.txtNombrePatrullero.insert(END, i[22])
            self.txtObservacionServicio.insert(END, i[23])
            self.txtDescripcion.insert(END, i[25])

            self.areaAnalistaAux = str(i[26])
            
        

        #Se agrega en los campos txt 


    def eliminarPatrulla(self):

        validacion = simpledialog.askstring("Eliminar", "¿Motivo del por cual se elimina la patrulla?")

        if validacion == None:
            pass
        else:
            self.delete = conexion.conexion().eliminarPatrulla(self.no, self.codigoBi)

            self.cantidadPatrullasEliminadas()
            self.iEliminadas += 1
            self.addDelete = conexion.conexion().addPatrullaEliminada(self.iEliminadas, self.fechaCordinacion,self.codigoBi, self.nombreBi, validacion, self.areaAnalistaAux)

        self.txtCodigoSearch.delete(0, END)
        self.limpiarCampos()
        self.mostrarPatrullas()

        self.btnEliminar["state"] = "disable"
        self.btnAceptar["state"] = "normal"
        self.btnGuardar["state"] = "disable"

    def cantidadPatrullasEliminadas(self):
        self.mPatrulla = conexion.conexion().mostrarPatrullasEliminadas()

        if self.mPatrulla == []:
            self.iEliminadas = 0
        else:
            patrullaAux = self.mPatrulla[-1]

            self.iEliminadas = patrullaAux[0]

    def restarHoras(self, hora1, hora2):
        hora1 = datetime.datetime.strptime(hora1, "%H:%M")
        hora2 = datetime.datetime.strptime(hora2, "%H:%M")
        resta = hora1 - hora2
        return resta

    #Buscar patrulla por codigo
    def searchPatrulla(self, event):

        registros = self.tabla.get_children()
        for registro in registros:
            self.tabla.delete(registro)

            
        self.conexion = conexion.conexion().searchPatrulla(self.txtCodigoSearch.get())

        if self.txtCodigoSearch.get() != "":
            for i in self.conexion:
                if i[26] == self.areaAnalista and self.rolAnalista == "ANALISTA":
                    #14 -> llegada i[17]-> Retiro #21 -> Numero de Boleta -> Observacion del servicio
                    if i[14] == "" or i[17] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "" :
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')
                elif self.rolAnalista == "COORDINADOR":
                    if i[14] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')
        else: 
            self.mostrarPatrullas()