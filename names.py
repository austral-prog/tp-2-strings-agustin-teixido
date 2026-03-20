def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    nombre = input("Ingrese nombre y apellido: ")

    print(nombre.lower())
    print(nombre.title())
    print(nombre.upper())
    print("\f", nombre)

names()