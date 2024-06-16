from peewee import SqliteDatabase
from model.database_model import Videojuego
from services.read_csv import read_csv
from datetime import datetime
import pandas as pd

sqlite_db = SqliteDatabase('videojuegos_.db', pragmas={'journal_mode': 'wal'}) 

class ManagementVideogames:
    @classmethod
    def data_extract(cls):
        df = read_csv()

        if df is False:
            print("Error al leer el CSV.")
            return False

        try:
            with sqlite_db.atomic():
                for index, row in df.iterrows():
                    # Manejar el año como cadena si es válido, de lo contrario, usar un valor por defecto
                    year = row['Year']
                    if pd.isna(year) or not str(year).isdigit():
                        print(f"Error: formato de fecha incorrecto para '{year}'. Saltando este registro.")
                        continue
                    
                    fecha_lanzamiento = datetime.strptime(str(int(year)), '%Y')

                    # Manejar valores NaN en ventas
                    ventas_totales = float(row['Global_Sales']) if not pd.isna(row['Global_Sales']) else 0.0

                    Videojuego.create(
                        nombre=row['Name'],
                        genero=row['Genre'],
                        plataforma=row['Platform'],
                        desarrollador='',
                        publicador=row['Publisher'],
                        fecha_lanzamiento=fecha_lanzamiento.date(),
                        ventas_totales=ventas_totales
                    )
            return True
        except Exception as e:
            print("Error al cargar datos desde el CSV:", e)
            return False
