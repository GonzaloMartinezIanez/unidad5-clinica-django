# unidad5-clinica-django
Entrega de la unidad 5 de la asignatura Fundamentos de backend con python
Pacientes
    CRUD - Recepcionistas
    Leer - Medicos

Citas
    GET, POST (Siempre pendiente y sin diagnostico) y DELETE - Recepcionistas
    Leer - Medicos
    Pasar de pendiente a finalizada y diagnostico - Medicos
    Ver la historia de un paciente - Medicos

Pedro - medico1234 - "Token 729acab2fde374490d446ff14d3b4a21eab6dfe2"
Marta - recepcionista1234 "Token 7962a24bb2ddb298304cd1fcd9238217f7cf9c22"

CREATE DATABASE clinica CHARACTER SET UTF8;

GRANT ALL PRIVILEGES ON clinica.* TO root@localhost;

py .\manage.py migrate

py .\manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 --output datadump.json

Convertir los datos a utf-8 (Solo si se usa Windows)
py .\convert-utf8.py

py .\manage.py loaddata .\datadump_utf8.json