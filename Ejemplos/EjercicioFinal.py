class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({'tarea': tarea, 'completada': False})

    def marcar_completada(self, posicion):
        if 1 <= posicion <= len(self.tareas):
            self.tareas[posicion - 1]['completada'] = True
        else:
            raise IndexError("La posición no existe en la lista")

    def mostrar_tareas(self):
        print("Tareas pendientes:")
        for i, tarea in enumerate(self.tareas, 1):
            estado = 'Completada' if tarea['completada'] else 'Pendiente'
            print(f"{i}. {tarea['tarea']} - {estado}")

    def eliminar_tarea(self, posicion):
        if 1 <= posicion <= len(self.tareas):
            del self.tareas[posicion - 1]
        else:
            raise IndexError("La posición no existe en la lista")


def main():
    lista_tareas = ListaTareas()

    while True:
        print("\n--- MENU ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            nueva_tarea = input("Ingrese la nueva tarea: ")
            lista_tareas.agregar_tarea(nueva_tarea)
        elif opcion == '2':
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                lista_tareas.marcar_completada(posicion)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif opcion == '3':
            lista_tareas.mostrar_tareas()
        elif opcion == '4':
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                lista_tareas.eliminar_tarea(posicion)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()
