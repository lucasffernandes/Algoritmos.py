'''A técnica de resolução de problemas DC busca dividir o problema em partes menores
    para assim resolve-lo como um todo. Este exemplo abaixo é um algoritmo recursivo 
    simples que faz a utilização dessa técnica'''


def soma(lista): 
    total = 0        # A variável x começa setada em o
    for x in lista:  # O laço for faz a iteração sobre os elementos contidos na lista
        total += x   # A cada iteração o valor é somado com o valor atual da variável x e armazenado o resultado na mesma
    return total
    
    
print (soma([1, 2, 3, 4, 5]))