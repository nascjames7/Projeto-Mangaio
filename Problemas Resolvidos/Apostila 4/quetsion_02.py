try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
 print("Erro: Arquivo não encontrado!")
finally:
    arquivo.close()
 