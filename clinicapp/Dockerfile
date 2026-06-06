# Usar la versión de python slim ya que es más ligera
# Analiza las dependencias y eliminas las innecesarias
FROM python:3.13

# Crear una carpeta en la raíz del contenedor
RUN mkdir /app

# Asociar la carpeta creada al espacio de trabajo
WORKDIR /app

# Copiar los paquetes que debe instalar en la carpeta
COPY clinicapp/requirements.txt  .

# Instalar los paquetes
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto a la carpeta /app
COPY clinicapp/ .
 
# Exponer el puerto 8000 al exterior para que nuestra máquina
# pueda consumir los endpoints del contenedor
EXPOSE 8000

# Finalmente decidir los comando necesarios para poner en marcha el sevidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]