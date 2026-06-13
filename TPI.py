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

def mostrar_menu():
    print("\n" + "-" * 40)
    print("Gestión de Datos de Paises")
    print("-" * 40)
    print("1. Mostrar todos los paises")
    print("2. Agregar Pais")
    print("3. Actualizar Pais")
    print("4. Buscar Pais por nombre")
    print("5. Filtrar Paises")
    print("6. Ordenar Paises")
    print("7. Estadisticas")
    print("0. Salir")
