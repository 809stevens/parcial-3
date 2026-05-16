print("="*90)
print("\n Binevenido al sistema de caliificacion")
print("="*90)

def validar_nombre():
    while True:
        nombre = input("ingresa tu nombre: ")
        if len(nombre) >= 3:
            return nombre
            
            
        else:
            print("¡ERROR!, Ingrese un nombre valido")
        
nombre = validar_nombre()

while True:
    rut = input("Ingresa tu rut sin dgito verificador: ")
    if not rut.isdigit():
        print("¡ERROR! ingresa un rut valido")
    if rut.isdigit() and len(rut) == 8:
        print("rut valido")
        break
    else:
        print(f"¡ERROR! rut invalido  {rut}")
    
while True:
    dv = input("ingresa tu digito verificador: ").upper()
    if len(dv) == 1 and (dv == "K" or dv.isdigit()):
        print("Digito verificador valido")
        break
    else:
        print("¡ERROR! Digito verificador no valido")

historial_notas = []

while True:
    print("\n" + "-"*90)
    
    
    while True:
        nombre_alumno = input("Ingresa el nombre del alumno: ").strip()
        if len(nombre_alumno) >= 3 and not nombre_alumno.isdigit():
            break
        print("¡Nombre inválido! Debe tener al menos 3 caracteres y no ser solo números.")

    
    print("\n A qué asignatura quieres ingresar las notas?")
    print("1. Matemática 1")
    print("2. Fundamentos de Programación")
    print("3. DevOps")
    print("4. Inteligencia Artificial")
    print("5. Ciencia de Datos")
    print("6. Salir")

    op = input("Ingresa tu opción: ").strip()

    if op == "6":
        print("Saliendo...")
        break

    materias = {
        "1": "Matemática 1",
        "2": "Fundamentos de Programación",
        "3": "DevOps",
        "4": "Inteligencia Artificial",
        "5": "Ciencia de Datos"
    }

    if op not in materias:
        print("Opción inválida")
        continue

    asignatura = materias[op]

    while True:
        try:
            cantidad = int(input("¿Cuántas notas quieres introducir?: "))
            if cantidad > 0:
                break
            print("Debe ingresar al menos 1 nota")
        except ValueError:
            print("Ingresa un número válido")

    cantidad_notas = []
    for i in range(1, cantidad + 1):
        while True:
            try:
                nota = float(input(f"Ingresa la nota {i}: "))
                if 1.0 <= nota <= 7.0:
                    cantidad_notas.append(nota)
                    break
                else:
                    print("¡Error! La nota debe estar entre 1.0 y 7.0")
            except ValueError:
                print("Ingresa una nota válida")

    promedio = sum(cantidad_notas) / len(cantidad_notas)

    historial_notas.append({
        "nombre_alumno": nombre_alumno,
        "materia": asignatura,
        "promedio": round(promedio, 2)
    })

    if input("¿Quieres calcular otro promedio? (si/no): ").lower() != "si":
        break
    


total = 0
for i, item in enumerate(historial_notas, start=1):
    print("-" *90)

    print(f"{"nombre":<30}:       {item['nombre_alumno']:>10}")
    print(f"{"Materia":<30}:      {item['materia']:>10}")
    print(f"{"Promedio":<30}:     {item['promedio']:>10}")
    total += item["promedio"]
    print("-" *90)
