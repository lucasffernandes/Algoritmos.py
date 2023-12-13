'''
Algoritmos de busca binária necessitam que os elementos das estruras de dados estejam ordenados para que a busca funcione,
sabendo disso, aqui se faz escrito um algoritmo de ordenação de dados, que recebe uma arrey de elementos desordenados e retorna uma arrey ordenada de menor para o maior desses elementos.

'''

def busca_menor(arr):
    menor = arr[0]               # Armazena o menor valor
    menor_indice = 0             # Armazena o índice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):     # Ordenações em um arrey
    novoArr = []                  # Encontra o menor elemento de um arrey e adiciona ao novo arrey
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))