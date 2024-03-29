import tkinter
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import datetime
from conexion import conexion
import xlsxwriter

from concurrent.futures import ThreadPoolExecutor


class VentanaPatrullaje:

    def __init__(self, login, nombreAnalista, coordinador, areaAnalista, rolAnalista):
    #def __init__(self):
        #VENTANA
        self.login = login
        self.ventana = Toplevel(login)
        self.ventana.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        #self.ventana = Tk()
        self.ventana.title('Patrullaje Bi')
        self.ventana.resizable(False, False)
        self.ventana.geometry("1272x475")

        #Variables
        fecha = datetime.datetime.now()
        self.fechaPrincipal = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year)
        self.opc = IntVar()

        #**************************************************************************************************************
        self.tablaAux = []
        #**************************************************************************************************************
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
        self.tiempoRespuestaAbasto = StringVar()
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
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label = "Reporte por operador", command=self.reporteOperadores)
        self.menuArchivo.add_command(label = "Reporte por código", command=self.reporteCodigo)
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Cerrar Sesión", command=self.on_closing)

        self.barraMenu.add_cascade(menu=self.menuArchivo, label="Archivo")
        self.ventana.config(menu=self.barraMenu)


        #Widgets -----> Apartado 1
        self.marcoPrincipal = Frame(self.ventana)
        self.marcoPrincipal.config(bg="#dcffff", width=1350, height=750)
        self.lblTitulo = Label(self.marcoPrincipal, text="\t\t\tCentro de Recepción de Alarmas" + "\t\t\t    " + self.fechaPrincipal)
        self.lblTitulo.config(bg="#325795", width=1350, anchor="w", height=1, font=("Rockwell", 20, 'bold'), foreground="#FFFFFF", relief=RAISED)

        #Widgets -----> Apartado 2
        self.lblNombreBi = Label(self.marcoPrincipal, text="Punto de servicio")
        self.lblNombreBi.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'))
        self.lblCodigo = Label(self.marcoPrincipal, text="Código:")
        self.lblCodigo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigo = Entry(self.marcoPrincipal, textvariable=self.codigo)
        self.txtCodigo.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=7)
        self.txtCodigo.bind("<Return>", self.buscarPuntoBi)

        self.btnDetalles = Button(self.marcoPrincipal, text="Detalles", command=self.informacioPuntoBi)
        self.btnDetalles.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.lblAutorizado = Label(self.marcoPrincipal, text="Autorizado ABS:")
        self.lblAutorizado.config(bg="#dcffff", font=("Comic Sans MS", 11))
        self.lblAutorizadoSINO = Label(self.marcoPrincipal, text="SI/NO")
        self.lblAutorizadoSINO.config(bg="#dcffff", font=("Comic Sans MS", 15, 'bold'))
        self.lblMotivo = Label(self.marcoPrincipal, text="Motivo")
        self.lblMotivo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.cbxMotivo = ttk.Combobox(self.marcoPrincipal, background="#F4F4F4", state="readonly", width=25)
        self.cbxMotivo.config(font=("Comic Sans MS", 12), width=15)
        self.lblCodigoConfirmacion = Label(self.marcoPrincipal, text="Confirmación")
        self.lblCodigoConfirmacion.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigoConfirmacion = Entry(self.marcoPrincipal, textvariable=self.codigoConfirmacion)
        self.txtCodigoConfirmacion.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=8)
        self.txtCodigoConfirmacion.insert(END, "N/A");

        #Widgets -----> Apartado 3
        self.lblHoraSolicitud = Label(self.marcoPrincipal, text="Solicitud CRA")
        self.lblHoraSolicitud.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtHoraSolicitud = Entry(self.marcoPrincipal, textvariable=self.horaSolicitud)
        self.txtHoraSolicitud.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=8)

        self.lblNombreOperador = Label(self.marcoPrincipal, text="Operador")
        self.lblNombreOperador.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtNombreOperador = Entry(self.marcoPrincipal, textvariable=self.nombreOperador)
        self.txtNombreOperador.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)

        self.btnAceptar = Button(self.marcoPrincipal, text="Aceptar", command=self.addPatrulla)
        self.btnAceptar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))

        
        self.lblHoraLlegada = Label(self.marcoPrincipal, text="Llegada")
        self.lblHoraLlegada.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtHoraLlegada = Entry(self.marcoPrincipal, textvariable=self.horaLlegada)
        self.txtHoraLlegada.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=8)     
        self.lblHoraRetiro = Label(self.marcoPrincipal, text="Retiro")
        self.lblHoraRetiro.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtHoraRetiro = Entry(self.marcoPrincipal, textvariable=self.horaRetiro)
        self.txtHoraRetiro.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=8)
        self.lblNota = Label(self.marcoPrincipal, text="* Formato 24 Horas *")
        self.lblNota.config(bg="#dcffff", font=("Comic Sans MS", 9))

        #Widgets -----> Apartado 4
        
        self.lblNumeroBoleta = Label(self.marcoPrincipal, text="Boleta")
        self.lblNumeroBoleta.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtNumeroBoleta = Entry(self.marcoPrincipal, textvariable=self.numeroBoleta)
        self.txtNumeroBoleta.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblNombrePatrullero = Label(self.marcoPrincipal, text="Patrullero")
        self.lblNombrePatrullero.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtNombrePatrullero = Entry(self.marcoPrincipal, textvariable=self.nombrePatrullero)
        self.txtNombrePatrullero.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)

         #Widgets -----> Apartado 5

        self.lblDescripcion = Label(self.marcoPrincipal, text="Descripción")
        self.lblDescripcion.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtDescripcion = Text(self.marcoPrincipal)
        self.txtDescripcion.config(bg="#F4F4F4", font=("Comic Sans MS", 12), height = 8, width = 40, wrap=WORD)
        self.lblObservacionServicio = Label(self.marcoPrincipal, text="Observaciones")
        self.lblObservacionServicio.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtObservacionServicio = Text(self.marcoPrincipal)
        self.txtObservacionServicio.config(bg="#F4F4F4", font=("Comic Sans MS", 12), height = 4, width = 40, wrap=WORD)
        self.btnGuardar = Button(self.marcoPrincipal, text="Guardar", command=self.editarPatrulla)
        self.btnGuardar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))

        
        
        

        self.lblSearchCodigo = Label(self.marcoPrincipal, text="Código")
        self.lblSearchCodigo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigoSearch = Entry(self.marcoPrincipal)
        self.txtCodigoSearch.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=7)
        self.txtCodigoSearch.bind("<Return>", self.searchPatrulla)

        self.lblPatrullasEnviadas = Label(self.marcoPrincipal, text="Patrullas enviadas")
        self.lblPatrullasEnviadas.config(bg="#dcffff", font=("Comic Sans MS", 12))
        #Creacion de la tabla de patrullas enviadas
        columnas = ('#0', '#1', '#2', '#3')
        self.tabla = ttk.Treeview(self.marcoPrincipal, height=13,  columns=columnas)
        self.tabla.bind("<Double-Button-1>", self.doubleClickTabla)
        self.tabla.column('#0', width=30)       
        self.tabla.heading('#0', text='No', anchor=CENTER)
        self.tabla.column('#1', width=60)
        self.tabla.heading('#1', text='Fecha', anchor=CENTER)
        self.tabla.column('#2', width=60)        
        self.tabla.heading('#2', text='Cod', anchor=CENTER)
        self.tabla.column('#3', width=70)        
        self.tabla.heading('#3', text='Motivo', anchor=CENTER)
        self.tabla.column('#4', width=80)        
        self.tabla.heading('#4', text='Operador', anchor=CENTER)

        self.btnEliminar = Button(self.marcoPrincipal, text="Eliminar", command=self.eliminarPatrulla)
        self.btnEliminar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))

        

        #separador-----> Apartado 1
        self.separador1v = ttk.Separator(self.marcoPrincipal, orient="vertical")
        #separador-----> Apartado 2
        self.separador2h = ttk.Separator(self.marcoPrincipal, orient="horizontal")
        self.separador2v = ttk.Separator(self.marcoPrincipal, orient="vertical")

        self.separador3v = ttk.Separator(self.marcoPrincipal, orient="vertical")

        #Atajos de teclado
        #self.ventana.bind("<F1>", self.addPatrulla)
        #self.ventana.bind("<F2>", self.editarPatrulla)
        #self.ventana.bind("<F3>", self.eliminarPatrulla)
        self.btnDetalles.bind("<Return>", self.informacioPuntoBi)
        self.btnAceptar.bind("<Return>", self.addPatrulla)
        self.btnGuardar.bind("<Return>", self.editarPatrulla)
        self.btnEliminar.bind("<Return>", self.eliminarPatrulla)

        self.txtDescripcion.bind("<Tab>", self.on_tab1)
        self.txtObservacionServicio.bind("<Tab>", self.on_tab2)
        self.ventana.bind("<F3>", self.addPatrulla)
        self.ventana.bind("<F5>", self.searchPatrulla)

    def on_closing(self):
        patrullasPendientes = 0
        patrullasEnProceso = 0
        patrullasFinalizadas = 0
        estadoPatrulla = []

        for i in self.tabla.tag_has('pendiente'):
            patrullasPendientes += 1

        for j in self.tabla.tag_has('pendienteFinalizacion'):
            patrullasEnProceso += 1

        for k in self.tabla.tag_has('finalizados'):
            patrullasFinalizadas += 1

        messagebox.showinfo("Resumen", "Patrullas pendientes: " + str(patrullasPendientes) + "\nPatrullas en proceso: " + str(patrullasEnProceso) + "\nPatrullas finalizadas: " + str(patrullasFinalizadas))
    
        self.ventana.destroy()

    def mostrarVentana(self):
        self.marcoPrincipal.place (x=0,y=0)
        self.lblTitulo.place(x=0, y=0)



         #Widgets -----> Apartado 2
        self.lblCodigo.place(x=10, y=50)
        self.txtCodigo.place(x=80, y=50)
        self.btnDetalles.place(x=180, y=45)
        self.lblNombreBi.place(x=10, y=92)
        self.lblAutorizado.place(x=310, y=160)
        self.lblAutorizadoSINO.place(x=350, y=200)
        self.lblMotivo.place(x=10, y=140)
        self.cbxMotivo.place(x=80, y=140)
        self.lblCodigoConfirmacion.place(x=10 , y=190)
        self.txtCodigoConfirmacion.place(x=155, y=190)

        self.lblHoraSolicitud.place(x=10 , y=240)
        self.txtHoraSolicitud.place(x=155 , y=240)
        self.lblNombreOperador.place(x=10, y=290)
        self.txtNombreOperador.place(x=150,y=290)

        self.btnAceptar.place(x=385,y=280)

         #Widgets -----> Apartado 3  415 460
        
        self.lblHoraLlegada.place(x=10 , y=360) 
        self.txtHoraLlegada.place(x=80 , y=360)
        self.lblHoraRetiro.place(x=10 , y=410)
        self.txtHoraRetiro.place(x=80 , y=410)
        self.lblNota.place(x=20 , y=440)

        #Widgets -----> Apartado 4
        
        self.lblNumeroBoleta.place(x=175, y=360)
        self.txtNumeroBoleta.place(x=265,y=360)
        self.lblNombrePatrullero.place(x=175,y=410)
        self.txtNombrePatrullero.place(x=265,y=410)

        #Widgets -----> Apartado 5
        self.lblDescripcion.place(x=505,y=50)
        self.txtDescripcion.place(x=505,y=85)
        self.lblObservacionServicio.place(x=505,y=280) 
        self.txtObservacionServicio.place(x=505,y=315)
        self.btnGuardar.place(x=825,y=420)

        self.btnEliminar.place(x=1173,y=420)
        

        # ** Creacion de la tabla con los datos de las patrullas enviadas **
        self.lblSearchCodigo.place(x=940, y=50)
        self.txtCodigoSearch.place(x=1000, y=55)
        self.lblPatrullasEnviadas.place(x=1050, y=90)
        self.tabla.place(x=950, y=120)

        #Separador -----> Apartado 1
        self.separador1v.place(relx=0.36, rely=0.052, relheight=1, relwidth=0.002)
        self.separador2h.place(relx=0, rely=0.450, relheight=0.002, relwidth=0.36)

        #self.separador2v.place(relx=0.21, rely=0.525, relheight=0.4, relwidth=0.002)
        self.separador3v.place(relx=0.69, rely=0.052, relheight=1, relwidth=0.002)

        self.btnGuardar["state"] = "disable"
        self.btnEliminar["state"] = "disable"

        self.txtCodigo.focus()

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
                self.tiempoRespuestaAbasto = i[8]
                self.autorizado = i[10]


                if i[10] == "SI":
                    self.lblAutorizadoSINO['text'] = "SI"
                    self.lblAutorizadoSINO.config(fg="#008000", font=("Comic Sans MS", 15, 'bold'))
                elif i[10] == "NO":
                    self.lblAutorizadoSINO['text'] = "NO"
                    self.lblAutorizadoSINO.config(fg="#cc0605", font=("Comic Sans MS", 15, 'bold'))
                else:
                    self.lblAutorizadoSINO['text'] = "N/A"
                    self.lblAutorizadoSINO.config(fg="#000000", font=("Comic Sans MS", 15, 'bold'))

                self.lblNombreBi['text'] =i[4]

            
                self.txtHoraSolicitud.insert(0, datetime.datetime.now().strftime("%H:%M"))

    def informacioPuntoBi(self, event=None):

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
            elif self.txtHoraSolicitud.get() != "" and self.txtHoraLlegada.get() != "":
                tiempoRealRespuestaAux = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))

                excedenteTiempoAux = str(self.restarHoras(tiempoRealRespuestaAux[:-3], self.tiempoRespuesta[:-3]))

                if excedenteTiempoAux < "00:00:00":
                    excedenteTiempoAux = "00:00:00"
                    if self.txtHoraRetiro.get() == "":
                        duracionServicioAux = str(self.restarHorasFinalizacion(horaActualAux, self.txtHoraLlegada.get()))
                    elif self.txtHoraRetiro.get() != "":
                        duracionServicioAux = str(self.restarHorasFinalizacion(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))
                else:
                    if self.txtHoraRetiro.get() == "":
                        duracionServicioAux = str(self.restarHorasFinalizacion(horaActualAux, self.txtHoraLlegada.get()))
                    elif self.txtHoraRetiro.get() != "":
                        duracionServicioAux = str(self.restarHorasFinalizacion(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))


        for i in self.conexion:
            puntoBi = i[3]
            name = i[4]
            direccion = i[6]
            tiempoRespuesta = i[7]
            tiempoRespuestaAbasto = i[8]
        

        messagebox.showinfo(puntoBi, """Nombre: {} \nDirección: {} \nTiempo de respuesta: {}\n Tiempo de respuesta abasto: {}\n--------------------------------\nFecha de coordinación: {} \nExcedente de tiempo: {}\nDuración del servicio: {}\nÁrea: {}"""
                            .format(name, direccion, tiempoRespuesta, tiempoRespuestaAbasto, self.fechaCordinacion, 
                                    excedenteTiempoAux, duracionServicioAux, self.areaAnalistaAux))
        
    def motivosPatrulla(self):
        motivos = []

        self.motivos = conexion.conexion().descripcionMotivo(self.areaAnalista)

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
                
                
                
                workbook = xlsxwriter.Workbook('patrullaje_'+fecha+ self.areaAnalista + '.xlsx')
                sheet = workbook.add_worksheet()
                for i in self.reportePatrulla:      
                    print(self.areaAnalista)         
                    if i[26] == self.areaAnalista and self.rolAnalista == "ANALISTA" :
                        
                        if self.areaAnalista == "CLAVES":
                            

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

                            incremento = 0
                            for j in i:
                                sheet.write(fila, columna + incremento, str(j))
                                incremento += 1
                            fila += 1
                            

                        else:

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
                            #sheet.write('J1', 'Autorizado para abastecimiento', bold)   9
                            #sheet.write('K1', 'Codigo de confirmación (Jefe/Patrullero)', bold)   10
                            sheet.write('J1', 'Proveedor', bold)
                            sheet.write('K1', 'Tiempo de respuesta Ebano', bold)
                            sheet.write('L1', 'Hora solicitud central Bi', bold)
                            sheet.write('M1', 'Hora llegada', bold)
                            sheet.write('N1', 'Tiempo real de respuesta', bold)
                            sheet.write('O1', 'Excedente de tiempo', bold)
                            sheet.write('P1', 'Retiro', bold)
                            sheet.write('Q1', 'Duración del servicio', bold)
                            sheet.write('R1', 'Operador BI', bold)
                            sheet.write('S1', 'Nombre de operador', bold)
                            sheet.write('T1', 'Número de boleta', bold)
                            sheet.write('U1', 'Nombre patrullero', bold)
                            sheet.write('V1', 'Observaciones de servicio', bold)
                            sheet.write('W1', 'Coordinador a cargo', bold)
                            sheet.write('X1', 'Descripción', bold)
                            sheet.write('Y1', 'Área', bold)

                            incremento = 0
                            for j in i:
                                if incremento < 9:
                                    sheet.write(fila, columna + incremento, str(j))
                                    incremento += 1
                                elif incremento == 9 or incremento == 10:
                                    incremento += 1
                                else:
                                    sheet.write(fila, columna + incremento - 2, str(j))
                                    incremento += 1
                            fila += 1
                
                    elif self.rolAnalista == "COORDINADOR":
                        if self.areaAnalista == "CLAVES":
                            
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

                            incremento = 0
                            for j in i:
                                sheet.write(fila, columna + incremento, str(j))
                                incremento += 1
                            fila += 1

                        else:
                            
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
                            #sheet.write('J1', 'Autorizado para abastecimiento', bold)   9
                            #sheet.write('K1', 'Codigo de confirmación (Jefe/Patrullero)', bold)   10
                            sheet.write('J1', 'Proveedor', bold)
                            sheet.write('K1', 'Tiempo de respuesta Ebano', bold)
                            sheet.write('L1', 'Hora solicitud central Bi', bold)
                            sheet.write('M1', 'Hora llegada', bold)
                            sheet.write('N1', 'Tiempo real de respuesta', bold)
                            sheet.write('O1', 'Excedente de tiempo', bold)
                            sheet.write('P1', 'Retiro', bold)
                            sheet.write('Q1', 'Duración del servicio', bold)
                            sheet.write('R1', 'Operador BI', bold)
                            sheet.write('S1', 'Nombre de operador', bold)
                            sheet.write('T1', 'Número de boleta', bold)
                            sheet.write('U1', 'Nombre patrullero', bold)
                            sheet.write('V1', 'Observaciones de servicio', bold)
                            sheet.write('W1', 'Coordinador a cargo', bold)
                            sheet.write('X1', 'Descripción', bold)
                            sheet.write('Y1', 'Área', bold)

                            incremento = 0
                            for j in i:
                                if incremento < 9:
                                    sheet.write(fila, columna + incremento, str(j))
                                    incremento += 1
                                elif incremento == 9 or incremento == 10:
                                    incremento += 1
                                else:
                                    sheet.write(fila, columna + incremento - 2, str(j))
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
 
    def reporteOperadores(self):
        fila = 1
        columna = 0
        analista = ""
        operador = simpledialog.askstring("Reporte de operador", "¿Patrullas que envio el operador (Corporativo)?")

        if operador == NONE:
            pass
        elif operador == "":
            messagebox.showerror("Error", "Debe agregar un corporativo")
        else:
            self.reporteOperadorAux = conexion.conexion().analistasCorpBi(operador)
            for i in self.reporteOperadorAux:
                analista = i[1]
            
            self.reporteOperador = conexion.conexion().buscarPatrullaOperador(analista)

            if self.reporteOperador == []:
                messagebox.showinfo("Patrullas", "El operador {} no ha coordinado patrullas.".format(analista))
            else:
                workbook = xlsxwriter.Workbook('patrullas_por_'+analista+'.xlsx')
                sheet = workbook.add_worksheet()

                for i in self.reporteOperador:
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
                    sheet.write('L1', 'Proveedor', bold)
                    sheet.write('K1', 'Codigo de confirmación (Jefe/Patrullero)', bold)
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

                    incremento = 0
                    for j in i:
                        sheet.write(fila, columna + incremento, str(j))
                        incremento += 1
                    fila += 1
                workbook.close()

    def reporteCodigo(self):
        fila = 1
        columna = 0

        codigo = simpledialog.askstring("Reporte por codigo", "¿Patrullas al punto de servicio Bi?")

        if codigo == NONE:
            pass
        elif codigo == "":
            messagebox.showerror("Error", "Debe agregar el codigo del punto de servicio")
        else:
            self.reportePorCodigo = conexion.conexion().searchPatrulla(codigo)

            if self.reportePorCodigo == []:
                messagebox.showinfo("Patrullas", "No se han enviado patrullas al punto de servicio {}.".format(codigo))
            else:
                workbook = xlsxwriter.Workbook('patrullas_enviadas_a_'+codigo+'.xlsx')
                sheet = workbook.add_worksheet()

                for i in self.reportePorCodigo:
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
                    sheet.write('L1', 'Proveedor', bold)
                    sheet.write('K1', 'Codigo de confirmación (Jefe/Patrullero)', bold)
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

                    incremento = 0
                    for j in i:
                        sheet.write(fila, columna + incremento, str(j))
                        incremento += 1
                    fila += 1
                workbook.close()
    
    #***************************************
    def addPatrulla(self, event=None):

        self.duracionServicio = ""
        self.tiempoRealRespuesta = ""
        self.excedenteTiempo = ""
        tiempoAux = ""

        if self.txtCodigo.get() == "":  
            messagebox.showerror("Error", "Debe ingresar un codigo")
        elif self.cbxMotivo.get()=="":
            messagebox.showerror("Error", "Debe seleccionar un motivo")
        elif self.txtCodigo.get() == "" and self.cbxMotivo.get()=="":
            messagebox.showerror("Error", "Debe llenar los campos codigo y motivo")
        elif self.lblNombreBi.cget("text") == "Nombre:":
            messagebox.showerror("Error", "Debe buscar el punto BI")
        #VALIDACION DE MOTIVO (ABASTO / DISPENSADOR)
        elif self.cbxMotivo.get() == "ABASTO" or self.cbxMotivo.get() == "FALLA EN DISPENSADOR" and self.tiempoRespuestaAbasto != "N/A":
            if self.tiempoRespuestaAbasto == "N/A" or self.tiempoRespuestaAbasto == "" or self.tiempoRespuestaAbasto == None: 
                self.cantidadPatrullas()
                self.i += 1

                #Se calcula el tiempo de respuesta en que llego la patrulla
                if self.txtHoraLlegada.get()=="":
                    pass
                else:   
                    self.tiempoRealRespuesta = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))

                    #Se calcula el tiempo de excedente de la patrualla
                    self.excedenteTiempo = str(self.restarHoras(self.tiempoRealRespuesta[:-3], self.tiempoRespuesta()[:-3]))

                    if self.excedenteTiempo < "00:00:00":
                        self.excedenteTiempo = "00:00:00"

                    if self.txtHoraRetiro.get() != "":             
                        self.duracionServicio = str(self.restarHorasFinalizacion(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))
                    else: 
                        self.duracionServicio = ""
                    

            

                fecha = datetime.datetime.now()
                fechaAux = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year) 
                self.patrulla = conexion.conexion().addPatrulla(self.i, fechaAux, self.codigoBi, self.centroCosto, self.puntoBi, 
                                                                self.nombreBi, self.ubicacion, self.direccion, self.cbxMotivo.get(), 
                                                                self.autorizado, self.txtCodigoConfirmacion.get(), self.proveedor, 
                                                                self.tiempoRespuesta, self.txtHoraSolicitud.get(), self.txtHoraLlegada.get(), 
                                                                self.tiempoRealRespuesta, self.excedenteTiempo, self.txtHoraRetiro.get(), 
                                                                self.duracionServicio, self.nombreAnalista,self.txtNombreOperador.get(), self.txtNumeroBoleta.get(), 
                                                                self.txtNombrePatrullero.get(), self.txtDescripcion.get(1.0, END+"-1c"), 
                                                                self.coordinador, self.txtObservacionServicio.get(1.0, END+"-1c"), self.areaAnalista)
                self.mostrarPatrullas()
                self.limpiarCampos()
            else:
                self.cantidadPatrullas()
                self.i += 1

                #Se calcula el tiempo de respuesta en que llego la patrulla
                if self.txtHoraLlegada.get()=="":
                    pass
                else:   
                    self.tiempoRealRespuesta = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))

                    #Se calcula el tiempo de excedente de la patrualla
                    self.excedenteTiempo = str(self.restarHoras(self.tiempoRealRespuesta[:-3],  self.tiempoRespuestaAbasto()[:-3]))

                    if self.excedenteTiempo < "00:00:00":
                        self.excedenteTiempo = "00:00:00"

                    if self.txtHoraRetiro.get() != "":             
                        self.duracionServicio = str(self.restarHorasFinalizacion(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))
                    else: 
                        self.duracionServicio = ""
                        

                

                fecha = datetime.datetime.now()
                fechaAux = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year) 
                self.patrulla = conexion.conexion().addPatrulla(self.i, fechaAux, self.codigoBi, self.centroCosto, self.puntoBi, 
                                                                self.nombreBi, self.ubicacion, self.direccion, self.cbxMotivo.get(), 
                                                                self.autorizado, self.txtCodigoConfirmacion.get(), self.proveedor, 
                                                                self.tiempoRespuestaAbasto, self.txtHoraSolicitud.get(), self.txtHoraLlegada.get(), 
                                                                self.tiempoRealRespuesta, self.excedenteTiempo, self.txtHoraRetiro.get(), 
                                                                self.duracionServicio, self.nombreAnalista,self.txtNombreOperador.get(), self.txtNumeroBoleta.get(), 
                                                                self.txtNombrePatrullero.get(), self.txtDescripcion.get(1.0, END+"-1c"), 
                                                                self.coordinador, self.txtObservacionServicio.get(1.0, END+"-1c"), self.areaAnalista)
                self.mostrarPatrullas()
                self.limpiarCampos()
            
        else:
            self.cantidadPatrullas()
            self.i += 1

            #Se calcula el tiempo de respuesta en que llego la patrulla
            if self.txtHoraLlegada.get()=="":
                pass
            else:   
                self.tiempoRealRespuesta = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))

                #Se calcula el tiempo de excedente de la patrualla
                self.excedenteTiempo = str(self.restarHoras(self.tiempoRealRespuesta[:-3], self.tiempoRespuesta()[:-3]))

                if self.excedenteTiempo < "00:00:00":
                    self.excedenteTiempo = "00:00:00"

                if self.txtHoraRetiro.get() != "":             
                    self.duracionServicio = str(self.restarHorasFinalizacion(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))
                else: 
                    self.duracionServicio = ""
                

        

            fecha = datetime.datetime.now()
            fechaAux = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year) 
            self.patrulla = conexion.conexion().addPatrulla(self.i, fechaAux, self.codigoBi, self.centroCosto, self.puntoBi, 
                                                            self.nombreBi, self.ubicacion, self.direccion, self.cbxMotivo.get(), 
                                                            self.autorizado, self.txtCodigoConfirmacion.get(), self.proveedor, 
                                                            self.tiempoRespuesta, self.txtHoraSolicitud.get(), self.txtHoraLlegada.get(), 
                                                            self.tiempoRealRespuesta, self.excedenteTiempo, self.txtHoraRetiro.get(), 
                                                            self.duracionServicio, self.nombreAnalista,self.txtNombreOperador.get(), self.txtNumeroBoleta.get(), 
                                                            self.txtNombrePatrullero.get(), self.txtDescripcion.get(1.0, END+"-1c"), 
                                                            self.coordinador, self.txtObservacionServicio.get(1.0, END+"-1c"), self.areaAnalista)
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
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                        print("PENDIENTES")
                    elif i[18] == "" or i[17] == "0:00:00" or i[17] == "00:00:00" or i[17] == "0:00" or i[17] == "00:00" or i[17] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                        print("PENDIENTES FINALIZACION")
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')
                        print("FINALIZADOS")
            elif self.rolAnalista == "COORDINADOR":
                if i[1] == self.fechaPrincipal:
                    #14 -> llegada i[17]-> Retiro #21 -> Numero de Boleta -> Observacion del servicio
                    if i[14] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "" or i[17] == "0:00:00" or i[17] == "00:00:00" or i[17] == "0:00" or i[17] == "00:00" or i[17] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')

    def limpiarCampos(self):
        self.lblNombreBi['text'] = "Nombre:"
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

    def editarPatrulla(self, event=None):

        self.duracionServicio = ""
        self.tiempoRealRespuesta = ""
        self.excedenteTiempo = ""
        


        if self.txtHoraLlegada.get()!="":
            self.tiempoRealRespuesta = str(self.restarHoras(self.txtHoraLlegada.get(), self.txtHoraSolicitud.get()))
            
            #Se calcula el tiempo de excedente de la patrualla
            self.excedenteTiempo = str(self.restarHoras(self.tiempoRealRespuesta[:-3], self.tiempoRespuesta[:-3]))

            if self.excedenteTiempo < "00:00:00":
               self.excedenteTiempo = "00:00:00"
            else:
                self.btnGuardar["state"] = "disable"
                respuesta = messagebox.showinfo("Excedente de tiempo", "La patrulla excedio el tiempo de respuesta en: " + self.excedenteTiempo)

                if respuesta == "ok":
                    self.btnGuardar["state"] = "normal"
                

            if self.txtHoraRetiro.get() != "":   
                self.duracionServicio = str(self.restarHorasFinalizacion(self.txtHoraRetiro.get(), self.txtHoraLlegada.get()))
                if self.duracionServicio > "00:35:00":
                    self.btnGuardar["state"] = "disable"
                    respuesta1 = messagebox.showinfo("Duracion de servicio", "La duracion del servicio excedio 35 minutos, tiempo total: " + self.duracionServicio)                 

                    if respuesta1 == "ok":
                        self.btnGuardar["state"] = "normal"
            else:
                self.duracionServicio = ""
        
        self.editPatrulla = conexion.conexion().editarDatosPatrulla(self.no, self.codigoBi, 
                                                                    self.cbxMotivo.get(), self.txtCodigoConfirmacion.get(),
                                                                    self.txtHoraSolicitud.get(), self.txtHoraLlegada.get(), 
                                                                    self.tiempoRealRespuesta, self.excedenteTiempo,
                                                                    self.txtHoraRetiro.get(), self.duracionServicio, self.txtNombreOperador.get(),
                                                                    self.txtNumeroBoleta.get(), self.txtNombrePatrullero.get(),
                                                                    self.txtDescripcion.get(1.0, END+"-1c"), self.txtObservacionServicio.get(1.0, END+"-1c"))
        self.txtCodigoSearch.delete(0, END)
        self.limpiarCampos()
        self.mostrarPatrullas()
        self.btnEliminar["state"] = "disable"
        self.btnAceptar["state"] = "normal"
        self.btnGuardar["state"] = "disable"

    def doubleClickTabla(self, event):
        self.limpiarCampos()
        self.txtCodigoConfirmacion.delete(0, END)
        self.txtHoraLlegada.focus()
        
        #Agregar los campos para vaciar
        self.btnEliminar["state"] = "normal"
        self.btnAceptar["state"] = "disable"
        self.btnGuardar["state"] = "normal"

        self.no=self.tabla.item(self.tabla.selection())["text"]
        self.codigoBi=self.tabla.item(self.tabla.selection())["values"][1]
        motivo=self.tabla.item(self.tabla.selection())["values"][2]
        analista=self.tabla.item(self.tabla.selection())["values"][3]

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

            self.lblNombreBi['text'] = "Nombre: \t"+i[5]
            self.txtNombreOperador.insert(END, i[20])
            self.txtNumeroBoleta.insert(END, i[21])
            self.txtNombrePatrullero.insert(END, i[22])
            self.txtObservacionServicio.insert(END, i[25])
            self.txtDescripcion.insert(END, i[23])

            self.areaAnalistaAux = str(i[26])
            
        

        #Se agrega en los campos txt 

    def eliminarPatrulla(self, event=None):
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

    def restarHoras(self, finalizacion, inicio):
        finalizacion = datetime.datetime.strptime(finalizacion, "%H:%M")
        inicio = datetime.datetime.strptime(inicio, "%H:%M")
        resta = finalizacion - inicio
        return resta
    
    def restarHorasFinalizacion(self, finalizacion, inicio):
        finalizacion = datetime.datetime.strptime(finalizacion, "%H:%M")
        inicio = datetime.datetime.strptime(inicio, "%H:%M")
        resta = finalizacion - inicio

        diferencia_horas = str(resta.seconds // 3600)
        diferencia_minutos = str((resta.seconds // 60) % 60)

        if len(diferencia_horas) == 1:
            diferencia_horas = "0" + diferencia_horas
        if len(diferencia_minutos) == 1:
            diferencia_minutos = "0" + diferencia_minutos



        restaHoras = diferencia_horas + ":" + diferencia_minutos
        return restaHoras

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
                    if i[14] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "" or i[17] == "0:00:00" or i[17] == "00:00:00" or i[17] == "0:00" or i[17] == "00:00" or i[17] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')
                elif self.rolAnalista == "COORDINADOR":
                    if i[14] == "" or i[20] == "" or i[21] == "" or i[22] == "" or i[23] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendiente'))
                        self.tabla.tag_configure('pendiente', background='#CD6155')
                    elif i[18] == "" or i[17] == "0:00:00" or i[17] == "00:00:00" or i[17] == "0:00" or i[17] == "00:00" or i[17] == "":
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('pendienteFinalizacion'))
                        self.tabla.tag_configure('pendienteFinalizacion', background='#F3883F')
                    else:
                        self.tabla.insert("", 'end', text=i[0], values=(i[1],i[2], i[8], i[19]), tags=('finalizados'))
                        self.tabla.tag_configure('finalizados', background='#52BE80')
        else: 
            self.mostrarPatrullas()

        for j in self.tabla.tag_has('pendienteFinalizacion'):
            noAux = self.tabla.item(j)["text"]
            codigoBiAux = self.tabla.item(j)["values"][1]
            motivoAux = self.tabla.item(j)["values"][2]
            analistaAux = self.tabla.item(j)["values"][3]
            
            print("No: ", noAux)
            print("Codigo: ", codigoBiAux)
            print("Motivo: ", motivoAux)
            print("Analista: ", analistaAux)

    def on_tab1(self, event):
        self.txtObservacionServicio.focus()
        return 'break'
    
    def on_tab2(self, event):
        self.txtCodigoSearch.focus()
        return 'break'