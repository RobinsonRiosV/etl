import pandas as pd
import os
from data_processing import process_all, tiendas_df, acciones_df

# Verificar si la carpeta 'transformed_data' existe, si no, crearla
if not os.path.exists('../transformed_data'):
    os.makedirs('../transformed_data')

# Cargar la data original
df = pd.read_csv('../raw_data/df_retail.csv')

# Procesar la informacion
departments, categories, subcategories, products, principal_base = process_all(df)

# Guardamos la Data Transformada
departments.to_csv('../transformed_data/departments.csv', index=False)
categories.to_csv('../transformed_data/categories.csv', index=False)
subcategories.to_csv('../transformed_data/subcategories.csv', index=False)
products.to_csv('../transformed_data/products.csv', index=False)
principal_base.to_csv('../transformed_data/principal_base.csv', index=False)
tiendas_df.to_csv('../transformed_data/tiendas.csv', index=False)
acciones_df.to_csv('../transformed_data/acciones.csv', index=False)             
