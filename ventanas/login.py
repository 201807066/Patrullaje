from tkinter import *
from tkinter import ttk
from  ventanas import administrarUsuarios, ventanaPatrullaje

class login:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Inicio de sesión administrador")
        self.ventana.resizable(False, False)
        self.ventana.geometry("400x200")
        self.ventana.eval('tk::PlaceWindow . center')

        #Variables
        self.user = StringVar()
        self.password = StringVar()

        #Creacion de marco y widgets
        self.marcoLogin = Frame(self.ventana)
        self.marcoLogin.config(bg="#FFFFFF", width=400, height=200)
        self.labelTitulo = Label(self.marcoLogin, text="\t       Inicio de sesión")
        self.labelTitulo.config(bg="#325795", width=31, anchor="w", height=2, font=("Rockwell", 15, 'bold'), foreground="#FFFFFF", relief=RAISED)
        self.labelUsuario = Label(self.marcoLogin, text="Usuario:")
        self.labelUsuario.config(bg="#FFFFFF", font=("Rockwell", 12, 'bold'))
        self.labelContraseña = Label(self.marcoLogin, text="Contraseña:")
        self.labelContraseña.config(bg="#FFFFFF", font=("Rockwell", 12, 'bold'))
        self.textUsuario = Entry(self.marcoLogin, textvariable=self.user)
        self.textUsuario.config(bg="#F4F4F4")
        self.textContraseña = Entry(self.marcoLogin, textvariable=self.password)
        self.textContraseña.config(bg="#F4F4F4")
        self.botonIngresar = Button(self.marcoLogin, text="Ingresar", command=self.admonAnalistas)
        self.botonIngresar.config(bg="#3266B4", foreground="white", width=7)
        self.botonCancelar = Button(self.marcoLogin, text="Cancelar", command=self.cancelar)
        self.botonCancelar.config(bg="#3266B4", foreground="white", width=7)

    def muestraVentana(self):
        self.marcoLogin.place(x=0,y=0)
        self.labelTitulo.place(x=0, y=0)
        self.labelUsuario.place(x=40, y=85)
        self.textUsuario.place(x=160, y=85)
        self.labelContraseña.place(x=40, y=115)
        self.textContraseña.place(x=160, y=115)
        self.botonIngresar.place(x=310, y=82)
        self.botonCancelar.place(x=310, y=112)
        self.ventana.mainloop()

    def admonAnalistas(self):
        self.ventana.withdraw()
        self.analistas = administrarUsuarios.admonUsuarios().ventanaUsuario()

    def cancelar(self):
        self.ventana.destroy()

