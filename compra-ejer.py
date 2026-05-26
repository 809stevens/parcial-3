

ESPADA = 5000
ARCO = 7000
BASTON = 9000

print("="*70)
print("\n bienvenido a la tienda de armas")
print("="*70)

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
            print(f"bienvenido {nombre} a la tienda de armas")
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

print("-"*70)

armas_comprada = []
armas_acumulado = 0

while True:
    print("\n opcion disponibles para comprar")
    print(f"1 - espada con un precio de ${ESPADA} clp")
    print(f"2 - arco con un precio de ${ARCO} clp")
    print(f"3 - baton magico con un precio de ${BASTON} clp")
    print("4 - salir")

   
    opc = (input("ingrese tu opcion: "))
        
    if opc not in  ["1", "2", "3", "4"]:
        print("debes elegir una opcion en el rango de 1-4")
        continue
        

    
    
    if opc == "1":
        print("compraste la espada") 
        armas_comprada.append(("espada", ESPADA))
        armas_acumulado += ESPADA
    elif opc == "2":
        print("compraste el arco") 
        armas_comprada.append(("arco", ARCO))
        armas_acumulado += ARCO 
    elif opc == "3":
        print("compraste el baston magico")
        armas_comprada.append(("baston magico", BASTON))
        armas_acumulado += BASTON
    elif opc == "4":
        print("saliendo...")
        break
    
    

    print("_"*70)
    seguir = input("desea seguir comparando (si/no): ").strip().lower()
    if seguir != "si":
        print("procediendo el pago...")
        break 


descuento = 0
porcentaje = 0

print("_"*70)

if armas_acumulado > 0:
    while True:
        try:
            nivel = int(input("\n que nivel eres (1 al 100) "))
            break
        except Exception:
            print("Error!! , intente de nuevo")
            

    if nivel >= 90:
        print("obtienes 10% de descuento")
        descuento = 0.30
        porcentaje = 30
    elif nivel >= 30:
        print("obtienes 20% de descuento")
        descuento = 0.20
        porcentaje = 20
    elif nivel <= 30:
        print("obtienes 30% de descuento")
        descuento = 0.10
        porcentaje = 10
    else:
        print("tu nivel es muy bajo para obtener un descuento")

    print("_"*70)

    iva = 0.19

    precio_iva = armas_acumulado + (armas_acumulado * iva) 

    total = precio_iva - (precio_iva * descuento)



    print(f"nombre {nombre}")
    print(f"rut {rut}-{dv}")
    print(f"direccion {direccion}")

    for arm, pre in  armas_comprada:
        print(f"{arm: <30} ${pre:>10,.0f}")

    print("-" *90)
    
    print("\n RESUMEN DE TU COMPRA")

    print("-" * 42)
    if porcentaje > 0:
        print(f"{'Total sin IVA:': <30} ${armas_acumulado:>10,.0f}")
        print(f"{"descuento aplicado:" :<30}  {descuento:>10}")
        print(f"{'Total con IVA (19%):': <30} ${total:>10,.0f}")
        print("=" *90)
else:
    print("no compraste ningun elemento, vuelva pronto!!")
    print("=" *90)
    
    
    




        









