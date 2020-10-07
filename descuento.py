"""
basica = 1   = 700
estandar = 2  = 900
de lujo = 3  = 1500


clientes frecuentes 20% descuento

clientes normales:
    si compra >=10000 y <20000  =  10% desceunto
    si compra >= 20000  = 15% descuento

"""

def main():
    
    precio_sd = 0
    descuento = 0
    fin = 0
    
    silla = int(input('Que tipo de silla quieres?  (1:basica - 2:estandar - 3:de lujo)    '))
    cantidad = int(input('Cuantas sillas quieres?   '))
    cliente = input('Que tipo de cliente eres? (normal/frecuente)    ')
    
    print()
    precio_sd = precio_antes(silla,cantidad)
    descuento = descuento_otorgado(precio_sd, cliente)
    fin = total(precio_sd,descuento)
    if fin == 0:
        return (0)
    
def precio_antes(silla,cantidad):
    if silla == 1:
        sin_descuento = silla * 700 * cantidad
    elif silla == 2:
        sin_descuento = silla * 900 * cantidad
    elif silla == 3:
        sin_descuento = silla * 1500 * cantidad
        
    print('El precio sin descuento es $', float(sin_descuento))
    return(sin_descuento)

def descuento_otorgado(sin_descuento, cliente):
    descuento_p = 0
    
    if cliente == "frecuente":
        descuento_p = sin_descuento * .20
    
    elif cliente == "normal":
        if (sin_descuento >= 10000 and sin_descuento < 20000):
            descuento_p = sin_descuento * .10
        
        elif sin_descuento >= 20000:
            descuento_p = sin_descuento * .15
    else:
        print('Su cliente no es valido')
        exit()
        
    print('Usted tiene un descuento de $', descuento_p)
    return (descuento_p)

def total(precio_sd,descuento):
    total = precio_sd - descuento
    print('El precio final es de $',float(total))
    return (0)

main()
    