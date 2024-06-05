import datos
import re
def registrar_campers():
    camper = {}

    def id_no_repetir(id_input):
        for i in datos.data["Campers"]:
            if i["ID"] == id_input:
                return False
        return True
    while True:
        id_input = input("Escriba la cedula del camper: ")
        if id_no_repetir(id_input):
            camper["ID"] = id_input
            break
        else:
            print("La cedula ya existe....")
    
    
    camper["Nombres"] = input("Escriba los nombre(s) del camper: ")
    camper["Apellidos"] = input("Escriba los apellidos del camper: ")
    camper["Direccion"] = input("Escriba la direccion del camper: ")
    camper["Acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
    while True:
        telefonos_input = input("Escriba el telefono del camper: ")
        if re.match(r'^[0-9]+$', telefonos_input):
            camper["Telefonos"] = telefonos_input
            break
        else:
            print("Teléfonos no válidos. Deben contener solo números y  no pueden incluir espacios, guiones o paréntesis.")
    camper["Estado"] = input("Ingrese el estado del camper: ")
    camper["Riesgo"] = input("Ingrese el riesgo del camper: ")
    #Vamos a cargar los datos ingresado a la base de datos
    datos.data["Campers"].append(camper)
    datos.guardar_datos(datos.data)
    print("El camper ha sido registrado correctamente...")

def mostrar_campers():
    print("Estos son los campers registrado.....")
    for camper in datos.data["Campers"]: #camper el nombre del diccionario donde esta guardado y campers el nombre del diccionario principa de data
        print("ID", camper["ID"], "/ Nombre", camper["Nombres"], "/ Apellidos ", camper["Apellidos"],"/ Direccion", ["Direcccion"], "/ Telefono", camper["Telefono"], "/ Estado", camper["Estado"], "/ Riesgo", camper["Riesgo"])
        
def actualizar_campers():
    camper_id = input("Ingrese la cedula del camper que desea modificar: ")
    for camper in datos.data["Campers"]:
        if camper["ID"] == camper_id:
            camper["Nombres"] = input("Ingrese los nombre(s) del camper: ")
            camper["Apeliidos"] = input("ingrese los apellidos del camper: ")
            camper["Direccion"] = input("Ingrese la direccion del camper: ")
            camper["Acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
            while True:
                telefonos_input = input("Escriba el numero del camper: ")
                if re.match(r'^[0-9]+$', telefonos_input):
                    camper["Telefonos"] = telefonos_input
                    break
                else:
                    print("Telefonos no validos. Debe contener solo numero")
            camper["Estado"] = (input("Ingrese el estado del camper: "))
            camper["Riesgo"] = input("Ingrese el riego del camper: ")
            datos.guardar_datos(datos.data)
            print("Los datos han sido actualizados correctamente....")
            return
    print("No se encontro un camper con esa cedula...")

def eliminar_campers():
    camper_id = input("Ingrese la cedula del camper que desea eliminar: ")
    for camper in datos.data["Campers"]:
        if camper["ID"] == camper_id:
            datos.data["Campers"].remove(camper)
            datos.guardar_datos(datos.data)
            print("El camper ha sido eliminado exitosamente...")
            return
    print("No se encontro camper con esa cedula..")





