from tkinter import *
from tkinter import ttk
import datetime
from conexion import conexion

class VentanaPatrullaje:

    def __init__(self):
        #VENTANA
        self.ventana = Tk()
        self.ventana.title('Patrullaje Bi')
        self.ventana.resizable(False, False)
        self.ventana.geometry("1350x750")

        #Variables
        fecha = datetime.datetime.now()
        fechaAux = str(fecha.day) +"-"+ str(fecha.month) +"-"+ str(fecha.year)
        self.opc = IntVar()

        self.codigo = StringVar()
        self.codigoConfirmacion = StringVar()

        self.horaSolicitud = StringVar()
        self.horaLlegada = StringVar()
        self.horaRetiro = StringVar()
        self.codigoConfirmacion = StringVar()
        
        self.nombreOperador = StringVar()
        self.numeroBoleta = StringVar()
        self.nombrePatrullero = StringVar()

        #Widgets -----> Apartado 1
        self.marcoPrincipal = Frame(self.ventana)
        self.marcoPrincipal.config(bg="#dcffff", width=1350, height=750)
        self.lblTitulo = Label(self.marcoPrincipal, text="\t\t\t\t\tPatrullaje Bi" + "\t\t\t    Fecha: " + fechaAux)
        self.lblTitulo.config(bg="#325795", width=1350, anchor="w", height=1, font=("Rockwell", 20, 'bold'), foreground="#FFFFFF", relief=RAISED)

        #Widgets -----> Apartado 1
        self.lblOperadorBi = Label(self.marcoPrincipal, text="Operador Bi")
        self.lblOperadorBi.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'))
        self.rbAlarmas  = Radiobutton(self.marcoPrincipal, text="Alarmas", variable= self.opc, value=1)
        self.rbAlarmas.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.rbCctv  = Radiobutton(self.marcoPrincipal, text="Cctv", variable= self.opc, value=2)
        self.rbCctv.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.rbClaves  = Radiobutton(self.marcoPrincipal, text="Claves", variable= self.opc, value=3)
        self.rbClaves.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.cbxOperador = ttk.Combobox(self.marcoPrincipal, width=25)
        self.cbxOperador.config(font=("Comic Sans MS", 12), width=10)
        self.lblCoordinador = Label(self.marcoPrincipal, text="Coordinador a cargo")
        self.lblCoordinador.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'))
        self.cbxCoordinador = ttk.Combobox(self.marcoPrincipal, width=25)
        self.cbxCoordinador.config(font=("Comic Sans MS", 12), width=10)

        #Widgets -----> Apartado 2
        self.lblNombreBi = Label(self.marcoPrincipal, text="Nombre: Este es un ejemplo de una agencia con texto largo (A080)")
        self.lblNombreBi.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'))
        self.lblCodigo = Label(self.marcoPrincipal, text="Código:")
        self.lblCodigo.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigo = Entry(self.marcoPrincipal, textvariable=self.codigo)
        self.txtCodigo.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=10)
        self.btnBuscar = Button(self.marcoPrincipal, text="Buscar", command=self.buscarPuntoBi)
        self.btnBuscar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnDetalles = Button(self.marcoPrincipal, text="Detalles")
        self.btnDetalles.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.lblAutorizado = Label(self.marcoPrincipal, text="Autorizado para abastecimiento:")
        self.lblAutorizado.config(bg="#dcffff", font=("Comic Sans MS", 11))
        self.lblAutorizadoSINO = Label(self.marcoPrincipal, text="SI/NO")
        self.lblAutorizadoSINO.config(bg="#dcffff", font=("Comic Sans MS", 15, 'bold'))
        self.lblCodigoConfirmacion = Label(self.marcoPrincipal, text="Código de confirmación")
        self.lblCodigoConfirmacion.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.lblJefePatrullero = Label(self.marcoPrincipal, text="(Jefe / Patrullero)")
        self.lblJefePatrullero.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.txtCodigoConfirmacion = Entry(self.marcoPrincipal, textvariable=self.codigoConfirmacion)
        self.txtCodigoConfirmacion.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=8)
        self.lblProveedor = Label(self.marcoPrincipal, text="Proveedor")
        self.lblProveedor.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.cbxProveedor = ttk.Combobox(self.marcoPrincipal, background="#F4F4F4", width=25, values=["Bi", "Ebano", "Wackenhut"])
        self.cbxProveedor.config(font=("Comic Sans MS", 12), width=10)

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

        #separador-----> Apartado 1
        self.separador1h = ttk.Separator(self.marcoPrincipal, orient="horizontal")
        self.separador1v = ttk.Separator(self.marcoPrincipal, orient="vertical")
        #separador-----> Apartado 2
        self.separador2h = ttk.Separator(self.marcoPrincipal, orient="horizontal")
        self.separador2v = ttk.Separator(self.marcoPrincipal, orient="vertical")
        

    def mostrarVentana(self):
        self.marcoPrincipal.place (x=0,y=0)
        self.lblTitulo.place(x=0, y=0)

       #Widgets -----> Apartado 1
        self.rbAlarmas.place(x=20, y=40)
        self.rbCctv.place(x=20, y=65)
        self.rbClaves.place(x=20, y=90)
        self.lblOperadorBi.place(x=160, y=50)
        self.lblCoordinador.place(x=325, y=50)
        self.cbxOperador.place(x=160, y=75)
        self.cbxCoordinador.place(x=350, y=75)

         #Widgets -----> Apartado 2
        self.lblNombreBi.place(x=10, y=145)
        self.lblCodigo.place(x=10, y=205)
        self.txtCodigo.place(x=90, y=205)
        self.btnBuscar.place(x=210, y=185)
        self.btnDetalles.place(x=210, y=230)
        self.lblAutorizado.place(x=300, y=175)
        self.lblAutorizadoSINO.place(x=380, y=225)
        self.lblCodigoConfirmacion.place(x=5 , y=290)
        self.lblJefePatrullero.place(x=20 , y=315)
        self.txtCodigoConfirmacion.place(x=208, y=305)
        self.lblProveedor.place(x=360, y=280)
        self.cbxProveedor.place(x=340, y=305)

         #Widgets -----> Apartado 3
        self.lblHoraSolicitud.place(x=50 , y=375)
        self.txtHoraSolicitud.place(x=80 , y=430)
        self.lblHoraLlegada.place(x=90 , y=460) 
        self.txtHoraLlegada.place(x=80 , y=490)
        self.lblHoraRetiro.place(x=90 , y=520)
        self.txtHoraRetiro.place(x=80 , y=550)

        #Widgets -----> Apartado 4
        self.lblNombreOperador.place(x=365, y=385)
        self.txtNombreOperador.place(x=325,y=430)
        self.lblNumeroBoleta.place(x=365, y=460)
        self.txtNumeroBoleta.place(x=325,y=490)
        self.lblNombrePatrullero.place(x=365,y=520)
        self.txtNombrePatrullero.place(x=325,y=550)

        #Separador -----> Apartado 1
        self.separador1h.place(relx=0, rely=0.175, relheight=0.002, relwidth=0.420)
        self.separador1v.place(relx=0.42, rely=0.052, relheight=1, relwidth=0.002)
        self.separador2h.place(relx=0, rely=0.475, relheight=0.002, relwidth=0.420)

        self.separador2v.place(relx=0.21, rely=0.475, relheight=0.4, relwidth=0.002)

        self.ventana.mainloop()

    def buscarPuntoBi(self):
        
        self.conexion = conexion.conexion().buscarPuntoBi(self.codigo.get())
        print(self.conexion)