# Tarea: Trabajando con Diccionarios
def main():
    # 1) Diccionario inicial (incluye nombre, edad, ciudad y profesion)
    informacion_personal = {
        "nombre": "Ana Pérez",
        "edad": 28,
        "ciudad": "Quito",
        "profesion": "Estudiante"
    }

    # 2a) Acceder y modificar 'ciudad'
    informacion_personal["ciudad"] = "Guayaquil"

    # 2b) Agregar/actualizar 'profesion' (si ya existe, se actualiza)
    informacion_personal["profesion"] = "Enfermera"

    # 3) Verificar existencia de 'telefono'; si no existe, agregar
    if "telefono" not in informacion_personal:
        informacion_personal["telefono"] = "+593 99 123 4567"

    # 4) Eliminar la clave 'edad'
    informacion_personal.pop("edad", None)

    # 5) Imprimir diccionario final
    print("Diccionario final:", informacion_personal)

if __name__ == "__main__":
    main()

