from tkinter import *
from tkinter import ttk
import datetime

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
        opc = IntVar()

        #Widgets
        self.marcoPrincipal = Frame(self.ventana)
        self.marcoPrincipal.config(bg="#dcffff", width=1350, height=750)
        self.lblTitulo = Label(self.marcoPrincipal, text="\t\t\t\t\tPatrullaje Bi")
        self.lblTitulo.config(bg="#325795", width=1350, anchor="w", height=1, font=("Rockwell", 20, 'bold'), foreground="#FFFFFF", relief=RAISED)

        #Apartado de los operadores 
        self.lblOperadorBi = Label(self.marcoPrincipal, text="Operador Bi")
        self.lblOperadorBi.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'))
        self.rbAlarmas  = Radiobutton(self.marcoPrincipal, text="Alarmas", variable= opc, value=1)
        self.rbAlarmas.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.rbCctv  = Radiobutton(self.marcoPrincipal, text="Cctv", variable= opc, value=2)
        self.rbCctv.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.rbClaves  = Radiobutton(self.marcoPrincipal, text="Claves", variable= opc, value=3)
        self.rbClaves.config(bg="#dcffff", font=("Comic Sans MS", 12))
        self.cbxOperador = ttk.Combobox(self.marcoPrincipal, width=25)

        #Apartado para el coordinador
        self.lblCoordinador = Label(self.marcoPrincipal, text="Coordinador a cargo")
        self.lblCoordinador.config(bg="#dcffff", font=("Comic Sans MS", 12, 'bold'))
        self.cbxCoordinador = ttk.Combobox(self.marcoPrincipal, width=25)

        #separador
        self.lSeparador = ttk.Separator(self.marcoPrincipal, orient="horizontal")
        self.l2Separador = ttk.Separator(self.marcoPrincipal, orient="vertical")


    def mostrarVentana(self):
        self.marcoPrincipal.place (x=0,y=0)
        self.lblTitulo.place(x=0, y=0)

        #Apartado de los operadores 
        self.lblOperadorBi.place(x=140, y=50)
        self.rbAlarmas.place(x=10, y=40)
        self.rbCctv.place(x=10, y=65)
        self.rbClaves.place(x=10, y=90)
        self.cbxOperador.place(x=110, y=75)

        #Apartado para el coordinador
        self.cbxCoordinador.place(x=290, y=75)
        self.lblCoordinador.place(x=295, y=50)

        #Separador
        self.lSeparador.place(relx=0, rely=0.175, relheight=0.002, relwidth=0.367)
        self.l2Separador.place(relx=0.365, rely=0.052, relheight=0.124, relwidth=0.002)


        self.ventana.mainloop()