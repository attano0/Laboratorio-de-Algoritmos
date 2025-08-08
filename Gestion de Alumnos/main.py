estudiantes = []

menor_nota = 11
mayor_nota = -1

buenos_alumnos = False

while True:
    print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedio general")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar estudiantes con nota mayor al promedio")
    print("6. Mostrar mejor y peor nota")
    print("7. Eliminar estudiante por nombre")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombre = input("Nombre del estudiante: ")
            try:
                edad = int(input("Edad: "))
                nota = float(input("Nota (0-10): "))
            except ValueError:
                print("Edad o nota inválidas. Intenta de nuevo.")
                continue

            if edad <= 0 or nota < 0 or nota > 10:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_estudiante = {
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                }
                estudiantes.append(nuevo_estudiante)
                print(f"Estudiante {nombre} registrado con éxito.")

        case "2":
            if not estudiantes:
                print("No hay estudiantes registrados aún.")
            else:
                print("\nEstudiantes registrados:")
                print("-------------------------")
                for i, estudiante in enumerate(estudiantes, 1):
                    print(f"{i}. Nombre: {estudiante['nombre']}")
                    print(f"   Edad: {estudiante['edad']}")
                    print(f"   Nota: {estudiante['nota']}")
                    print("-------------------------")

        case "3":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                print(f"El promedio general de notas es: {promedio:.2f}")
                
        case "4":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                buscar_est = input("Escribe el nombre del estudiante que quieras buscar: ")
                
                for estudiante in estudiantes:
                    if estudiante['nombre'] == buscar_est:
                        print("-------------------------")
                        print(f" Nombre: {estudiante['nombre']}")
                        print(f"   Edad: {estudiante['edad']}")
                        print(f"   Nota: {estudiante['nota']}")
                        print("-------------------------")
                        
        case "5":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                print(f"El promedio general de notas es: {promedio:.2f}")
                
                for estudiante in estudiantes:
                    if estudiante['nota'] > promedio:
                        print(estudiante['nombre'], " tiene una nota mayor al promedio, con una nota de ", estudiante['nota'] )
                        buenos_alumnos = True
                    
                if buenos_alumnos == False:
                    print("Ningun alumno supera el promedio...")
                    
        case "6":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                for estudiante in estudiantes:
                    if estudiante['nota'] < menor_nota:
                        menor_nota = estudiante['nota']
                        est_burro = estudiante['nombre']
                
                for estudiante in estudiantes:
                    if estudiante['nota'] > mayor_nota:
                        mayor_nota = estudiante['nota']
                        est_genio = estudiante['nombre']
                    
                print("La peor nota la tiene", est_burro, "con un" , menor_nota, "y la mejor nota la tiene", est_genio, "con un", mayor_nota)
                
        case "7":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                borrar_est = input("Escribe el nombre del estudiante que quieras eliminar: ")
                
                for estudiante in estudiantes:
                    if estudiante['nombre'] == borrar_est:
                        estudiantes.remove(estudiante)
                
        case "8":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")