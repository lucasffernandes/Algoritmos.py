''' Uma função hash, verifica se o item consta na tabela e printa o valor, caso contrário ele armazena o ítem na tabela e atribui seu valor'''




votaram = dict()      # só um atalho para a criação de um dicionário, mesmo resultado daria se colocasse: votaram = dict().

def verifica_eleitor(nome):
    if votaram.get(nome):
        print("mande embora!")
    else:
        votaram[nome] = True
        print("deixe votar!")

verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("tom")
verifica_eleitor("mateus")
verifica_eleitor("filipe")
verifica_eleitor("gustavo")
verifica_eleitor("mike")

print(votaram)