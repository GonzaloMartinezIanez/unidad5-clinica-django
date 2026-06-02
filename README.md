# Despliegue a producción - Docker
Universidad Europea\
Despliegue a producción\
Ejercicio entregable de la Unidad 1\
Gonzalo Martínez Iáñez

Para ver el README.md de la entrega anterior consultar el commmit 4b44877

### Memoria
En este ejercicio se pide dockerizar un proyecto de nuestra elección.\
Para introducir este proyecto en una imagen de docker que luego se pueda hacer un contenedor, primero hay que instalar docker. En mi caso como uso Windows, he decidido instalar Docker Desktop ya que la interfaz gráfica ayuda a agilizar el proceso de vigilar y manejar los contenedores.\
En la carpeta /clinicapp hay un fichero Dockerfile, en él hay una serie de pasos que debe realizar docker para poder meter el código y las intrucciones para lanzarlo en una imagen. En primer lugar se instala una versión de python, se crea una carpeta donde se guardará el código fuente, se instalan las dependencias, se abre el puerto donde escuchará el contenedor y finalmente se da la instrucción necesaria para ejecutar la API.\
También hay un pequeño fichero dentro de /clinicapp llamado CHANGELOG.md donde se irán apuntando todos los cambios relevantes que se vayan produciendo. Usa un formato de KeepAChangelog. El proyecto no es muy grande, pero en el caso de que crezca es muy conveniente llevar un control con lo que se añade o se modifica en cada versión.

### Pasos para ejecutar docker
Primero hay que crear el .env, en este caso se puede eliminar el .example de .env.example ya que no se va a usar la base de datos MySQL. Lo único importante es cambiar la clave secreta para aportar seguridad a la API.

A continucación, se ejecuta el siguiente comando que compila el proyecto y crea la imagen:
```
docker build -t entrega1 .
```
Para lanzar el proyecto se puede hacer desde Docker Desktop indicando el puerto por el que escuchará el contenedor. O se puede ejecutar este comando que lanza en segundo plano el contenedor escuchando en el puerto 8000 de la máquina host.
```
docker run -d -p 8000:8000 entrega1
```

### Comprobación
Para comprobar que ha funcionado correctamente se pueden probar los siguientes endpoints:
```
http://127.0.0.1:8000/auth/
body: 
    {
        "username": "Marta",
        "password": "recepcionista1234"    
    }
```

```
http://127.0.0.1:8000/patient/viewset/
Headers:
    Authorization       -       Token 7962a24bb2ddb298304cd1fcd9238217f7cf9c22
```
### Conclusión
Docker es el sistema más utilizado para encapsular aplicaciones y desplegarlas en servidores remotos. Me parece una gran herramienta.\
Mi ejercicio no es del todo correcto ya que a pesar de que la aplicación corre perfectamente en el contenedor. Si se apaga y se vuelve a levantar, la información que se hubiera añadido a la base de datos sqlite desaparecerá y volverá a la versión original del proyecto. Para solucionar esto se debe crear un volumen donde se almacenará la base de datos que persistirá entre reinicios. He intentado crear el volumen pero aparecían errores que no he tenido tiempo de solucionar. Para siguientes entregas de esta asignatura, se continuará añadiendo cambios al CHANGELOG y se creará un contenedor con una base de datos MySQL si fuera necesario.