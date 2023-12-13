
'''este é um exemplo de um algoritmo de busca binária, que faz a busca pergorrendo a todos os elementos de uma lista numérica ordenada e retorna seu elemento de maneira otimizada e em tempo de execução O(log n)'''

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2         
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1  

    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))