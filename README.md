# Proyecto de Procesamiento de Datos Retail

Este proyecto tiene como objetivo procesar y normalizar una base de datos plano de ventas y productos de una cadena de retail.
La data original contiene información de productos, tiendas y acciones (como stock, transferencias y ventas), y se transforma en un formato relacional para facilitar su análisis 
en herramientas como Power BI.

## Descripción del Proyecto

La data original contiene múltiples columnas con información agregada, como ventas por tienda y producto. El proceso de este proyecto transforma esta data en varias tablas relacionadas entre sí, eliminando redundancias y mejorando su estructura para facilitar el análisis de los datos.

Las tablas generadas son:

- **Departments**: Contiene la lista de departamentos, cada uno con un ID único.
- **Categories**: Relaciona productos con sus categorías y departamentos, facilitando su organización.
- **Subcategories**: Incluye las subcategorías de productos, vinculadas a las categorías correspondientes.
- **Products**: Una lista de productos con sus IDs, costos y subcategorías asociadas.
- **Principal Base**: Esta tabla reúne información detallada sobre las acciones (stock, transferencias, ventas) realizadas en cada tienda, para cada producto.


## Requisitos

Este proyecto utiliza Python 3 y las siguientes librerías:

- `pandas`: Para el manejo y procesamiento de datos.
- `os`: Para la gestión de carpetas.

Puedes instalar las librerías necesarias ejecutando el siguiente comando:

```bash
pip install pandas
