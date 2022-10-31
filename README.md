![Lenguaje Python](https://img.shields.io/badge/Lenguaje-Python-green)
![Versión de Python 3.10](https://img.shields.io/badge/Versión%20de%20Python-3.10-green)


---

# Actualización de precios y redondeo a una cifra más comercial partiendo de un documento de InDesign
## Descripción
Partiendo de un catálogo de precios y servicios tenemos que incrementar los precios en un 5% y a esa cifra hay que redondearla por arriba y por último, hacer que termine en 5 o en 0.

Es necesario exportar la caja de texto a el formato 'Fragmento de Indesign' (con la extensión .idms) que nos genera un documento de texto con lenguaje de marcas de etiquetas que abren <…> y cierran </…>, al igual que HTML.

Estas etiquetas contiene todo el contenido necesario: formato, estilos usados, colores, etc y el contenido editorial.
Al ser un documento de texto es editable.


---
## Configuración de las búsquedas
- En este caso, pero dependerá del documento, ha sido necesario ejecutar dos búsquedas inteligentes:

  PATRON_SIMPLE = '(>[0-9]* €)'
    Para precios de 3 cifras.

  PATRON_COMPUESTO = '([0-9]*\.[0-9]* €)'
    Para precios de mas de tres cifras con punto qde separación de miles.

Por otra parte, el porcentaje de incremento viene reflejado en esta variable:
PORCENTAJE = 1.05


---
## Instrucciones de uso
- Desde Indesgin, seleccionamos la caja que contiene los datos a tratar y la exportamos como 'Fragmento de Indesign' (con la extensión .idms).
- Este paso es necesario con todas las cajas sobre las cuales queramos hacer los cambios.
- Ejecutamos el programa en Python: "redondeo y cambio a valor mas bonito.py"
- Nos pedira el nombre del archivo a modificar.
- Después de rastrear todo el archivo va a generar un archivo modificado que tiene el mismo nombre pero termina en " mod.idms" para mantener el original a salvo si fuera necesario.
- El último paso es, ya en Indesign, importar ese (o esos) fragmento(s) modificados.


---
## Manifiesto de los archivos del repositorio
- redondeo y cambio a valor mas bonito.py

  Aplicación en Python.


- README.md

  El archivo que estas leyendo.


---
## Errores conocidos
- El archivo generado no separa los miles de euros.


---
## Historial de versiones

### 1
- Versión base.


---
## Licencias y derechos de autor
CC (Creative Commons) de Reconocimiento – NoComercial – SinObraDerivada
![CC (Creative Commons) de Reconocimiento – NoComercial – SinObraDerivada](https://raw.githubusercontent.com/JavierPerezManzanaro/Maquetacion-de-masivos-responsive-html-con-noticias/main/Reconocimiento-no-comercial-sin-obra-derivada.png)


---
## Información de contacto del autor
Javier Pérez
javierperez@perasalvino.es


---
## Motivación
Automatizar tareas repetitivas.


---
## Créditos y agradecimientos
- A toda la comunidad web que me ha permitido ir ampliando mi formación.
- A mi familia por su infinita paciencia.
