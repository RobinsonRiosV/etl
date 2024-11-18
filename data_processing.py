import pandas as pd

# Crear un DataFrame con las acciones disponibles y sus IDs correspondientes.
acciones_df = pd.DataFrame({'accion_id': [1, 2, 3], 'Accion': ['stock', 'transfer', 'sales']})

# Mapa de códigos de tienda (clave) a nombres de tiendas (valor).
tiendas_map = {
    '100': 'Dist. Center',
    '101': 'Madrid',
    '102': 'Andalucia',
    '103': 'Aragon',
    '104': 'Asturias',
    '105': 'Canarias',
    '106': 'Galicia',
    '107': 'Murcia',
    '108': 'Cataluña',
    '109': 'País Vasco',
    '110': 'Ceuta',
    '111': 'La Rioja',
    '112': 'Castilla-La Mancha',
    '113': 'Melilla',
    '114': 'Principado de Asturias',
    '115': 'Baleares',
    '116': 'Cantabria',
    '117': 'Comunidad Valenciana',
    '118': 'Melilla',
    '119': 'Madrid_Las Rozas',
    '120': 'Madrid_SS de los Reyes'
}

# Crear un DataFrame de tiendas con sus IDs y nombres.
tiendas_df = pd.DataFrame([{'tienda_id': id_tienda, 'tienda': tienda} for id_tienda, tienda in tiendas_map.items()])

# Diccionario para mapear acciones a sus IDs correspondientes.
acciones = {'stock': 1, 'transfer': 2, 'sales': 3}

# Función para crear un DataFrame de departamentos.
# Elimina duplicados y asigna un ID único a cada departamento.
def create_department_df(data):
    departments = data[['department']].drop_duplicates().reset_index(drop=True)
    departments['department_id'] = departments.index + 1
    return departments

# Función para crear un DataFrame de categorías.
# Se une con los departamentos para incluir el ID correspondiente.
def create_categories_df(data, departments):
    categories = data[['category', 'category_id', 'department']].drop_duplicates().reset_index(drop=True)
    categories = categories.merge(departments, on='department', how='left').drop(columns=['department'])
    return categories

# Función para crear un DataFrame de subcategorías.
# Relaciona cada subcategoría con su ID de categoría correspondiente.
def create_subcategories_df(data):
    subcategories = data[['subcategory', 'subcategory_id', 'category_id']].drop_duplicates().reset_index(drop=True)
    return subcategories

# Función para crear un DataFrame de productos.
# Incluye los IDs de producto, costo y la subcategoría asociada.
def create_product_df(data):
    product = data[['product', 'product_id', 'cost', 'subcategory_id']].drop_duplicates().reset_index(drop=True)
    return product

# Función para crear la tabla principal.
# Genera registros que asocian productos, tiendas, acciones e información de valor (como stock, ventas, etc.).
def create_principal_base(data):
    principal_base = []
    for col in data.columns:
        for key, tienda in tiendas_map.items():
            if key in col:
                accion = col.split('_')[1]  # Extraer la acción del nombre de la columna.
                id_accion = acciones[accion]  # Obtener el ID de la acción.
                id_tienda = tiendas_df.loc[tiendas_df['tienda'] == tienda].values[0][0]  # Obtener el ID de la tienda.

                # Crear registros para cada fila del DataFrame original.
                for _, row in data.iterrows():
                    principal_base.append({
                        'product_id': row['product_id'],
                        'tienda_id': id_tienda,
                        'accion_id': id_accion,
                        'valor': row[col]
                    })
    return pd.DataFrame(principal_base)

# Función principal para procesar el DataFrame original y generar todas las tablas necesarias.
def process_all(data):
    departments = create_department_df(data)  # Crear tabla de departamentos.
    categories = create_categories_df(data, departments)  # Crear tabla de categorías.
    subcategories = create_subcategories_df(data)  # Crear tabla de subcategorías.
    products = create_product_df(data)  # Crear tabla de productos.
    principal_base = create_principal_base(data)  # Crear la tabla principal.

    return departments, categories, subcategories, products, principal_base
