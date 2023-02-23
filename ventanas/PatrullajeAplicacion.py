import sys
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow
from VentanaPatrullaje import MainWindow

class PatrullajeAplicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = MainWindow()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = PatrullajeAplicacion()
    ventana.show()
    sys.exit(app.exec_())