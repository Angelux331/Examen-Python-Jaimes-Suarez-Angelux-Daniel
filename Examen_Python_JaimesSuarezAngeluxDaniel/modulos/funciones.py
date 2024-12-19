import os
import json
import modulos.ui as ui
import modulos.mensajes as msg
import modulos.servicios as servi

def guardarArchivo(Diccionario, archivo):
    with open(f'/home/camper/Documentos/J2/modulos/{archivo}.json', 'w') as f: 
        json.dump(Diccionario, f, indent=4) 
    return True

def abrirArchivo(archivo): 
    with open(f'/home/camper/Documentos/J2/modulos/{archivo}.json',"r") as entrada:
        nuevoDiccionario = json.load(entrada)
        return nuevoDiccionario
    
baseDatos = abrirArchivo('base_datos')

def administrador():
    os.system('clear')
    print(ui.menuAdmins)
    opcion = int(input('_'))
    match opcion:
        case 1:
            os.system('clear')
            nombre = input('Nombre del cliente: ').capitalize()
            apellido = input('Apellido del cliente: ').capitalize()
            documento = int(input('Documento del cliente: '))
            direccion = input('Direccion del cliente: ')
            telefono = int(input('Telefono del cliente: '))

            informacion = {
                documento:{
                    'Nombre': nombre,
                    'Apellido': apellido,
                    'Documento': documento,
                    'Direccion': direccion,
                    'Telefono': telefono,
                    'Categoria': 'Nuevo cliente',
                    'Suscripciones activas': [0],
                    'Promociones': [0],
                    'Estado de pago': 'Estable',
                    'Historial de suscripciones': [0],
                    'quejas' : [0]
                    }
            }
            baseDatos["cliente"].append(informacion)
            guardarArchivo(baseDatos,"base_datos")
            print(f"Su cliente fue guardado exitosamente {documento}")
            x = input('Presione una tecla para continuar....')
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            x = input('Presione una tecla para continuar....')
        case _:
                os.system('clear')
                print('Opcion no valida...')
                x = input('Presione una tecla para continuar....')
                return

def cliente():
        os.system('clear')
        print(ui.menuCliente)
        opcion = int(input('_'))
        match opcion:
            case 1:
                os.system('clear')
                cliente = input('Ingresa tu numero de documento: ')
                for clientes in baseDatos["cliente"]:
                    if cliente == clientes:
                        print(baseDatos["cliente"][cliente]["Suscripciones activas"])
                        x = input('Pesione una tecla para continuar....')
                    else:
                        os.system('clear')
                        x = input('cliente no encontrado...')
            case 2:
                os.system('clear')
                print(servi.servicios)
                opcion = input('_')
                match opcion:
                    case 1:
                        os.system('clear')
                        print(servi.serviciotef)
                        opcion = input('_')
                        match opcion:
                            case 1:
                                print(servi.planesPos)
                    case 2:
                        os.system('clear')
                        print(servi.servicioHog)
                        opcion = input('_')
                        match opcion:
                            case 1:
                                os.system('clear')
                                opcion = input('Desea comprar el servicio hogar 100mb? S/N').capitalize()
                                match opcion:
                                    case 'S':
                                        os.system('clear')
                                        cliente = input('Ingrese su numero de documento')
                                        for clientes in baseDatos["cliente"]:
                                            if cliente == clientes['documento']:
                                                baseDatos["cliente"][cliente]["Suscripciones activas"].append('Servicio Hogar 100mb')
                                                guardarArchivo(baseDatos,"base_datos")
                                                x = input('el paquete se ha comprado con exito....')
                                            else:
                                                x= input('No se encontro cliente en la base de datos,cancelando compra y regresando al menu principal')
                                    case 'N':
                                        os.system('clear')
                                        X = input('Compra cancelada, regresando al menu principal....')

            case 3:
                pass
            case 4:
                os.system('clear')
                queja = input('Que queja desea dejar: ')
                cliente = input('Nro de documento: ')
                for clientes1 in baseDatos["cliente"]:
                    if cliente == clientes1['Documento']:
                        baseDatos["cliente"][cliente]['quejas'].append(queja)
                        guardarArchivo(baseDatos,"base_datos")
                        x=input('Queja registrada')
                    else:
                        baseDatos["quejasidk"].append(queja)
                        guardarArchivo(baseDatos,"base_datos")
                        x=input('Queja registrada')
            case 5:
                x = input('Presione una tecla para continuar....')
            case _:
                os.system('clear')
                print('Opcion no valida...')
                x = input('Presione una tecla para continuar....')
                return