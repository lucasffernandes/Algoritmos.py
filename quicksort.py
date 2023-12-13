def quicksort(array):
    if len(array) < 2:
        return array # caso Base: arrays com 0 ou 1 elemento já estão ordenandas
    else:
        pivo = array[0] # caso recursivo
        menores = [i for i in array[1:] if i <= pivo] # armazena na variável menores os valores que forem menores ou iguais ao pivo escolhido
        maiores = [i for i in array[1:] if i > pivo]  # armazena na variável maiores os valores que forem maiores ao pivo escolhido
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([54, 29, 23, 86, 320, 293, 32, 12, 0, 12, 4, 19, 123, 444, 4141]))

'''O algoritmo quicksort é muito conhecido e muito utilizado na criação de programas, ele faz de forma elegante a ordenação de elementos. A principal estratégia desse algoritmo é a utilização de um elemento pivô, que pode ser qualquer elemento da array, como um marco divisor, para que os elementos menores sejam adicionados a uma subarray do lado esquedo, e os maiores sejam adicionados a uma subarray do lado direito. Após os elementos estando em seus devidos lugares e em seus respectivos subarrays, será feito a ordenação dos mesmos (esse processo deve ocorrer dentro de seus respectivos subarrays ) antes de proceguir para o passo final, que é a CONCATENAÇÃO (ou junção de elementos), do subarray do lado esquerdo, pivo e do suarray do lado direito'''

# OBS: seu tempo de execução é de O(n log n), nos casos médios. Em piores casos a notação é O(n^2)