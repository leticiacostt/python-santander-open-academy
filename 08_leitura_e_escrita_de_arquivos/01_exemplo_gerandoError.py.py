#ainda não tenho arquivo e vou gerar um erro: FileNotFoundError
arquivo =  open("dados.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()