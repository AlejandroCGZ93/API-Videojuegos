from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from model.database_model import Videojuego, Lista
from peewee import fn

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)
        if parsed_path.path == '/search':
            self._handle_search(query)
        elif parsed_path.path == '/list':
            self._handle_list(query)
        else:
            self.send_error(404, 'Not Found')

    def _handle_search(self, query):
        filters = {}
        if 'nombre' in query:
            filters['nombre'] = query['nombre'][0]
        if 'genero' in query:
            filters['genero'] = query['genero'][0]

        results = (Videojuego
                   .select()
                   .where(fn.Lower(Videojuego.nombre).contains(filters.get('nombre', '').lower()),
                          fn.Lower(Videojuego.genero).contains(filters.get('genero', '').lower())))
        
        response = [{'id': v.id, 'nombre': v.nombre, 'genero': v.genero, 'plataforma': v.plataforma,
                     'desarrollador': v.desarrollador, 'publicador': v.publicador, 'fecha_lanzamiento': str(v.fecha_lanzamiento),
                     'ventas_totales': v.ventas_totales} for v in results]
        
        self._set_headers()
        self.wfile.write(json.dumps(response).encode())

    def _handle_list(self, query):
        if 'nombre' in query:
            lista, created = Lista.get_or_create(nombre=query['nombre'][0])
            response = {'nombre': lista.nombre, 'videojuegos': json.loads(lista.videojuegos)}
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(400, 'Bad Request')

    def do_POST(self):
        parsed_path = urlparse(self.path)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        if parsed_path.path == '/list':
            self._handle_add_to_list(json.loads(post_data))
        else:
            self.send_error(404, 'Not Found')

    def _handle_add_to_list(self, data):
        if 'nombre' in data and 'videojuego_id' in data:
            lista, created = Lista.get_or_create(nombre=data['nombre'])
            videojuegos = json.loads(lista.videojuegos or '[]')
            videojuegos.append(data['videojuego_id'])
            lista.videojuegos = json.dumps(videojuegos)
            lista.save()
            self._set_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())
        else:
            self.send_error(400, 'Bad Request')
