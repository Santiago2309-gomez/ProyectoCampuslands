import datos
import gestiones.gestion_campers as gestion_campers
import gestiones.gestion_trainers as gestion_trainers 
import gestiones.gestionar_areas as gestionar_areas
import gestiones.gestionar_rutas as gestionar_rutas
import gestiones.gestion_matriculas as gestion_matriculas
import gestiones.gestion_coordinadores as gestion_coordinadores
#gestiones = el nombre de la carpeta, gestion campers nombre del archivo


#----------------------------- SE REALIZA EL MENU PRINCIPAL-------------------------------

def menu_principal():
    datos.cargar_datos()
    while True:
        print("------------------------------------------------")
        print("1.Coordinadores")
        print("2.Campers")
        print("3.trainers")
        print("4.Salir")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Valor incorrecto")
        if opc == 1:
            menu_coordinadores()
        elif opc == 2:
            menu_Campers()
        elif opc == 3:
            menu_trainers()
        elif opc == 4:
            print("Saliendo...")
            break
        else: 
            print("La opcion no es valida")

#---------------- SE REALIZO EL MENU DE COORDINADORES, CAMPERS Y TRAINERS-----------------

def menu_coordinadores():
    while True:
        print("------------------------------------------------")
        print("\nGestionar Coordinadores")
        print("1. Gestionar Areas")
        print("2. Gestionar Rutas")
        print("3. Gestionar Matriculas")
        print("4. Registrar Nota de Camper: ")
        print("5. Volver al menu principal")
        try:
            opc = int(input("Ingrese su opcion: "))
        except ValueError:
            print("Valor incorrecto ingrese una de las opciones validas")
            continue
        if opc == 1:
            menu_areas()
        elif opc == 2:
            menu_rutas()
        elif opc ==3:
            menu_matriculas()
        elif opc == 4:
            menu_registrar_notas()
        elif opc == 5:
            break
        else:
            print("Opcion invalida")



def menu_Campers():
    while True:
        print("------------------------------------------------")
        print("\nGestionar Camper")
        print("1. Registrar Camper")
        print("2. Mostrar Camper")
        print("3. Actualizar Camper")
        print("4. Eliminar Camper")
        print("5. Volver al Menu Principal")
        try:
            opc = int(input("Ingrese la opcion que desee: "))
        except ValueError:
            print("Valor incorrecto ingrese una opcion valida")
            continue
        if opc == 1:
            gestion_campers.registrar_campers()
        elif opc == 2:
            gestion_campers.mostrar_campers()
        elif opc == 3:
            gestion_campers.actualizar_campers()
        elif opc == 4:
            gestion_campers.eliminar_campers()
        elif opc == 5:
            break
        else:
            print("Opción invalida")

def menu_trainers():
    while True:
        print("\nGestionar Trainers")
        print("1. Registrar Trainers")
        print("2. Mostrar Trainers")
        print("3. Actualizar Trainers")
        print("4. Eliminar Trainers")
        print("5. Volver al menu principal")
        try: 
            opc = int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("la opcion que ingreso no es correcta")
            continue
        if opc == 1:
            gestion_trainers.registrar_trainers()
        elif opc == 2:
            gestion_trainers.mostrar_trainers()
        elif opc == 3:
            gestion_trainers.modificar_trainers()
        elif opc == 4:
            gestion_trainers.eliminar_trainers()
        elif opc == 5:
            break
        else:
            print("Opcion no valida")

#---------------------SE REALIZO EL SUBMENU DE COORDINADORES------------------------------

def menu_areas():
    while True:
        print("-----------------------------------------------")
        print("\nGestion Areas")
        print("1. Registar Areas")
        print("2. Mostrar Areas")
        print("3. actualizar Areas")
        print("4. Eliminar areas")
        print("5. Volver al menu principal")
        try:
            opc = int(input("Ingrese la opcion que desee: "))
        except ValueError:
            print("La opcion que usted ingreso es incorrecta")
            continue
        if opc == 1:
            gestionar_areas.registrar_areas()

        elif opc == 2:
            gestionar_areas.mostrar_areas()

        elif opc == 3:
            gestionar_areas.actualizar_areas()
        elif opc == 4:
            gestionar_areas.eliminar_areas()
        elif opc == 5:
            break
        else:
            print("Opcion no valida")

def menu_rutas():
    while True:
        print("------------------------------------------------")
        print("\nGestionar Rutas")
        print("1. Registrar Ruta")
        print("2. Mostrar Rutas")
        print("3. Modificar Rutas")
        print("4. Elimiar rutas")
        print("5. Volver al menu principal")
        try:
            opc = int(input("Ingrese la opcion que desee: "))
        except ValueError:
            print("La opcion es incorrecta")
        if opc == 1:
            gestionar_rutas.registar_rutas()
        elif opc == 2:
            gestionar_rutas.mostrar_rutas()
        elif opc == 3:
            gestionar_rutas.modificar_rutas()
        elif opc == 4:
            gestionar_rutas.eliminar_rutas()
        elif opc == 5:
            break
        else:
            print("La opcion que escogio es incorrecta")

def menu_matriculas():
    while True:
        print("------------------------------------------------")
        print("\nGestion Matriculas")
        print("1. Registrar Matriculas")
        print("2. Mostrar las Matriculas")
        print("3. Volver al menu principal")
        try:
            opc = int(input("Ingrese la opcion que desee: "))
        except ValueError:
            print("La opcion que ingreso no es valida")
        if opc == 1:
            gestion_matriculas.registrar_matriculas()
        elif opc == 2:
            gestion_matriculas.mostrar_matriculas()
        elif opc == 3:
            break
        else:
            print("La opcion que ingreso es invalida")

def menu_registrar_notas():
    while True:
        print("/nRegistrar notas del camper")
        print("1. Registrar nota del camper ingresado")
        print("2. Ingresar nota del camper cursando")
        print("3. Volver al menu principal")
        try:
            opc = int(input("Ingrese la opcion que desee: "))
        except ValueError:
            print("El valor que ingreso es incorrecto")
            continue
        if opc == 1:
            gestion_coordinadores.registrar_notas_ingresado()
        elif opc == 2:
            gestion_coordinadores.registrar_notas_cursando()
        elif opc == 3:
            break
        else:
            print("Opcion incorrecta")

        
    

