# Importação das funções de manipulação do banco de dados
from query_functions import *


'''
    Testes das funções de manipulação do banco de dados
'''

# Conexão com o server do banco de dados
client = connect_serverdb()
list_databases(client)


# Seleciona um banco de dados
db = client.get_database('test')


# Obtêm os nomes das coleções do banco de dados
collections_list = db.list_collection_names()
print(f'Collections do banco de dados {db.name}: {collections_list}')


# Seleciona uma coleção de dados
current_collection = db.get_collection('contatos')
print(f'Collection selecionada: {current_collection.name}')


# Insere um novo documento na coleção de dados atual
print()
data = {
    'name':'Fulano',
    'telefone': '67 77777-7777',
    'email':'fulano@gmail.com',
    'idade':99
}
id = insert_document(current_collection, data)


# Realiza consulta pelo id na coleção de dados atual
print()
find_document(current_collection, id)


# Realiza update pelo id na coleção de dados atual
print()
update_document(current_collection, id, field = {'idade':90})
find_document(current_collection, id)


# Deleta documento pelo id na coleção de dados atual
print()
input('Pressione ENTER para deletar o documento...')
delete_document(current_collection, id)


# Lista todos os documentos da coleção
print()
list_documents(current_collection)


# Mostra o total de documentos da coleção atual
print()
count_documents(current_collection)
