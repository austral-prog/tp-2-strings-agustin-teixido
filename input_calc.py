def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass

    # Preguntas
    base = input("Base: ")
    altura = input("Altura: ")

    # Calculos
    base = int(base)
    altura = int(altura)

    area = (base * altura)
    perimetro = (base*2) + (altura*2)

    # Output
    print("Base: ", base)
    print("Altura: ", altura)
    print("Area: ", area)
    print("Perimetro: ", perimetro)

#rectangle()

