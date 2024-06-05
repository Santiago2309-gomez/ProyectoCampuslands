import datos
import re
def registrar_trainers():
    trainer = {}

    def id_no_repetir(id_input):
        for i in datos.data["Trainers"]:
            if i["ID"] == id_input:
                return False
        return True
    while True:
        id_input = input("Escriba la cedula del Trainer: ")
        if id_no_repetir(id_input):
            trainer["ID"] = id_input
            break
        else:
            print("La cedula ya existe....")
    trainer["Nombres"] = input("Ingrese el nombre(s) del trainer: ")
    trainer["Apellidos"] = input("Ingrese los apellidos del trainer: ")
    trainer["Direccion"] = input("Ingrese la direccion del trainer: ")
    trainer["Telefonos"] = input("Ingrese el telefono del trainer (celular o fijo): ")

    datos.data["Trainers"].append(trainer)
    datos.guardar_datos(datos.data)
    print("El trainer ha sido guardado exitosamente......")

def mostrar_trainers():
    print("Estos son los trainer que se encuentran trabajando en Campuslands")
    for trainer in datos.data["Trainers"]:
        print("ID", trainer["ID"], "/Nombres", trainer["Nombres"], "Apellidos", trainer["Apellidos"], "/Telefono", trainer["Telefonos"])

def modificar_trainers():
   
    trainer_id = input("Ingrese la cedula del trainer que desea modificar: ")
    for trainer in datos.data["Trainers"]:
        if trainer["ID"] == trainer_id:
            trainer["Nombres"] = input("Ingrese los nombre(s) del trainer: ")
            trainer["Apellidos"] = input ("Ingrese los apellidos del trainer: ")
            trainer["Direccion"] = input("Ingrese la direccion del trainer: ")
            while True:
                telefonos_input = input("Escriba el numero del trainer: ")
                if re.match(r'^[0-9]+$', telefonos_input):
                    trainer["Telefonos"] = telefonos_input
                    break
                else:
                    print("Telefonos no validos. Debe contener solo numero")
            datos.guardar_datos(datos.data)
            print("Los datos han sido actualizados exitosamente...")
        else:
            print("No se encontro un trainer con esta cedula")

def eliminar_trainers():
    trainer_id = input("Ingrese por favor la cedula del trainer que desea eliminar......")
    for trainer in datos.data["Trainers"]:
        if trainer["ID"] == trainer_id:
            datos.data["Trainers"].remove(trainer)
            datos.guardar_datos(datos.data)
            print("El trainer ha sido eliminado exitosamente.......")
            return
    else:
        input("Trainer no encontrado con esa cedula")