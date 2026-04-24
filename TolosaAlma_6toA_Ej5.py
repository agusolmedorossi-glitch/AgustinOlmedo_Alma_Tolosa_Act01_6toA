#Ejercicio 5

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append([nombre, telefono, email])

    def listar_contactos(self):
        if self.contactos:
            for c in self.contactos:
                print(c[0], "-", c[1], "-", c[2])
        else:
            print("No hay contactos")

    def buscar_contacto(self):
        nombre = input("Nombre a buscar: ")
        for c in self.contactos:
            if c[0] == nombre:
                print(c[0], "-", c[1], "-", c[2])
                return
        print("No encontrado")

    def editar_contacto(self):
        nombre = input("Nombre a editar: ")
        for c in self.contactos:
            if c[0] == nombre:
                c[1] = input("Nuevo teléfono: ")
                c[2] = input("Nuevo email: ")
                print("Contacto actualizado")
                return
        print("No encontrado")


agenda = Agenda()
opcion = ""

while opcion != "5":
    print("\n1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")

    opcion = input("Opción: ")

    if opcion == "1":
        agenda.añadir_contacto()
    elif opcion == "2":
        agenda.listar_contactos()
    elif opcion == "3":
        agenda.buscar_contacto()
    elif opcion == "4":
        agenda.editar_contacto()
    elif opcion == "5":
        print("Agenda cerrada")
    else:
        print("Opción inválida")