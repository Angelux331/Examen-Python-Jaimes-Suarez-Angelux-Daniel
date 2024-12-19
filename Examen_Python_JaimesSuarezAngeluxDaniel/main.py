import os
import modulos.ui as ui
import modulos.mensajes as msg
import modulos.funciones as funci
import modulos.servicios as servi

if __name__ == "__main__":
    while (True):
        os.system('clear')
        print(ui.mainMenu)
        opcion = int(input('_'))
        match opcion:
            case 1:
                funci.cliente()
            case 2:
                funci.administrador()
            case 3:
                break