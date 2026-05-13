print("="*90)
print("\n bienevenido al sistema de ventas")
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



while True:
    direccion = input("Ingresa tu direccion: ")
    dividir = direccion.split()

    if len(dividir) >= 1 and dividir[-1].isdigit():
        print("direccion valido")
        break
    else:
        print("¡ERROR! ingresa un direccion valido")



edad = int(input("Ingresa tu edad: "))

socio = input("¿tienes tarjeta de socio? (si/no): ")



if edad >= 60 and socio.lower() == "si":
    descuento = 0.30
    porcentaje = 30
    print("eres mayor de edad y socio de la tienda, tienes un descuento del 30%")
    
elif edad < 18 and socio.lower() == "si":
    descuento = 0.10
    porcentaje = 10
    print("eres menor de edad y tienes tarjeta de socio, tienes un descuento del 10%")
elif edad < 18:
    descuento = 0.10
    porcentaje = 10
    print("eres menor de edad, tienes un descuento del 10%")

elif edad >= 60:
    descuento = 0.15
    porcentaje = 15
    print("eres mayor de edad, tienes un descuento del 15%")

elif socio.lower() == "si":
    descuento = 0.20
    porcentaje = 20
    print("eres socio de la tienda, tienes un descuento del 20%")

else:
    descuento = 0.0
    porcentaje = 0
    print("no cumples los requisitos para obtener un descuento")



suma = 0
sub_total_precio = [] 
total_producto = []


while suma <= 10:


    print(f"venta numero {suma}")
    print("")

    producto = input("ingresa el nombre del producto: ")
    total_producto.append(producto)

    while True:
        try:
            precio = int(input("Ingresa el precio del producto: "))
            if precio <= 0:
                print("error el numero debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("ingresa solo numeros")


    suma += 1
    sub_total_precio.append(precio)  
    ajuste = sum(sub_total_precio)  
    
    if suma == 10:

        respuesta = input("quieres ingresar mas ventas (si/no): ").lower()
        if respuesta != "si":
            print(f"la suma de las ventas: {ajuste} ")
            break


descuento2 = 0
porcentaje2 = 0

if suma >= 15:
    descuento2 = 0.15
    porcentaje2 = 15
    print("obetienes 15% adicional de descuento")
elif suma >= 10:
    descuento2 = 0.10
    porcentaje2 = 10
    print("obtienes 10% de descuento adicional")
elif suma <= 5:
    descuento2 = 0.05
    porcentaje2 = 5
    print("obtienes un 5% de descuento  adicional")


# calculo

iva = 0.19

porcentaje_iva = 19

precio_iva =  ajuste + (ajuste * iva)

suma_descuento = descuento + descuento2

suma_porcentaje = porcentaje + porcentaje2

total_descuento = precio_iva - (precio_iva * suma_descuento)

#resultado


print("=" *90)
print(f"nombre                :{nombre}")
print(f"rut                   :{rut}-{dv}")
print(f"edad                  :{edad}")
print(f"socio                 :{socio}")
print(f"direccion             :{direccion}")
print("=" *90)
print("")

print(f"{"producto": <30} {"precio":>10}")

print("-" *90)

for prod, prec in zip (total_producto, sub_total_precio):
    print(f"{prod: <30} ${prec:>10,.0f}")

print("-" *90)

print(f"{"precio original":<30} ${ajuste:>10,.0f}")
print(f"{"iva":<30} {porcentaje_iva:>10}%")
print(f"{"precio con iva":<30} ${precio_iva:>10,.0f}")
print(f"{"descuento aplicado":<30} {suma_porcentaje:>10}%")
print(f"{"precio con descuento":<30} ${total_descuento:>10,.0f}%")
print("=" *90)




        