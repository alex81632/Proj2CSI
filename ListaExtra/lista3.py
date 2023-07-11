def translateCesar(carac, chave):
    minusculo = "abcdefghijklmnopqrstuvwxyz"
    maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if carac in minusculo:
        indice = minusculo.index(carac)
        indice = (indice + chave) % 26
        return minusculo[indice]
    elif carac in maiusculo:
        indice = maiusculo.index(carac)
        indice = (indice + chave) % 26
        return maiusculo[indice]
    else:
        return carac

# pedir o nome do arquivo
nome = input("Digite o nome do arquivo: ")

try:
    # abrir o arquivo .py
    arquivo = open(nome+".txt", "r")
except:
    print("Arquivo não encontrado")
else:
    # criar um arquivo novo
    arquivo_novo = open(nome + "2.txt", "w")
    # ler o arquivo
    for linha in arquivo:
        chave = linha[0]
        if chave == "-":
            chave = int(linha[0:2])
            linha = linha[2:]
        else:
            chave = int(linha[0])
            linha = linha[1:]

        for carac in linha:
            carac = translateCesar(carac, chave)
            arquivo_novo.write(carac)

    # fechar o arquivo novo
    arquivo_novo.close()

    # fechar o arquivo
    arquivo.close()