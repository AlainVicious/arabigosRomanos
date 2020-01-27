import os
from numeros.Convert import numerosConvert


def imprimeMenu():
    os.system('cls')
    menuH1 = "MENU"
    menuOp1 = "1.-Convertir Romano a Arabigo"
    menuOp2 = "2.-Convertir Arabigo a Romano"
    menuOp3 = "3.-Salir"
    menuFoot = "Seleccione la opcion deseada..."
    print('\u250F',''.center(32,'\u2501'), '\u2513')
    print('\u2503',menuH1.center(32),'\u2503')
    print('\u2523',''.center(32,'\u2501'),'\u252B')
    print('\u2503',menuOp1.ljust(32),'\u2503')
    print('\u2503',menuOp2.ljust(32),'\u2503')
    print('\u2503',menuOp3.ljust(32),'\u2503')
    print('\u2503',''.center(32,'\u2501'),'\u2503')
    print('\u2503','Seleccione una opcion...'.ljust(32),'\u2503')
    print('\u2517',''.center(32,'\u2501'), '\u251B')

    

    return


def fun_repetir(SN):
    hayError = False
    repetir = False
    pasaOtra = True
        
    while not hayError:
        if SN == 'S':
            repetir = True
            break
        elif SN == 'N':
            repetir = False
            break
        else:
            SN = input('teclee S o N: ').upper()
    return repetir


def init():    
    opcion = 0
    salir = False
    convert = numerosConvert()
    while not salir:
        imprimeMenu()
        opcion = int(input('opcion: '))
        siVolver = ''
        siSalir = ''
        repetir = True
        if opcion == 1:
            while repetir:
                os.system('cls')
                romanoInput = input('ingresa el numero romano: ').upper()  
                arabigo = convert.romano_a_arabigo(romanoInput)
                print('Romano: {0} Arabigo: {1}'.format(romanoInput, arabigo))
                repetir = fun_repetir(input('Desea hacer otra convercion?(S/N) ').upper())
                

        elif opcion == 2:
            while repetir:
                os.system('cls')
                arabigoInput = int(input('ingresa el numero arabigo: '))
                romano = convert.arabigo_a_romano(arabigoInput)
                print('Arabigo: {0} Romano: {1}'.format(arabigoInput, romano))
                repetir = fun_repetir(input('Desea hacer otra convercion?(S/N) ').upper())

        elif opcion == 3:
            siSalir = input('Seguro que desea salir?(S/N) ')
            if siSalir.upper() == 'S' or siVolver == 'N':
                salir = True
                input('presione cualquier tecla para continuar...')
                exit()
        
        else:
            input('Opcion no valida!')
            
init()