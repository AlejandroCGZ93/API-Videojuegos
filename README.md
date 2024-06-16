##### API de Videojuegos

--- Documentación ---

*Basado en la estructura MVC, la API de Videojuegos se divide en distintas carpetas que a continuación serán explicadas:

·Controller: Contiene los endpoints de los cuales se realizan las solicitudes http desde el lado de cliente. Contiene videogame_controller donde se encuentra las solicitudes de tipo GET y Post respectivamente. Contiene funciones para realizar consultas a la Base de Datos sobre videojuegos, también tiene funciones que crea y
devuelve las listas que el usuario crea y en los cuales se encuentra info de los juegos que el usuario agrega en dicha lista.

·Data: Contiene el csv con el cual la Base de Datos obtiene los registros de los videojuegos para su posterior utilización. Las columnas que se extraen del csv son: Nombre, genero, plataforma, desarrollador, publicador, fecha de lanzamiento y ventas totales.

·Model: Contiene la creación de la Base de Datos, la creación de las tablas y columnas. También en ella se agregan los datos del csv en la base de datos.
Los archivos que la contiene son database_model que es donde se construyen las tablas lista y videojuegos, la conexión es a SQLite utilizando peewe como ORM.
Por otra parte management_videogames carga los datos necesarios del csv en la base de datos.

·Services: Contiene el archivo read_csv que obtiene los datos del csv y realiza una limpieza de datos para mantener la base de datos normalizada.

main.py: Es el archivo que se utiliza para que la API se levante y funcione correctamente.


Busca los videojuegos por nombre y genero

GET http://localhost:8000/search?nombre=Pokemon&genero=racing

Crea la lista que el usuario desee con los juegos que desee

POST http://localhost:8000/list

Obtiene la lista que el usuario creo

GET http://localhost:8000/list?nombre=Favoritos
