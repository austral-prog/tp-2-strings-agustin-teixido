def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    # Preguntas
    gasto = float(input("Ingresar gasto:"))
    print(gasto)
    recibido = int(input("Dinero  recibido:"))
    print(recibido)
    print("")
    print("Vuelto")
    print("")

    # Resulatados
    vuelto = recibido - gasto
    pesos = int(vuelto)
    print("Pesos:")
    print(int(pesos))

    centavos = round((vuelto - pesos) * 100)
    print("Centavos:")
    print(centavos)

#change()