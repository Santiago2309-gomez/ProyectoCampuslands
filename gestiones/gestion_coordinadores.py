import datos

def registrar_notas_ingresado():
    camper_id = input("Ingrese la cedula del camper: ")
    for camper in datos.data["Campers"]:
        if camper["ID"] == camper_id:
            try:
                nota_teorica = float(input("Ingrese la nota teórica del camper: "))
                nota_practica = float(input("Ingrese la nota práctica del camper: "))
                nota_quizes_trabajos = float(input("Ingrese la nota de quizes y trabajos del camper: "))
                if 0 <= nota_teorica <= 100 and 0 <= nota_practica <= 100 and 0 <= nota_quizes_trabajos <= 100:
                    promedio = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quizes_trabajos * 0.1)
                    camper["Promedio"] = promedio
                    if promedio >= 60:
                        camper["Estado"] = "Aprobado"
                    else:
                        camper["Estado"] = "Reprobado"
                    datos.guardar_datos(datos.data)
                    print(f"Notas registradas y estado del camper actualizado a {camper['Estado']}.")
                else:
                    print("Las notas deben estar entre 0 y 100.")
            except ValueError:
                print("Valor incorrecto, por favor ingrese un número.")
            return
    print("No se encontró un camper con ese ID.")

def registrar_notas_cursando():
    matricula_id = input("Ingrese el ID de la matricula: ")
    for matricula in datos.data["Matriculas"]:
        if matricula["ID"] == matricula_id:
            try:
                nota_teorica = float(input("Ingrese la nota teórica del camper: "))
                nota_practica = float(input("Ingrese la nota práctica del camper: "))
                nota_quizes_trabajos = float(input("Ingrese la nota de quizes y trabajos del camper: "))
                if 0 <= nota_teorica <= 100 and 0 <= nota_practica <= 100 and 0 <= nota_quizes_trabajos <= 100:
                    promedio = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quizes_trabajos * 0.1)
                    matricula["Promedio"] = promedio
                    if promedio >= 60:
                        matricula["Estado"] = "Aprobado"
                    else:
                        matricula["Estado"] = "Reprobado"

                    if promedio < 40:
                        matricula["Riesgo"] = "Alto"
                    elif 40 <= promedio < 70:
                        matricula["Riesgo"] = "Medio"
                    else:
                        matricula["Riesgo"] = "Bajo"
                    
                    datos.guardar_datos(datos.data)
                    print(f"Notas registradas y estado del camper actualizado a {matricula['Estado']}.")
                else:
                    print("Las notas deben estar entre 0 y 100.")
            except ValueError:
                print("Valor incorrecto, por favor ingrese un número.")
            return
    print("No se encontró un camper con ese ID.")
