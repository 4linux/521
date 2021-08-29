# Aula 10: Projeto

## Sobre o desafio

Este desafio é baseado em testes práticos relacionados a desenvolvimento _backend_ em si, incluindo elementos de infraestrutura e integração comuns em ambientes de esteira DevOps.

## Enunciado

Pede-se o desenvolvimento de uma API, cuja finalidade seja o **gerenciamento de um estoque**.

Para fins deste exercício:

- Um estoque é uma coleção de **produtos**.
- Um produto pode ser caracterizado a partir dos seguintes atributos:
  - nome
  - descrição
  - quantidade
  - preço unitário

- As funcionalidades esperadas de um estoque são:
  1. Adicionar um novo produto;
  1. Remover um produto existente;
  1. Adicionar uma unidade em um produto existente
  1. Remover uma unidade em um produto existente
  1. Atualizar informações de um produto existente
  1. Listar os produtos de um determinado estoque
  1. Buscar produto por:
    - Nome
	- Intervalo de Quantidade
	- Intervalo de Preço
  1. Total de produtos em um determinado estoque
  1. Valor total de produtos em um determinado estoque

## Entregáveis

### Obrigatório

1. Repositório público com o código fonte da API
1. Uma descrição do projeto no README.md do repositório, indicando como acessar a API, seja através de uma montagem de infraestrutura local ou através de alguma plataforma de publicação através do seu endereço eletrônico. 


### Diferenciais

Para além das funcionalidades listadas no enunciado, seguem pontos que são considerados diferenciais na entrega do exercício: 

1. Autenticação
1. Logs
1. Integração
1. Testes


### Infraestrutura

Ao longo curso vimos como utilizar o **Docker** e utilitários de gerenciamento como o `docker-compose`. Além destes, vimos como criar uma esteira, utilizando ferramentas de integração com a publicação e uso de plataformas gratuitas como Gitlab e Heroku. 

Você pode optar por:

1. Desenvolver uma infraestrutura local, baseada em contêiner com as instruções para sua utilização e utilizando o `docker-compose` para sumarizar as imagens e recursos necessários;

1. Utilizar ferramentas de integração para que, além de utilizar o Docker como plataforma de desenvolvimento, você possa explicitar as etapas utilizadas desde o versionamento de código até a publicação (recomendado).

### Frontend

Não é exigido o desenvolvimento do _frontend_. No entanto, há uma sugestão deste no diretório `app` desta aula. Você esta livre para criar o seu _frontend_.


