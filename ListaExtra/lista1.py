# pedir o nome do arquivo
nome = input("Digite o nome do arquivo: ")

try:
    # abrir o arquivo .py
    arquivo = open(nome+".py", "r")
except:
    print("Arquivo não encontrado")
else:
    # criar um arquivo novo
    arquivo_novo = open(nome + "2.py", "w")
    # ler o arquivo
    for linha in arquivo:
        # se houver um # no começo da linha, remover
        if linha[0] == "#":
            linha = linha[1:]
        # guardar linha em um arquivo novo
        arquivo_novo.write(linha)
    # fechar o arquivo novo
    arquivo_novo.close()

    # fechar o arquivo
    arquivo.close()