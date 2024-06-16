# model/management_videogames.py
from peewee import *
from model.database_model import Videojuego, Lista
from services.read_csv import read_csv

class ManagementVideogames():
    @classmethod
    def data_extract(cls):
        cls.df = read_csv()  # Implementar esta función en services/read_csv.py
        
        if cls.df is False:
            exit()

    @classmethod
    def conectar_db(cls):
        from database_model import sqlite_db
        sqlite_db.connect()
