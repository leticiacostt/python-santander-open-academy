arquivo = open("08_leitura_e_escrita_de_arquivos/dados.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()