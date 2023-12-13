
# tabelas hash em python são chamadas de dicionário.

'''
EXEMPLO 01:

caderno = dict() 

caderno["maça"] = 0.67
caderno["leite"] = 1,49
caderno["abacate"] = 1.49

print(caderno["abacate"])

'''
# Exemplo 2

'''
lista_telefonica = dict()

lista_telefonica["jenny"] = 2222222
lista_telefonica["emergency"] = 190

print(lista_telefonica["jenny"])

'''
# Exemplo 3

''' Nesse exemplo a tabela verifica se a URL já foi armazenada em cachê, caso sim ele a retorna sem precisar sobrecarregar o servidor com mais uma tarefa, a função só procura no servidor caso o endereço não foi armazenado no cache'''

cache = dict()         

def pega_dados_do_servidor(url):
    
    return len(url)

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados
