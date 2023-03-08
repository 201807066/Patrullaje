from tkinter import *
from tkinter import ttk, messagebox
from conexion import conexion
from ventanas import ventanaPatrullaje


class admonUsuarios:

    def __init__(self, VentanaPatrullaje):
        self.analistas = Toplevel(VentanaPatrullaje)
        self.analistas.title("CRUD Analistas")
        self.analistas.resizable(False, False)
        self.analistas.geometry("500x585")

        #Variables
        self.bCorp = IntVar()
        self.nombre = StringVar()
        self.corp = IntVar()
        self.ant = IntVar()

        self.motivo = StringVar()

        self.marco = Frame(self.analistas)
        self.marco.config(bg="#FFFFFF", width=500, height=700)
        self.lblTitulo = Label(self.marco, text="\t\tAdministrador Bi")
        self.lblTitulo.config(bg="#325795", width=40, anchor="w", height=2, font=("Rockwell", 15, 'bold'), foreground="#FFFFFF", relief=RAISED)

        self.lblBCorp = Label(self.marco, text="Buscar por corporativo")
        self.lblBCorp.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.txtBCorp = Entry(self.marco, textvariable=self.bCorp)
        self.txtBCorp.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=10)

        self.lblDatos = Label(self.marco, text="Datos de analista")
        self.lblDatos.config(bg="#FFFFFF", font=("Rockwell", 16, 'bold'))

        self.lblNombre = Label(self.marco, text="Nombre: ")
        self.lblNombre.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.txtNombre = Entry(self.marco, textvariable=self.nombre)
        self.txtNombre.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblCorp = Label(self.marco, text="Corporativo: ")
        self.lblCorp.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.txtCorp = Entry(self.marco, textvariable=self.corp)
        self.txtCorp.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblAnt = Label(self.marco, text="Antiguedad: ")
        self.lblAnt.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.txtAnt = Entry(self.marco, textvariable=self.ant)
        self.txtAnt.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblArea = Label(self.marco, text="Área: ")
        self.lblArea.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.lblRol = Label(self.marco, text="Rol: ")
        self.lblRol.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.cbxArea = ttk.Combobox(self.marco, background="#F4F4F4", state="readonly", width=25, values=["ALARMAS", "CCTV", "CLAVES"])
        self.cbxArea.config(font=("Comic Sans MS", 12), width=18)
        self.cbxRol = ttk.Combobox(self.marco, background="#F4F4F4", state="readonly", width=25, values=["ANALISTA", "COORDINADOR"])
        self.cbxRol.config(font=("Comic Sans MS", 12), width=18)

        self.btnBuscar = Button(self.marco, text="Buscar", command=self.analistasCorpBi)
        self.btnBuscar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnGuardar = Button(self.marco, text="Guardar", command=self.registrarAnalista)
        self.btnGuardar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnEliminar = Button(self.marco, text="Eliminar", command=self.eliminarAnalistas)
        self.btnEliminar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))

        self.lblMotivoPatrullaje = Label(self.marco, text="Motivos de patrullaje")
        self.lblMotivoPatrullaje.config(bg="#FFFFFF", font=("Rockwell", 16, 'bold'))
        self.lblMotivo = Label(self.marco, text="Motivo: ")
        self.lblMotivo.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.txtMotivo = Entry(self.marco, textvariable=self.motivo)
        self.txtMotivo.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=20)
        self.lblDescripcion = Label(self.marco, text="Descripción: ")
        self.lblDescripcion.config(bg="#FFFFFF", font=("Rockwell", 12))
        self.cbxDescripcion = ttk.Combobox(self.marco, state="readonly", width=30)
        self.cbxDescripcion.config(font=("Comic Sans MS", 12), width=20)

        self.btnAgregar = Button(self.marco, text="Agregar", command=self.agregarMotivo)
        self.btnAgregar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnEliminarMotivo = Button(self.marco, text="Eliminar", command=self.eliminarMotivo)
        self.btnEliminarMotivo.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.btnVolver = Button(self.marco, text="Cerrar Sesion", command=self.volverVentanaPatrullaje)
        self.btnVolver.config(bg="#3266B4", foreground="white", width=15, font=("Comic Sans MS", 12))

        self
        #separador-----> Apartado 1
        self.separador1h = ttk.Separator(self.marco, orient="horizontal")



    def ventanaUsuario(self):
        self.marco.place(x=0,y=0)
        self.lblTitulo.place(x=0, y=0)
        self.lblBCorp.place(x=320, y=55)
        self.txtBCorp.place(x=385, y=80)
        self.lblDatos.place(x=20,y=65)
        self.lblNombre.place(x=20, y=130)
        self.txtNombre.place(x=150,y=130)
        self.lblCorp.place(x=20, y=170)
        self.txtCorp.place(x=150,y=170)
        self.lblAnt.place(x=20, y=210)
        self.txtAnt.place(x=150, y=210)
        self.lblArea.place(x=20, y=250)
        self.cbxArea.place(x=150, y=250)
        self.lblRol.place(x=20, y=290)
        self.cbxRol.place(x=150, y=290)

        self.btnBuscar.place(x=385, y=120)
        self.btnGuardar.place(x=385, y=170)
        self.btnEliminar.place(x=385, y=220)

        self.lblMotivoPatrullaje.place(x=30,y=370)
        self.lblMotivo.place(x=20, y=435)
        self.txtMotivo.place(x=150,y=435)
        self.lblDescripcion.place(x=20, y=475)
        self.cbxDescripcion.place(x=150, y=475)

        self.btnAgregar.place(x=385,y=425)
        self.btnEliminarMotivo.place(x=385,y=475)
        self.btnVolver.place(x=385,y=525)

        #Separador -----> Apartado 1
        self.separador1h.place(relx=0, rely=0.5, relheight=0.002, relwidth=1)

        self.descripcionMotivo()
        self.analistas.mainloop()

    #Buscar al analista por corporativo
    def analistasCorpBi(self):
        self.analista = conexion.conexion().analistasCorpBi(self.bCorp.get())

        name = ""
        corp = ""
        ant = ""
        rol = ""
        area = ""

        if len(self.analista) == 0:
            messagebox.showerror("Analista no registrado", "El corp {} no se encuentra registrado como analista de monitoreo".format(self.bCorp.get()))
        else:
            for i in self.analista:
                name = i[1]
                corp = i[2]
                ant = i[3]
                rol = i[4]
                area = i[5]

                messagebox.showinfo("Datos analista", "Nombre: {}\nCorporativo: {}\nAntiguedad: {}\n Rol: {}\n Área: {}".format(name, corp, ant, rol, area))               

        self.txtBCorp.delete(0, "end")

    #Registrar datos del analista
    def registrarAnalista(self):
        self.analista = conexion.conexion().analistasCorpBi(self.corp.get())

        if len(self.analista) == 0:
            self.registrar = conexion.conexion().registrarAnalista(self.nombre.get(), self.corp.get(), self.ant.get(), self.cbxRol.get(), self.cbxArea.get())
            messagebox.showinfo("Registro correcto", "Se registro de manera exitoso al analista {}".format(self.nombre.get()))
        else:
            messagebox.showerror("Error en el registro", "El corp {} ya se encuentra registrado como analista de monitoreo".format(self.corp.get()))

    #Eliminar datos del analista 
    def eliminarAnalistas(self):
          self.eliminar = conexion.conexion().eliminarAnalista(self.bCorp.get())      
          self.txtBCorp.delete(0, "end")
          messagebox.showinfo("Usuario eliminado", "Se elimino correctamente el usuario")

    #Motivos del por cual se enviaron las patrullas CRUD
    def agregarMotivo(self):
       self.analista = conexion.conexion().buscarMotivo(self.motivo.get())
       if len(self.analista) == 0:
            self.addMotivo = conexion.conexion().agregarMotivo(self.motivo.get())
            self.txtMotivo.delete(0, "end")
       else:
           messagebox.showerror("Error en el registro", "Motivo ya registrado en el sistema")

    def descripcionMotivo(self):
        motivos = []

        self.motivos = conexion.conexion().descripcionMotivo()

        for i in self.motivos:
            motivos.append(i[1])
        self.cbxDescripcion["values"] = motivos

    def eliminarMotivo(self):
        self.deleteMotivo = conexion.conexion().eliminarMotivo(self.cbxDescripcion.get())
        self.index = self.cbxDescripcion.current()
        self.values = self.cbxDescripcion["values"]

        self.values = (*self.values[:self.index], *self.values[self.index+1:])
        self.cbxDescripcion["values"] = self.values
        messagebox.showinfo("Motivo eliminado", "Se elimino correctamente el motivo de patrullaje")


    def volverVentanaPatrullaje(self):
        self.analistas.withdraw()
        