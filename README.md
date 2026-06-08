# Despliegue a producción - GitHub Actions
Universidad Europea\
Despliegue a producción\
Ejercicio entregable de la Unidad 2\
Gonzalo Martínez Iáñez

Para ver el README.md de la entrega anterior consultar el commmit 4b44877

### Memoria
En esta actividad se pide que usando GitHub Actions se construya el proyecto cada vez que se introduce un nuevo tag en el repositorio. Para esto es necesario crear el fichero .ci.yml dentro de una carpeta .github/workflows/ en la raíz del repositorio. En ese fichero se especifica que cada vez que se haga push con un nuevo tag, GitHub lo construya en sus servidores y lo empaquete en un zip. De esta forma se puede asegurar que no hay errores de compilación. Adicionalmente, también lo he configurado para que genere una imagen del proyecto que se pueda descargar de manera pública. Para ello hay que seguir los siguientes pasos:

Generar un token.\
Desde la cuenta de github Settings -> Developer settings -> Personal access token -> Token classic -> Generate new token -> Dar un nombre -> Dar permisos de (write:packages y delete:packages) -> Generar token -> Copiar el token porque solo se muestra una vez (Volver a generarlo si se pierde)

Añadir este token a este repositorio.\
Copiar el secreto en el repositorio: Settings -> Secrets and variables -> Actions -> New repository secret -> Dar un nombre y copiar el token

### Pasos para ejecutar la acción
Primero hay que añadir las nuevas funcionalidades de esta versión. Se crea el commit y también un nueva etiqueta. Cuando se cumplen estos pasos y se hace un "push" a GitHub, se desencadenarán las GitHub Actions que construirá el proyecto y si lo ha creado exitosamente, creará la imagen de docker.

```
git add .
git commit -m "Documentación y .dockerignore"
git tag 1.2.3
git push
```

### Descargar la imagen
En el repositorio solo sale "Releases", pero también hay un "Package" que se accede mediante la siguiente url:
```
docker pull ghcr.io/gonzalomartinezianez/unidad5-clinica-django:1.2.3
```
En el apartado de Packages de la web, no hay ningún paquete, no sé si hay que hacer algo más o que tarda en actualizarse.

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
Es la primera vez que hago uso de las GitHub Actions y es complicado de configurar, pero una vez que funciona, las ventajas son muy importantes. En un proyecto serio que hay que desplegarlo en un entorno real, no se puede perder el tiempo asegurandose de que la nueva versión funciona correctamente en el servidor. De esta forma, se automatiza el proceso y hay que preocuparse de otros aspectos.