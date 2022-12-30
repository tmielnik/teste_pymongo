# Importação de bibliotecas
from pymongo import MongoClient # Conexão com banco de dados
from decouple import config # Dados sensíveis com variáveis de ambiente
from pprint import pprint # Visualização de dados estruturada no console
#from bson.objectid import ObjectId # Importa classe ObjectId para trabalhar com consultas por _id


# Variáveis de acesso ao banco de dados
MONGODB_HOST=config('MONGODB_HOST')
MONGODB_PORT=config('MONGODB_PORT')
MONGODB_USER=config('MONGODB_USER')
MONGODB_PASSWORD=config('MONGODB_PASSWORD')


# Conecta com o servidor do banco de dados
def connect_serverdb():
    try:
        connection = MongoClient(f'mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}')
    except:
        print('Erro ao conectar com o servidor do banco de dados')
    
    return connection


# Lista bancos de dados
def list_databases(client):
    try:
        databases = list(client.list_database_names())
        print(f'Bancos de dados disponíveis: {databases}')
    except Exception as error:
        print(error)


# Mostra a quantidade de documentos da coleção de dados
def count_documents(collection):
    print(f'Total geral de documentos da coleção de dados: {collection.count_documents({})}')


# Insere um novo documento na coleção de dados
def insert_document(collection, document):
    contact_id = collection.insert_one(document).inserted_id
    print(f'_id inserido: {contact_id}')
    
    return contact_id


# Consulta um documento na coleção de dados
def find_document(collection, id):
    filter_query = {'_id':id}
    projection = {'_id':False}
    result = collection.find_one(filter_query, projection)
    pprint(result)


# Atualiza um documento da coleção de dados
def update_document(collection, id, field):
    filter_query = {'_id':id}
    projection = {'$set':field}
    result = collection.update_one(filter_query, projection)
    print(f'Resultado do Update: {result.raw_result}')


# Deleta um documento da coleção de dados
def delete_document(collection, id):
    filter_query = {'_id':id}
    result = collection.delete_one(filter_query)
    print(f'Resultado do delete: {result.raw_result}')


# Lista todos os documentos da coleção de dados
def list_documents(collection):
    filter_query = {}
    result = list(collection.find(filter_query))
    pprint(result)