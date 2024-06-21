# model/database_model.py
from peewee import *
from datetime import datetime

# Conexión a la base de datos
sqlite_db = SqliteDatabase('videojuegos_.db', pragmas={'journal_mode': 'wal'}) 

try:
    sqlite_db.connect()
except OperationalError as e:
    print("Error al conectar con la Base de Datos.", e)
    exit()

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class Videojuego(BaseModel):
    nombre = CharField()
    genero = CharField()
    plataforma = CharField()
    desarrollador = CharField()
    publicador = CharField()
    fecha_lanzamiento = DateField()
    ventas_totales = FloatField()

class Lista(BaseModel):
    nombre = CharField()
    videojuegos = TextField()
    fecha_creacion = DateTimeField(default=datetime.now)
    fecha_modificacion = DateTimeField(default=datetime.now)
    fecha_eliminacion = DateTimeField(null=True)

# Crear las tablas si no existen
sqlite_db.create_tables([Videojuego, Lista])
