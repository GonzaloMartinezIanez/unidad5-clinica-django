# Despliegue a producción - Compute Engine
Universidad Europea\
Despliegue a producción\
Ejercicio entregable de la Unidad 3\
Gonzalo Martínez Iáñez

Para ver el README.md de la entrega anterior consultar el commmit 4b44877

### Memoria


### Pasos para ejecutar la acción
Crear una cuenta en Compute Engine -> Habilitar Compute Engine API -> Crear instancia -> Nombre y elegir Madrid como Región -> Serie E para el tipo de máquina (e-2 small) -> pestaña de SO y almacenamiento -> Cambiar sistema operativo y almacenamiento -> Sistema Operativo: Container Optimized OS -> Pestaña de red -> Firewall: Permitir tráfico HTTP y HTTPS -> Crear la instancia
Acceder a la MV por SSH desde el navegador
```
docker pull ghcr.io/gonzalomartinezianez/unidad5-clinica-django:1.2.6
docker images
docker run -d --name=clinica -p 80:8000 -e SECRET_KEY="clavesecreta" --restart always ghcr.io/gonzalomartinezianez/unidad5-clinica-django:1.2.6
```

### Comprobación



### Conclusión
