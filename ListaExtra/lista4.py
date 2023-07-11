def func(lista, n):
    # retira os n maiores e n menores da lista e retorna o resultado
    lista.sort()
    lista = lista[n:-n]
    return lista

# pedir o nome do arquivo
nome = input("Digite o nome do arquivo: ")

try:
    # abrir o arquivo .py
    arquivo = open(nome+".txt", "r")
except:
    print("Arquivo não encontrado")
else:
    # ler o arquivo que consiste de apenas uma linha com números separados por espaço e transformar em uma lista de reais
    lista = arquivo.readline().split()
    lista = [float(x) for x in lista]
    lista_nova = func(lista, 2)
    print("Lista nova:", lista_nova)
    print("Lista original:", lista)

    # fechar o arquivo
    arquivo.close()