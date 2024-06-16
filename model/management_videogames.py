from peewee import SqliteDatabase, Model, CharField, DateField, FloatField
from model.database_model import Videojuego, Lista
from services.read_csv import read_csv
from datetime import datetime

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
                    # Convertir 'Year' a una fecha válida
                    year = str(row['Year'])  # Convertir a cadena explícitamente
                    try:
                        fecha_lanzamiento = datetime.strptime(year, '%Y')
                    except ValueError:
                        print(f"Error: formato de fecha incorrecto para '{year}'. Saltando este registro.")
                        continue

                    # Continuar con el proceso de inserción en la base de datos
                    Videojuego.create(
                        nombre=row['Name'],
                        genero=row['Genre'],
                        plataforma=row['Platform'],
                        desarrollador='',  # Ajustar según tus datos reales
                        publicador=row['Publisher'],
                        fecha_lanzamiento=fecha_lanzamiento.date(),  # Asegúrate de usar .date() para obtener solo la fecha
                        ventas_totales=row['Global_Sales']  # Ajustar según tus datos reales
                    )
            
            return True
        except Exception as e:
            print("Error al cargar datos desde el CSV:", e)
            return False