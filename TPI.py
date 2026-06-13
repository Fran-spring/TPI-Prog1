import csv

PAISES = "paises.csv"

def cargar_paises():
    paises = []
    try:
        with open(PAISES, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    paises.append({
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    })
                except (ValueError, KeyError):
                    print(f"Advertencia: fila con formato incorrecto: {fila}")
    except PermissionError:
        print("Error: el archivo está siendo utilizado por otro programa")
    return paises

def mostrar_paises(paises):
    if not paises:
        print("No hay paises para mostrar.")
        return
    print(f"\n{'Nombre':<25} {'Poblacion':>15} {'Superficie (km2)':>18} {'Continente':<15}")
    print("-" * 75)
    for p in paises:
        print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<15}")

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

    paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"])          
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
    
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])                        
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
    
    continentes = {}    

    for pais in paises:
        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("Cantidad de Países por Continente: ")

    for continente, cantidad in continentes.items():   
        print(f"{continente}: {cantidad}")

def mostrar_menu():
    print("\n" + "-" * 40)
    print("Gestion de Datos de Paises")
    print("-" * 40)
    print("1. Mostrar todos los paises")
    print("2. Agregar pais")
    print("3. Actualizar pais")
    print("4. Buscar pais por nombre")
    print("5. Filtrar por continente")
    print("6. Filtrar por poblacion")
    print("7. Filtrar por superficie")
    print("8. Ordenar por nombre")
    print("9. Ordenar por poblacion")
    print("10. Ordenar por superficie")
    print("11. Mayor poblacion")
    print("12. Menor poblacion")
    print("13. Promedio poblacion")
    print("14. Promedio superficie")
    print("15. Cantidad de paises por continente")
    print("0. Salir")

def main():
    paises = cargar_paises()
    while True:
        mostrar_menu()
        opcion = input("Elegir opcion: ").strip()
        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_paises(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_continente(paises)
        elif opcion == "6":
            filtrar_poblacion(paises)
        elif opcion == "7":
            filtrar_superficie(paises)
        elif opcion == "8":
            ordenar_nombre(paises)
        elif opcion == "9":
            ordenar_poblacion(paises)
        elif opcion == "10":
            ordenar_superficie(paises)
        elif opcion == "11":
            mayor_poblacion(paises)
        elif opcion == "12":
            menor_poblacion(paises)
        elif opcion == "13":
            promedio_poblacion(paises)
        elif opcion == "14":
            promedio_superficie(paises)
        elif opcion == "15":
            cantidad_por_continente(paises)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida.")

main()
