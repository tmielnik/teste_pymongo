## Sobre
Este é um simples projeto em python para utilizar o banco de dados mongodb com a biblioteca pymongo.

<h4 align="center"> 
	🚧 Em construção para a realização de testes 🚧
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#Sobre)
   * [Tabela de conteúdos](#Tabela-de-conteúdos)
   * [Tecnologias utilizadas](#Tecnologias-utilizadas)
   * [Como executar o projeto](#-Como-executar-o-projeto)
      * [Pré-requisitos](#Pré-requisitos)
      * [Executando os comandos](#Executando-os-comandos)
      * [Criando o banco de dados](#Criando-o-banco-de-dados)
      * [Executando os testes](#Executando-os-testes)
   * [Autor](#-Autor)
   * [Licença](#-Licença)
<!--te-->

## 💻 Tecnologias utilizadas
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Pymongo](https://pymongo.readthedocs.io)

## 🚀 Como executar o projeto

### Pré-requisitos
- É preciso que você tenha o python e o Docker já instalados.
- (Opcional): Utilize um editor de texto de sua preferência para escrever e executar os códigos.
- (Opcional): Utilize o [MongoDB Compass](https://www.mongodb.com/products/compass) para facilitar a visualização dos dados no mongodb.

### Executando os comandos
```bash

    # Criar um ambiente virtual no python para instalação das bibliotecas a serem utilizadas.
    $ python -m venv venv
    
    # Selecionando o ambiente virtual criado.
    $ .\venv\Scripts\activate
    
    # Instalar as dependências do projeto.
    $ pip install -r requirements.txt
    
    # Criar um arquivo ".env" no diretório atual do projeto com as seguintes variáveis:
    MONGODB_HOST=endereço do host (Ex: localhost).
    MONGODB_PORT=porta do serviço do banco de dados (Ex: 27017).
    MONGODB_USER=nome do usuario de acesso ao banco de dados (Ex: admin).
    MONGODB_DBNAME=nome do banco de dados padrão a ser iniciado no serviço (Ex: admin).
    MONGODB_PASSWORD=senha do usuário de acesso ao banco de dados (Ex: s3nh@).
    
    # Iniciar o container com o serviço do banco de dados.
    $ docker-compose up
    
```

### Criando o banco de dados
- Acessar o MongoDB Compass
- Criar uma nova conexão:
  <p align="center">
    <img src="https://user-images.githubusercontent.com/32055359/210122856-569bb627-56a8-4f97-ac44-4b17222653f6.png" width="600px">
    <img src="https://user-images.githubusercontent.com/32055359/210122885-1d6711f0-006d-427b-b82c-1b5583f760e7.png" width="600px">
  </p>
- Criar o banco de dados com o nome "test" e a coleção com o nome "contatos":
  <p align="center">
    <img src="https://user-images.githubusercontent.com/32055359/210123542-28cb2024-e698-4fb8-b051-169e633dbd15.png" width="600px">
  </p>

### Executando os testes
```bash
    # Executa os testes com as funções escritas em python.
    $ python .\test_functions.py
```
**Resultado:** 
os testes consistem em realizar as operações de CRUD no banco de dados na seguinte ordem:
  - Insert de um documento na coleção "contatos".
  - Busca do documento inserido anteriormente.
  - Update do documento inserido inicialmente.
  - Delete do documento inserido inicialmente.

Antes da execução da operação de delete, é possível consultar no MongoDB Compass o documento inserido inicialmente. 
<p align="center">
    <img src="https://user-images.githubusercontent.com/32055359/210123270-da893432-58a0-43b5-af44-d3dc8f2095b6.png" width="900px">
</p>

Ao final da execução o documento inserido é deletado, ficando sem nenhum registro no banco de dados.

---
## 🦸 Autor
Desenvolvido por Tiago Ajala Mielnik.

---
## 📝 Licença
Licença [MIT](./LICENSE).
