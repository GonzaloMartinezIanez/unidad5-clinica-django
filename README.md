# Despliegue a producción - Docker
Universidad Europea\
Despliegue a producción\
Ejercicio entregable de la Unidad 1\
Gonzalo Martínez Iáñez

Para ver el README.md de la entrega anterior consultar el commmit 4b44877

### Memoria
Desde la cuenta de github Settings -> Developer settings -> Personal access token -> Token classic -> Generate new token -> Dar un nombre -> Dar permisos de (write:packages y delete:packages) -> Generar token -> Copiar el token porque solo se muestra una vez (Volver a generarlo si se pierde)
Copiar el secreto en el repositorio: Settings -> Secrets and variables -> Actions -> New repository secret -> Dar un nombre y copiar el token
Crear un commit y un tag
```
git add .
git commit -m "Añadir workflow"
git tag 1.2.0
git push
```


### Conclusión
Docker es el sistema más utilizado para encapsular aplicaciones y desplegarlas en servidores remotos. Me parece una gran herramienta.\
Mi ejercicio no es del todo correcto ya que a pesar de que la aplicación corre perfectamente en el contenedor. Si se apaga y se vuelve a levantar, la información que se hubiera añadido a la base de datos sqlite desaparecerá y volverá a la versión original del proyecto. Para solucionar esto se debe crear un volumen donde se almacenará la base de datos que persistirá entre reinicios. He intentado crear el volumen pero aparecían errores que no he tenido tiempo de solucionar. Para siguientes entregas de esta asignatura, se continuará añadiendo cambios al CHANGELOG y se creará un contenedor con una base de datos MySQL si fuera necesario.