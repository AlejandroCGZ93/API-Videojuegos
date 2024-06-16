import pandas as pd
from datetime import datetime

def read_csv():
    archivo = 'data/vgsales.csv'
   
    try: 
        df = pd.read_csv(archivo, sep=",")

        # Limpiar los años eliminando el '.0'
        df['Year'] = df['Year'].astype(str).str.replace('.0', '')

        # Eliminar registros con valores NaN en las columnas que pueden ser convertidas a fechas
        df = df.dropna(subset=['Year'])  # Eliminar registros donde 'Year' es NaN

        # Convertir 'Year' a una fecha válida
        df['fecha_lanzamiento'] = pd.to_datetime(df['Year'], errors='coerce')

        # Eliminar registros con fechas inválidas ('NaT' representa una fecha inválida)
        df = df.dropna(subset=['fecha_lanzamiento'])

        return df
    except FileNotFoundError as e:
        print("Error al ejecutar el archivo", e)
        return False
