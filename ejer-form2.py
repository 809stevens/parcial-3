print("-"*90)
print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")
print("-"*90)

espacio_maxima = 60

espacio_ocupado = 0
#  verificar y obtener cantidad de espacio que desea ocupar
def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("ingresa la cantidad de espacio que desea ocupar: "))
            if cantidad <= 0:
                print("¡Error!, debe ingresar un valor mayor a cero")
            elif cantidad > (espacio_maxima - espacio_ocupado):
                print("¡Error!, No hay suficientes espacios disponibles para realizar la ocupación")
            else:
                print("espacio asignado correctamente")
                return cantidad
        except:
            print("¡ERROR!, Ingresas un valor invalido")


#verificar y obtener la cantidad de espacio se desea liberar
def cantidad_liberar():
    while True:
        try:
            liberar = int(input("ingresa la cantidad de espacio que desea liberar: "))
            if liberar <= 0:
                print("¡Error!, debe ingresar un valor mayor a cero")
            elif liberar > espacio_maxima:
                print("¡Error!, No puedes liberar más espacios de los que están ocupados actualmente")
            else:
                print("espacio liberado correctamente")
                return liberar
        except:
            print("¡ERROR!, Ingresas un valor invalido")


# menu principal
while True:
    print()
    print(f"-"*90)
    print("MENU PRINCIPAL")
    print("="*90)

    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Espacios actualmente ocupados")
    print("5. Salir") 

    while True:
        opc = input("ingresa tu opcion: ")
        if opc not in ["1", "2", "3", "4", "5"]:
            print("debes elegir una opcion del 1 al 5")
        else:
            break

    print("-"*90)
    print()
    if  opc == "1":
        print(f"espacio disponible {espacio_maxima - espacio_ocupado}")
    elif opc == "2":
        cantidad = obtener_cantidad()
        espacio_ocupado += cantidad
        print(f"se asigno {cantidad} de espacio")
    elif opc == "3":
        if espacio_ocupado == 0:
            print("no se puede liberar espacio que no estan ocupado")
        else:
            liberar = cantidad_liberar()
            espacio_ocupado -= liberar
            print(f"se libero {liberar} de espacio")
    elif opc == "4":
        print(f"espacio ocupado actualmente {espacio_ocupado}")
    elif opc == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

print()