import datos

def registar_rutas():
    ruta = {}
    def id_no_repetir(id_input):
        for i in datos.data["Rutas"]:
            if i["ID"] == id_input:
                return False
        return True
    while True:
        id_input = input("Escriba el ID del area: ")
        if id_no_repetir(id_input):
            ruta["ID"] = id_input
            break
        else:
            print("Ya existe un area con el mismo ID....")
    ruta["Nombre"] = input("Ingrese el nombre de la ruta: ")
    datos.data["Rutas"].append(ruta)
    datos.guardar_datos(datos.data)
    print("Area guardado exitosamente...")

def mostrar_rutas():
    print("Las rutas guardadas son:")
    for ruta in datos.data["Rutas"]:
        print("ID", ruta["ID"], "/ Nombre:", ruta["Nombre"])

def modificar_rutas():
    rutas_id = input("Ingrese el ID de la ruta que desea modificar: ")
    for ruta in datos.data["Rutas"]:
        if ruta["ID"] == rutas_id:
            ruta["Nombre"] = input("Ingrese el nombre de la ruta: ")
            datos.guardar_datos(datos.data)
            print("La ruta se modifico exitosamente")
            return
    print("No se encontro area con ese ID")

def eliminar_rutas():
    ruta_id = input("Ingrese el ID del area que desea eliminar: ")
    for ruta in datos.data["Rutas"]:
        if ruta["ID"] == ruta_id:
            datos.data["Rutas"].remove(ruta)
            print("La ruta ha sido eliminada exitosamente... ")
        else:
            print("No existe ruta con ese ID")

