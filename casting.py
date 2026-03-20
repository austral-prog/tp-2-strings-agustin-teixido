def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    #preguntas
    precio = int(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento: "))
    cantidad = int(input("Ingrese el cantidad de pago: "))

    # Calculos
    condes = precio - descuento
    total = condes * cantidad

    #Display
    print("Precio: ", precio)
    print("Descuento: ", descuento)
    print("Precio con descuento: ", condes)
    print("Total: ", total)

#casting()
