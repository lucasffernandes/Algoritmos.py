'''
grafo = {}
grafo["voce"] = {"alice", "bob", "claire"}

Acima, este singelo e pequeno grafo["voce"], devolverá um vetor de nomes associados'''

# A implementação de um algoritmo ficaria assim:


grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["claire"] = ["peggy"]
grafo["anuj"] = ["thom", "jonny"]
grafo["peggy"] = [] # chama-se de dígrafo vértices como esse não associadas a nenhuma outra
grafo["thom"] = []
grafo["jonny"] = []

'''Os grafos nada mais são do que tabelas hash, de vértices associados uns aos outros por meio de arestas'''


from collections import deque

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + "é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

print(pesquisa("voce"))


