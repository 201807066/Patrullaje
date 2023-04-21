from ventanas import ventanaPatrullaje as ventana
from ventanas import administrarUsuarios as v
from ventanas import login as login


def main():
    inicio = ventana
    ventana.VentanaPatrullaje().mostrarVentana()

    #v.admonUsuarios().ventanaUsuario()


    #Llamar a login
    #inicio = login
    #login.login().muestraVentana()


if __name__ == "__main__":
    main()

