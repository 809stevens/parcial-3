print("-"*90)
print("bienvenido  al sistema de registro de habitaciones del Hotel Corporativo Internacional.")
print("-"*90)

habitaciones = []


def verificar_nombre():
    while True:
        nombre = input("ingresa tu nombre: ")
        if len(nombre) >= 3 and not any (c.isdigit() for c in nombre):
            print(f"bienvenido {nombre} al Hotel Corporativo Internacional.")
            return verificar_nombre
            
        else:
            print("error!!!, tu nombre debe ser mayor a tres y no debe contener ningun numero")

nombre = verificar_nombre()
print("-"*90)

def verificar_rut ():
    while True:
        rut = input("Ingresa tu RUT (sin dígito verificador): ").strip()
        if len(rut) >= 7 and rut.isdigit():
            return verificar_rut
        print("ERROR: El RUT debe contener solo números y tener al menos 7 dígitos.")

rut = verificar_rut()
print("-"*90)
def verificar_dv ():
    while True:
        dv = input("Ingresa tu dígito verificador: ").strip().lower()
        if len(dv) == 1 and (dv.isdigit() or dv == "k"):
            return verificar_dv
        print("ERROR: El dígito verificador debe ser un número o la letra 'k'.")

dv = verificar_dv

print("-"*90)

while True:
    try:
        registrar = int(input("¿cuantas habitaciones deseas registrar?: "))
        if registrar <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            break
    except Exception:
        print("¡Error!, debes ingresar un numero entero")

print("-"*90)

for i in range(1, registrar + 1):
    print(f"{i} de {registrar}")

    while True:
        numero = input("ingresa el numero del habitacion (ej:ROOM001V): ").upper()
        if len(numero) < 6:
            print("el numero de habitacion debe contener al menos 6 caracter")
        elif " " in numero:
            print("¡Error, no se permite espacio blanco")
        elif not numero.isalnum():
            print("el numero debe contener al numeros y letras")
        else:
            print("habitacion registrado")
            habitaciones.append(numero)
            break

habitaciones_tarifa = []
print("-"*90)
suite = 0
estandar  = 0
for hab in habitaciones:
    while  True:
        try:
            tarifa = int(input(f"ingresa la tarifa del habitacon {hab}: "))
            if tarifa <= 0:
                print("Error tarifario! Ingresa un número entero positivo para la tarifa nocturna ")
            else:
                habitaciones_tarifa.append((hab, tarifa))
                break

        except ValueError:
            print("¡Error! ingresa un valor valido")

for hab, precio in habitaciones_tarifa:

    if precio > 9000:
        print(f" la habitacion {hab} es suite ejecutiva")
        suite +=1
    elif precio <= 9000:
        estandar +=1
        print(f"la habitacion {hab} es estandar")

print("-"*90)
print("RESUMEN")
print("-"*90)
print(f"nombre: {nombre}")
print(f"rut {rut}-{dv}")
print(f"¡El hotel cuenta con {suite} Suites Ejecutivas y {estandar} Habitaciones Estándar! ¡Check-in disponible!")    