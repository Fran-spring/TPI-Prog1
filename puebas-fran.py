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

def mostrar_menu():
    print("\n" + "-" * 40)
    print("Gestión de Datos de Paises")
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
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida")

main()