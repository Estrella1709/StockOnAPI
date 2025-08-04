# Imagen de Python
FROM python:3.13-alpine

# Establece el directorio de trabajo en /app
WORKDIR /api

# Copia los archivos de la API al contenedor
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará la API
EXPOSE 5000

# Comando para ejecutar la API
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0","--port", "5000"]