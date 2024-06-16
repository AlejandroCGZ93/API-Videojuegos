# main.py
from http.server import HTTPServer
from controller.videogame_controller import RequestHandler
from model.database_model import sqlite_db, Videojuego, Lista
from model.management_videogames import ManagementVideogames

def create_tables():
    with sqlite_db:
        sqlite_db.create_tables([Videojuego, Lista])

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    create_tables()
    ManagementVideogames.data_extract()  # Cargar datos desde CSV si es necesario
    httpd.serve_forever()

if __name__ == '__main__':
    run()
