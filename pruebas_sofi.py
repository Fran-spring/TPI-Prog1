
def pedir_nombres(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("Error, el campo no puede estar vacío.")
        elif dato.isdigit():
            print("Error, no puede ingresar números.")
        else:
            return dato

def pedir_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Error, debe ser un numero positivo.")
            else:
                return numero
            
        except ValueError:
            print("Ingrese un número válido.")

def agregar_paises(paises):
    nombre = pedir_nombres("Ingrese el País: ")
    poblacion = pedir_numero("Ingrese la cantidad de la población: ")
    superficie = pedir_numero("Ingrese la cantidad de la superficie: ")
    continente = pedir_nombres("Ingrese el Continente: ")

    pais = {
        "nombre": nombre, 
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)
    print("Pais agregado correctamente.")
    print(paises)

def buscar_pais(paises):
    pais_buscado = pedir_nombres("Ingrese el País a buscar: ")

    encontrado = False

    for pais in paises: 
        if pais_buscado.lower() in pais["nombre"].lower():
            print(pais)
            encontrado = True
    
    if not encontrado:
        print("No se encontró el País buscado.")

def actualizar_pais(paises):
    pais_buscado = pedir_nombres("Ingrese el País a actualizar: ")

    encontrado = False

    for pais in paises:
        if pais_buscado.lower() == pais["nombre"].lower():
            poblacion = pedir_numero("Ingrese la población actualizada: ")
            superficie = pedir_numero("Ingrese la superficie actualizada: ")

            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            print("País actualizado correctamente.")
            print(pais)

            encontrado = True

    if not encontrado:
        print("No se encontró el País buscado.")

def filtrar_continente(paises):
    continente_buscado = pedir_nombres("Ingrese el nombre del Continente: ")

    encontrado = False

    for pais in paises:
        if continente_buscado.lower() == pais["continente"].lower():
            print(pais)
            encontrado = True

    if not encontrado:
        print("No se encontró el Continente.")

def filtrar_poblacion(paises):
    minimo = pedir_numero("Ingrese la población mínima: ")
    maximo = pedir_numero("Ingrese la población máxima: ")

    if minimo > maximo:
        print("Error, la población mínima ingresada, no puede ser mayor que la máxima.")
        return

    encontrado = False

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo: 
            print(pais)
            encontrado = True
    
    if not encontrado:
        print("No se encontraron países con ese rango de población.")
        return

def filtrar_superficie(paises):
    minima = pedir_numero("Ingrese la superficie mínima: ")
    maxima = pedir_numero("Ingrese la superficie máxima: ")

    if minima > maxima:
        print("Error, la superficie mínima ingresada, no puede ser mayor que la máxima.")
        return

    encontrado = False

    for pais in paises: 
        if minima <= pais["superficie"] <= maxima:
            print(pais)
            encontrado = True

    if not encontrado:
        print("No se encontraron países con ese rango de superficie.")
        return

def ordenar_nombre(paises):      

    paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"])          # creamos una nueva lista ordenanda por nombre y tomamos cada pais y usa ese nombre para ordenar.
    print("Países ordenados por nombre: ")

    for pais in paises_ordenados:
        print(pais)

def ordenar_poblacion(paises):

    paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"])
    print("Países ordenados por población: ")

    for pais in paises_ordenados:
        print(pais)

def ordenar_superficie(paises):

    paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"])
    print("Países ordenados por superficie: ")

    for pais in paises_ordenados:
        print(pais)

def mayor_poblacion(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])                        # buscamos el pais con el valor mas grande en el campo "poblacion"
    print("País con mayor población: ")
    print(pais_mayor)

def menor_poblacion(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    pais_menor = min(paises, key=lambda pais: pais["poblacion"])
    print("País con menor población: ")
    print(pais_menor)

def promedio_poblacion(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    
    suma = 0
    for pais in paises:
        suma += pais["poblacion"]
        
    promedio = suma / len(paises)

    print("Promedio de poblacion: ")
    print(promedio)

def promedio_superficie(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    
    suma = 0
    for pais in paises:
        suma += pais["superficie"]

    promedio = suma / len(paises)

    print("Promedio de superficie: ")
    print(promedio)

def cantidad_por_continente(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    
    continentes = {}    # creamos dicc vacio para guardar la cant por continente

    for pais in paises:
        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("Cantidad de Países por Continente: ")

    for continente, cantidad in continentes.items():   # recorremos el dicc
        print(f"{continente}: {cantidad}: ")