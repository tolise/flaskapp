# Importa alpine

FROM alpine:3.10

# Instala python3, pip3 y actualiza pip3

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Establece el directorio de trabajo

WORKDIR /flaskapp

# Copia directorio local al directorio de trabajo

COPY . /flaskapp

# Instala dependencias especificadas en requirements.txt

RUN pip3 --no-cache-dir install -r requirements.txt

