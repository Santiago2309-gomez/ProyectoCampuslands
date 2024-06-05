import datos

def registrar_matriculas():
    matricula = {}
    matricula["ID"] = str(len(datos.data["Matriculas"]) +1) 
    #Se asigna un ID a la nueva matrícula. Este ID es un string y se calcula como la longitud actual de la lista de matrículas más 1. Esto asegura que cada nueva matrícula tenga un ID único e incremental
    camper_id = input("Ingrese a cedula del camper: ")
    camper = next((c for c in datos.data["Campers"] if c["ID"] == camper_id), None)
    #Se busca el camper en la lista de campers (datos.data["Campers"]). La función next() se usa junto con una expresión generadora para encontrar el primer camper cuyo ID coincida con el camper_id ingresado. Si no se encuentra ningún camper, camper será None.
    if camper:
        matricula["Camper"] = f'{camper["Nombres"]} {camper["Apellidos"]}'
    else:
        print("No se encontro camper con esa cedula")
        return
    
    trainer_id = input("Ingrese la cedula del trainer: ")
    trainer = next((t for t in datos.data["Trainers"] if t["ID"] == trainer_id), None)
    if trainer:
        matricula["Trainer"] = f'{trainer["Nombres"]} {trainer["Apellidos"]}' 
    else:
        print("Trainer no se encontro con esa cedula..")
        return
    
    ruta_id = input("Ingrese el ID de la ruta")
    ruta = next((r for r in datos.data["Rutas"] if r["ID"] == ruta_id), None)
    if ruta:
        matricula["Ruta"] = ruta["Nombre"]
    else:
        print("No se encontro ruta con ese ID")
        return
    
    matricula["Fecha_inicio"] = input("Ingrese la fecha de inicio (DIA-MES-AÑO)")
    matricula["Fecha_finalizacion"] = input("Ingrese la fecha de finalizacion (DIA-MES-AÑO)")

    area_id = input("Ingrese el ID de la ruta: ")
    area = next((r for r in datos.data["Areas"] if r["ID"] == ruta_id), None)
    if area:
        matricula["Areas"] = area["Nombre"]
    else:
        print("No se encontro area con ese ID")
        return

    datos.data["Matriculas"].append(matricula)
    datos.guardar_datos(datos.data)
    print("Matricula registrada exitosamente....")

def mostrar_matriculas():
    print("Las matriculas registradas son: ")
    for matricula in datos.data["Matriculas"]:
        print("-ID: ", matricula["ID"], "/ Camper: ", matricula["Camper"], "/ Trainer: ", matricula["Trainer"], "/ Ruta: ", matricula["Ruta"], "/ Area: ", matricula["Areas"], "/ Estado: ", matricula["Estado"], "/Riesgo: ", matricula["Riesgo"])
