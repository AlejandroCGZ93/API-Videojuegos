import pandas as pd
from models.database_model import Videojuego

def read_csv():
    df = pd.read_csv('data/videojuegos.csv')
    for _, row in df.iterrows():
        Videojuego.create(
            nombre=row['Nombre'],
            genero=row['Genero'],
            plataforma=row['Plataforma'],
            desarrollador=row['Desarrollador'],
            publicador=row['Publicador'],
            fecha_lanzamiento=row['Fecha_Lanzamiento'],
            ventas_totales=row['Ventas_Totales']
        )
    return df
