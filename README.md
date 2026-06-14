# Gestión de Datos de Países

**Tecnicatura Universitaria en Programación - UTN**
Materia: Programación 1
Integrantes: Francisco Leonel Cardenas / Sofia Antonella Caliari

---

## ¿De qué se trata?

Este proyecto consiste en una aplicación desarrollada en Python que permite gestionar información dedistintos países mediante el uso de listas, diccionarios, funciones y archivos CSV.
El sistema permite agregar, buscar, actualizar, filtrar, ordenar y obtener estadísticas sobre los paísesalmacenados en el dataset.
El objetivo principal es aplicar los conceptos aprendidos durante la cursada, especialmente el manejo deestructuras de datos, modularización del código, lectura de archivos CSV y validación de datos ingresadospor el usuario.

## Tecnologías utilizadas
- Python 3.x
- CSV (Comma Separated Values)
- Git y GitHub

## Estructura del proyecto
```
TPI-Prog1/
│
├── TPI.py
├── paises.csv
├── README.md
├── Documentacion.pdf
└── (otros archivos auxiliares)
```

## Archivo CSV
El sistema utiliza un archivo llamado
"paises.csv" para almacenar la información.
Formato:
```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
```
## Instrucciones de ejecución
1. Clonar el repositorio
gitclone[URL_DEL_REPOSITORIO]

2. Ingresar a la carpeta
cdTPI-Prog1

3. Ejecutar el programa
pythonTPI.py

## ¿Cómo se usa?

Para ejecutar correctamente el programa, es necesario contar previamente con Python 3 instalado en el sistema. Luego, se debe descargar o clonar el repositorio correspondiente y verificar que el archivo paises.csv se encuentre ubicado en el mismo directorio que el archivo principal TPI.py, ya que de lo contrario el programa no podrá acceder a los datos necesarios para su funcionamiento.

Una vez cumplidos estos requisitos, se puede proceder a ejecutar el programa. Al iniciarlo, se mostrará en pantalla un menú interactivo que contiene todas las opciones disponibles, permitiendo al usuario navegar y utilizar las distintas funcionalidades desarrolladas en el trabajo práctico de manera ordenada y sencilla.

## ¿Qué puede hacer?

El programa tiene 15 opciones:

- Mostrar todos los países cargados
- Agregar un nuevo país con su nombre, población, superficie y continente
- Actualizar la población y superficie de un país existente
- Buscar un país por nombre, acepta coincidencia parcial
- Filtrar países por continente
- Filtrar países por rango de población
- Filtrar países por rango de superficie
- Ordenar países por nombre
- Ordenar países por población
- Ordenar países por superficie
- Ver el país con mayor población
- Ver el país con menor población
- Ver el promedio de población
- Ver el promedio de superficie
- Ver la cantidad de países por continente

## Ejemplos de uso

Al agregar un país el programa te va pidiendo los datos de a uno. Si dejás un campo vacío o ingresás letras donde van números, te avisa y te pide que lo ingreses de nuevo.

Al buscar, no hace falta escribir el nombre completo. Si escribís "arg" te aparece Argentina.

Al filtrar por población o superficie, ingresás un mínimo y un máximo y el programa te muestra todos los países que caen en ese rango.
```
Ingrese el País: Argentina
Ingrese la cantidad de la población: 45376763
Ingrese la cantidad de la superficie: 2780400
Ingrese el Continente: America
```
- Buscar Pais
Ingrese el País a buscar: Argentina
```
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400,
'continente': 'America'}
```
```
- Estadísticas
País con mayor población:
Brasil
Promedio de población:
129685100
```
## Conclusión
Este trabajo práctico permitió aplicar de manera integral los conceptos fundamentales abordados en la asignatura Programación 1, haciendo especial énfasis en el uso de estructuras de datos como listas y diccionarios, la implementación de funciones, la realización de validaciones de datos, la lectura y procesamiento de archivos CSV, y el trabajo colaborativo mediante el uso de Git y GitHub.

Asimismo, la realización del proyecto contribuyó a reforzar buenas prácticas de programación, tales como la correcta organización del código, la modularización de las distintas funcionalidades y el desarrollo de estrategias eficientes para la resolución de problemas en equipo.

## Integrantes

- Francisco Leonel Cardenas
- Sofia Antonella Caliari

## Links
```
Links al repositorio del proyecto : 
Link del video explicativo: 
Enlace a la documentación en PDF: 
```
