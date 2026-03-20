def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    nomb = input("Ingrese nombre: ").strip().lower()
    nombre, apellido = nomb.split(" ")
    email = input("Ingrese email: ").lower().strip()
    notaUno = int(input("Ingrasar nota 1:"))
    notaDos = int(input("Ingrese nota 2:"))
    notaTres = int(input("Ingrese nota 3:"))
    usuario = (apellido+"."+nombre).lower()
    nomApe = apellido+ " " + nombre
    archivo = (apellido+"_"+nombre).lower()
    caracteres = len(nomApe)
    iniNom = nombre[0]
    iniApe = apellido[0]
    nom, dominio = email.split("@")
    promedio = int((notaUno + notaDos + notaTres) / 3)



    print("=" * 40)
    print("FICHA DE ALUMNOS")
    print("=" * 40)
    print("Nombre: ", nomb)
    print("Email: ", email)
    print("Caracteres en nombre: ", caracteres)
    print("Iniciales: ", iniNom, iniApe)
    print("Usuarios: ", usuario)
    print("Email valido: ", "@" in email)
    print("Dominio: ", dominio)
    print("Nombre para el archivo: ", archivo)
    print("Codigo secreto: ", nomApe[::-1])
    print("Nota 1: ", notaUno)
    print("Nota 2: ", notaDos)
    print("Nota 3: ", notaTres)
    print("Suma: ", notaUno+notaDos+notaTres)
    print("Promedio: ", float(promedio))
    print("Premedio entero: ", int(promedio))
    print("*"*24)


ficha()

