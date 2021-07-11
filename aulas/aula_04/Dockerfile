# Multi Stage Building

## Build #1 

#1.1: preparar distro + instalação do python
FROM python:3.6-alpine as base 

#1.2: instalar as dependências a nível de aplicação (pip)

COPY ./requirements.txt /tmp

RUN mkdir /install

WORKDIR /install 

RUN pip install --prefix=/install  -r /tmp/requirements.txt

## Build #2

FROM base  

##2.1 copiar as dependências já preparadas

COPY --from=base /install /usr/local

# 2.2: copiar a aplicação para o contexto da imagem
RUN mkdir /app

COPY . /app/

WORKDIR /app

#2.3: configurar a porta de conexão da app (5000)
EXPOSE 5000

#2.4 definir variáveis de ambiente
ENV FLASK_ENV=development

# 2.5: executar um comando para subir o server flask
CMD flask run -h '0.0.0.0'
