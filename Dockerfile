#Imagen oficial de python
FROM python
#Instalar dependencis
RUN pip install sqlalchemy
RUN pip install psycopg2-binary
RUN pip install Flask
#Exponerpuertos
EXPOSE 5000
#Define directorio de trabajo
WORKDIR /app
#Copiar archivos del proyecto
COPY app .
#Variable de Entorno
ENV FLASK_APP app.py
#Ejecutar aplicacion
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]