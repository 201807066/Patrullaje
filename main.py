from ventanas import ventanaPatrullaje as ventana
from ventanas import administrarUsuarios as v
from ventanas import login as login


def main():
    login.login().muestraVentana()
    #ventana.VentanaPatrullaje().mostrarVentana()


if __name__ == "__main__":
    main()

