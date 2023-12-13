def pesquisa_linear(lista, alvo):
    """
    Implementa o algoritmo de busca linear ou também chamado "pesquisa simples", 
    que percorre todos os elementos um por um na estrutura de dados
    para retornar o elemento requisitado.
    
    Parameters:
    - lista: Uma lista de elementos.
    - alvo: O valor que estamos procurando na lista.
    
    Returns:
    - Se o alvo estiver na lista, retorna o índice onde foi encontrado.
    - Caso contrário, retorna -1.
    """
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  # retorna o índice do elemento caso encontrado.
    
    return -1  # O alvo não foi encontrado na lista.

# Exemplo de lista:
minha_lista = [1, 3, 5, 7, 9]
alvo_exemplo = 7

resultado = pesquisa_linear(minha_lista, alvo_exemplo)

if resultado != -1:
    print(f'O valor {alvo_exemplo} foi encontrado no índice {resultado}.')
else:
    print(f'O valor {alvo_exemplo} não foi encontrado na lista.')
