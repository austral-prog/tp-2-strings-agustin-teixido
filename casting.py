def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    # Cálculos (según lo que esperan los tests)
    precio_con_descuento = precio - descuento
    total = precio_con_descuento * cantidad

    # Salida
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {total}")


