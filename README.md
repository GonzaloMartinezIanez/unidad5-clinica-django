# Django avanzado - Clínica
Universidad Europea\
Fundamendos de backend con python\
Ejercicio entregable de la Unidad 5\
Gonzalo Martínez Iáñez

## Instalación
Crear el entorno virtual
```
py -m venv venv
```
Activar el entorno (Windows, para linux o mac usar su forma para ejecutar programas)
```
.\venv\Scripts\activate
```
Instalar la librerias necesarias
```
pip install -r requirements.txt
```
Crear una base de datos MySQL:
```
CREATE DATABASE clinica CHARACTER SET UTF8;

GRANT ALL PRIVILEGES ON clinica.* TO exampleuser@localhost;
```
Crear el fichero .env en la carpeta clinicapp (junto al manage.py) con la información necesaria para acceder a la base de datos. Por ejemplo:
```
DB_NAME = 'clinica'
DB_USER = 'root'
DB_PASSWORD = '...'
DB_HOST = 'localhost'
DB_PORT = '3306'
```
Para crear las tablas de los modelos propios y los de Django hay que hacer:
```
py .\manage.py migrate
```
Ahora hay que importar la información por defecto desde el fichero datadump_utf8.json.
```
py .\manage.py loaddata .\datadump_utf8.json
```
Finalmente hay que ejecutar el siguiente comando y hacer peticiones a la url: http://127.0.0.1:8000
```
py .\manage.py runserver
```
### Exportar datos desde sqlite
En la línea 80 del fichero [settings.py](./clinicapp/clinicapp/settings.py) se puede cambiar la base de datos que se usará. Para volcar la información de la base de datos actual se deberá ejecutar el siguiente comando:
```
py .\manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 --output datadump.json
```
Esto creará un fichero datadump.json con todas las tablas y su contenido. Si se ha realizado desde Windows, este fichero no estará en formato UTF-8 sino en Latin-1. Por tanto hay que convertirlo a UTF-8 con el siguiente fichero.
```
py .\convert-utf8.py
```

## Memoria
En este ejercicio se solicita la implementación de una API utilizando Django, con una temática libre. El servidor deberá contar con al menos dos modelos, endpoints que hagan uso de ambos y un sistema de permisos que impida que ciertos usuarios realicen peticiones para las que no estén autorizados.\

El proyecto simula el funcionamiento de una clínica en la que existen distintos roles. Por un lado, los recepcionistas se encargan de registrar la información de los pacientes y pueden crear y eliminar citas. Por otro lado, los médicos pueden consultar las citas existentes y, una vez finalizada la consulta, añadir el diagnóstico y marcar la cita como finalizada.

### Modelos
Hay dos modelos:
- Patient: Representa los datos de un paciente.
    - name: Nombre.
    - last_name: Apellidos.
    - dni: DNI único de la persona.
    - phone_number: Número de teléfono.
    - birth_date: Fecha de nacimiento.
- Appointment: 
    - patient: ID del paciente (foreign key).
    - appointment_date: Fecha y hora de la consulta.
    - diagnosis: Diagnóstico que rellena el médico tras la consulta.
    - status: Estado actual de la cita, puede ser pendiente o finalizada.

### Permisos
Para la gestión de permisos ha sido necesario crear dos grupos distintos desde el panel de administración de Django: Medicos y Recepcionistas. A cada uno de estos grupos se le han asignado permisos específicos sobre los modelos del sistema:

* Recepcionistas: pueden realizar operaciones CRUD sobre los pacientes, así como leer, crear y eliminar citas.
* Médicos: pueden listar los pacientes y leer y modificar las citas.

Es importante tener en cuenta que, al crear una cita, los recepcionistas únicamente pueden seleccionar el paciente y la hora. Por su parte, los médicos solo pueden modificar los atributos "status" y "diagnosis" de las citas.\
En este caso, se ha creado un único usuario por cada grupo. Para obtener sus credenciales es necesario utilizar el endpoint de autenticación, enviando el nombre de usuario y la contraseña. Este proceso devuelve un token que deberá incluirse en las cabeceras del resto de las peticiones de la siguiente forma: Authentication: Token "token_del_usuario".\
Las credenciales de los dos usuarios son las siguientes:
```
Médico: username: Pedro, password: medico1234, token = "Token 729acab2fde374490d446ff14d3b4a21eab6dfe2"
Recepcionista: username: Marta, password: recepcionista1234, token =  "Token 7962a24bb2ddb298304cd1fcd9238217f7cf9c22"
```

### Endpoints
La raíz de la API es la siguiente: http://127.0.0.1:8000/ y los endpoints son los siguientes:
- Token: auth/
    - POST : Se pasa el usuario y contraseña en el cuerpo y devuelve su token.
- Pacientes : patient/
    - Viewset : viewset/
        - GET : Devuelve todos los pacientes (Médicos y Recepcionistas).
        - POST : Añade un nuevo paciente con los datos "name", "last_name", "dni", "phone_number" y "birth_date" (Recepcionistas).
        - PUT y PATCH : "DNI"/ Modifica un paciente (Recepcionistas).
        - DELETE : "DNI"/ Elimina un paciente (Recepcionista).
    - Historial del paciente : history/
        - GET : /"DNI"/ Devuelve todas sus consultas (pendientes y finalizadas) .(Médicos y Recepcionistas)
- Consultas : appointment/
    - Viewset : viewset/
        - GET : Develve todas las consultas (Médicos y Recepcionistas).
        - POST : Crea una consulta con el id del paciente y la fecha (Recepcionistas).
        - DELETE : destroy/"id"/ Elimina una consulta por su id (Recepcionista).
    - Finalizar consulta : end/
        - PATCH : "id"/ Da por finalizada una consulta hay que mandar en el body el "diagnosis" (Médicos).
    - Pendientes : pending/
        - GET : Devuelve todas las consultas pendientes (Médicos y Recepcionistas).

Para probar los endpoints, en la raíz del proyecto hay un fichero llamado "PruebaEndpoints.postman_collection.json" que se puede importar en Postman.

### Test
Hay una serie de test que verifican el buen funcionamiento de los endpoints. Para ejecutarlo hay que usar la siguiente instrucción:
```
py .\manage.py test
```

### Conclusión
Django me sigue pareciendo una herramienta muy cómoda de utilizar, ya que se encarga de la gestión de los modelos y de la validación de los datos de forma automática.\

El único problema que he encontrado ha sido al exportar la base de datos SQLite a MySQL. Al generar el archivo datadump.json, en sistemas Windows este no se codifica en UTF-8, lo que provoca un error de formato al intentar importarlo en el servidor MySQL. Para solventar este inconveniente, he creado un script que transforma el archivo del volcado de datos y lo convierte a UTF-8.