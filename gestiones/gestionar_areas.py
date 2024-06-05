import datos

def registrar_areas():
    area = {}
    def id_no_repetir(id_input):
        for i in datos.data["Areas"]:
            if i["ID"] == id_input:
                return False
        return True
    while True:
        id_input = input("Escriba el ID del area: ")
        if id_no_repetir(id_input):
            area["ID"] = id_input
            break
        else:
            print("Ya existe un area con el mismo ID....")
    area["Nombre"] = input("Registre el nombre del area: ")
    datos.data["Areas"].append(area)
    datos.guardar_datos(datos.data)
    print("Areas registradas exitosamente...")

def mostrar_areas():
    print("Estas son las areas que se encuentran habilitadas")
    for area in datos.data["Areas"]:
        print("-ID: ", area["ID"], "/ Nombre: ", area["Nombre"])

def actualizar_areas():
    areas_id = input("Ingrese el id del area a modificar: ")
    for area in datos.data["Areas"]:
        if area["ID"] == areas_id:
            area["Nombre"] = input("Escriba el nombre del area: ")
            datos.guardar_datos(datos.data)
            print("El area se actualizo exitosamente...")
            return
        print("No se encuentra area con ese ID")

def eliminar_areas():
    areas_id = input("Ingrese el area a eliminar: ")
    for area in datos.data["Areas"]:
        if area["ID"] == areas_id:
            datos.data["Areas"].remove(area)
            print("El area ha sido eliminado exitosamente.....")
        else:
            print("No se encuentra area con ese ID")
            
