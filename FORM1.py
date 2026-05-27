PIKACHU = 4500
OTAKU = 5000
PULPO = 5200
ANGUILA = 4800

cantidad_pikachu = 0
cantidad_otaku = 0
cantidad_pulpo = 0
cantidad_anguila = 0




print("-"*90)
print("\n bienvenido  al sistema de compra de sushi")

while  True:
    try:
        nombre = input("ingresa tu nombre: ").strip().lower()
        if len(nombre) < 3:
            print("el nombre debe tener al menos 3 caracteres")
            continue
        if not nombre.isdigit:
            print("el nombre no debe contener numeros")
            continue
        else:
            print(f"bienvenido {nombre}")
            break
    except Exception:
        print("Error!!!, por favor intenta de nuevo")

print("-"*70)

while True:
    rut = input("ingresa tu rut:").strip()
    if len(rut) < 7:
        print("el rut debe tener al menos 8 caracteres")
        continue
    if not rut.isdigit():
        print("el rut solo debe contener numeros")
        continue
    else:
        break

print("-"*70)

while True:
    dv = input("ingresa tu digito verificador:").strip()
    if len(dv) != 1:
        print("el digito verificador debe tener un caracter")
        continue
    elif not dv.isdigit() and dv.lower() != "k":
        print("el digito verificador debe ser un numero o la letra k")
        continue
    else:
        break

while True:
    direccion = input("Ingresa tu direccion (nombre y numero): ")
    dividir = direccion.split()

    if len(dividir) >= 1 and dividir[-1].isdigit():
        print("direccion valido")
        break
    else:
        print("¡ERROR! ingresa un direccion valido")


print("-"*90)

while True:

    print("\n opciones disponibles ")

    print(f"1.Pikachu Roll ${PIKACHU}")
    print(f"2. Otaku Roll ${OTAKU}")
    print(f"3. Pulpo Venenoso Roll ${PULPO}")
    print(f"4. Anguila Eléctrica Roll ${ANGUILA}")
    print("5. salir")

    while True:
        opc = input("ingresa tu opcion: ").strip()
        if opc not in ["1", "2", "3", "4", "5"]:
            print("debes elegir una opcion del 1-5")
        else:
            break

    print("-"*90)
    
    precio_roll_acumaulada = 0
    roll_comprado = []

    if opc == "1":
        print("elegiste el sushi Pikachu Roll ")
        cantidad_pikachu += 1
        precio_roll_acumaulada += PIKACHU
        roll_comprado .append(("Pikachu Roll", PIKACHU ))
    elif opc == "2":
        print("elegiste el sushi Otaku roll")
        cantidad_otaku +=1
        precio_roll_acumaulada += OTAKU
        roll_comprado.append(("Otaku roll", OTAKU))
    elif opc == "3":
        print("eleguste el sushi Pulpo Venenoso Roll")
        cantidad_pulpo += 1
        precio_roll_acumaulada  += PULPO
    elif opc == "4":
        cantidad_anguila +=1
        precio_roll_acumaulada += ANGUILA
        roll_comprado.append(("Anguila eléctrica", ANGUILA))

        print("elegiste el sushi Anguila Eléctrica Roll")
    elif opc == "5":
        print("saliendo...")
        break

    print("-"*90)
    seguir = input("¿quieres agregar mas roll a tu compra (si/no)?: ").strip().lower()
    if seguir !="si":
        print("procediendo el pago...")
        
        break

descuento = 0
porcentaje = 0

if precio_roll_acumaulada > 0:
     
    while True:
        respuesta = input("posees codigo de descuento (si/no): ").strip().lower()
        if respuesta == "si":
            print("-"*90)

            codigo = input("ingresa el codigo: ")
            if codigo == "soyotaku":
                print("codigo valido")
                print("obtienes 10% de descuento")
                descuento = 0.10
                porcentaje = 10
                break
            else:
                print("codigo no valido")
                print("no obtienes descuento")
                descuento = 0
                porcentaje = 0


                print("-"*90)
                otro = input("deseas ingresar el codigo de nuevo (si/no): ")
                if otro == "si":
                    codigo = input("ingresa el codigo: ")
                    if codigo == "soyotaku":
                        print("codigo valido")
                        print("obtienes 10% de descuento")
                        descuento = 0.10
                        porcentaje = 10
                        
                        break
                    else:
                        print("codigo no valido")
                        print("no obtienes descuento")
                        descuento = 0
                        porcentaje = 0
                        break
                else:
                    break
        else:
            print("no obtienes descuento")
            break

    cantidad_total = (cantidad_pikachu + cantidad_otaku + cantidad_pulpo + cantidad_anguila)

    descuento_aplicado = precio_roll_acumaulada - (precio_roll_acumaulada * descuento)

    print("-"*90)
    print("RESUMEN")
    print("-"*90)

    print(f"{"nombre":<30} {nombre:>10}")
    print(f"{"rut":<30} {rut}-{dv}")
    print(f"{"direccion":<30} {direccion:>10}")

    print(F"TOTAL PRODUCTO {cantidad_total}")

    for roll , precio in roll_comprado:
        print(f"{roll :<30} ${precio :>10}")

    print("-"*90)
   
    print(f"{"pikachu roll" :<30} {cantidad_pikachu:>10}")
    print(f"{"Otaku roll":<30} {cantidad_otaku:>10}")
    print(f"{"pulpo venenoso roll":<30} {cantidad_pulpo:>10}")
    print(f"{"Anguila roll":<30} {cantidad_anguila:>10}")

    print("*"*90)

    print(f"{"subtotal":<30} ${precio_roll_acumaulada:>10,.0f}")
    print(f"{"descuento":<30} {porcentaje:>10}% ")
    print(f"{"total":<30} ${descuento_aplicado:>10,.0f}")
    print("="*90)

else:
    print("no compraste ningun elemento, vuelva pronto")
    print("="*90)

    