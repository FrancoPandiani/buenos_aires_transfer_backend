# Servidor dedicado a el microservicio de autenticación con su versión de python, logs, directorio y requerimientos.
FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

# Comando para correr el servidor de Django.
CMD python manage.py runserver 0.0.0.0:8000