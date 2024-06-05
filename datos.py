import json 
data= {
    "Campers": [],
    "Trainers": [],
    "Areas": [],
    "Rutas":[],
    "Matriculas": []
}

ruta_archivos = "db.json"

def guardar_datos(data):
    global ruta_archivos
    try:
        contenido = json.dumps(data, indent=4)
        with open (ruta_archivos, "w") as file:
            file.write(contenido)
            print("Datos Guardados")
    except Exception:
            print("Datos no guardados")
            
def cargar_datos():
     global data
     global ruta_archivos
     try:
        with open(ruta_archivos, "r") as file:
             data = json.load(file)
             print("Datos cargados")
     except Exception:
             print("Datos no cargados")
          