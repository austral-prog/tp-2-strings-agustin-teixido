def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """


    #nombre = str(input("Ingrese nombre: "))
    nombre1 = input()
    apellido = input()
    nombre = nombre1 + " " + apellido

    print(nombre.lower())
    print(nombre.title())
    print(nombre.upper())
    print(f"\t{nombre.lower()}")

