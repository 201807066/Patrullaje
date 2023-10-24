from tkinter import *
from tkinter import ttk, messagebox
from  ventanas import administrarUsuarios, ventanaPatrullaje
from conexion import conexion

class login:

    def __init__(self):
        #self.ventana = Toplevel(VentanaPatrullaje)
        self.ventana = Tk()
        self.ventana.protocol("WM_DELETE_WINDOW", self.cancelar)
        self.ventana.title("Inicio de sesión")
        self.ventana.resizable(False, False)
        self.ventana.eval('tk::PlaceWindow . center')
        self.ventana.geometry("385x300")

        #Variables
        self.user = StringVar()
        self.password = StringVar()

        #Creacion de marco y widgets
        self.marcoLogin = Frame(self.ventana)
        self.marcoLogin.config(bg="#FFFFFF", width=385, height=300)
        self.labelTitulo = Label(self.marcoLogin, text="\t       Inicio de sesión")
        self.labelTitulo.config(bg="#325795", width=31, anchor="w", height=2, font=("Rockwell", 15, 'bold'), foreground="#FFFFFF", relief=RAISED)
        self.labelUsuario = Label(self.marcoLogin, text="*Usuario:")
        self.labelUsuario.config(bg="#FFFFFF", font=("Rockwell", 12, 'bold'))
        self.labelContraseña = Label(self.marcoLogin, text="*Contraseña:")
        self.labelContraseña.config(bg="#FFFFFF", font=("Rockwell", 12, 'bold'))
        self.textUsuario = Entry(self.marcoLogin, textvariable=self.user)
        self.textUsuario.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=17)
        self.textContraseña = Entry(self.marcoLogin, show='*', textvariable=self.password)
        self.textContraseña.config(bg="#F4F4F4", font=("Comic Sans MS", 12), width=17)
     


        #Apartado coordinador
        self.lblCoordinador = Label(self.marcoLogin, text="Coordinador:")
        self.lblCoordinador.config(bg="#FFFFFF", font=("Rockwell", 12, 'bold'))
        self.cbxCoordinador = ttk.Combobox(self.marcoLogin, state="readonly", width=25)
        self.cbxCoordinador.config(font=("Comic Sans MS", 12), width=15)

        #Botones
        self.botonIngresar = Button(self.marcoLogin, text="Ingresar", command=self.inicioSesion)
        self.botonIngresar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        self.botonCancelar = Button(self.marcoLogin, text="Cancelar", command=self.cancelar)
        self.botonCancelar.config(bg="#3266B4", foreground="white", width=7, font=("Comic Sans MS", 12))
        
        #Separador 
        self.separador1h = ttk.Separator(self.marcoLogin, orient="horizontal")
        self.botonIngresar.bind("<Return>", self.inicioSesion)
        self.botonCancelar.bind("<Return>", self.cancelar)



    def muestraVentana(self):
        self.marcoLogin.place(x=0,y=0)
        self.labelTitulo.place(x=0, y=0)
        self.labelUsuario.place(x=30, y=80)
        self.textUsuario.place(x=160, y=80)
        self.labelContraseña.place(x=30, y=115)
        self.textContraseña.place(x=160, y=115)
        self.botonIngresar.place(x=102, y=230)
        self.botonCancelar.place(x=200,y=230)

        #Coordinador
        self.lblCoordinador.place(x=40, y=185)
        self.cbxCoordinador.place(x=160, y=185)

        #Separador

        self.separador1h.place(relx=0, rely=0.55, relheight=0.002, relwidth=1.0)
                               
        self.coordinadorBi()          
        self.ventana.mainloop()



    def inicioSesion(self, event=None):
        user = self.textUsuario.get()
        password = self.textContraseña.get()
        nombreAnalista = ""

        if(user == "" or password == ""):
              messagebox.showerror("Campos vacios", "Campos usuario o contraseña vacios")  
        elif(user=="a" and password=="a"):
            self.textUsuario.delete(0, END)
            self.textContraseña.delete(0, END)
            self.administrador = administrarUsuarios.admonUsuarios(self.ventana).ventanaUsuario()         
            self.minimizaVentana()
        else:

            if(self.cbxCoordinador.get() == ""):
                messagebox.showerror("Campos vacios", "Debe seleccionar el coordinador")  
            else:            
                self.analista = conexion.conexion().buscarAnalista(user, password)
                for i in self.analista:
                    nombreAnalista = i[1]
                    areaAnalista = i[5]
                    rolAnalista = i[4]

                if(len(self.analista)!=0):
                    self.textUsuario.delete('0', 'end')
                    self.textContraseña.delete('0', 'end')

                    self.patrullaje = ventanaPatrullaje.VentanaPatrullaje(self.ventana, nombreAnalista, self.cbxCoordinador.get(), areaAnalista, rolAnalista).mostrarVentana()
                    self.textUsuario.delete(0, END)
                    self.textContraseña.delete(0, END) 
                    self.minimizaVentana()                   

                    
                else:
                    messagebox.showerror("Datos erroneos", "Campos usuario o contraseña incorrectos") 
                    
           
    def coordinadorBi(self):
        coordinadores = []

        self.analistas = conexion.conexion().coordinadoresBi()
        for i in self.analistas:
            coordinadores.append(i[1])
            self.cbxCoordinador["values"] = coordinadores

    def minimizaVentana(self):
        self.ventana.iconify()
    
    def cancelar(self, event=None):
        self.ventana.destroy()

