artistas = {
    "Nome": "Lagum",
    "Estilo musical": "Pop rock",
    "País": "Brasil",
    "Ano de início": "2015",
    "Status": "Pior banda do Brasil"
}

print(artistas.keys()) #me mostra as chaves do dicionário
print(artistas.values()) #me mostra os valores do dicionário
print(artistas.items()) #me mostra as chaves e valores do dicionário

artistas["Cidade"] = "Belo Horizonte" #informação que adicionei depois no dicionário
artistas["Ano de início"] = 2016 #informação que alterei no dicionário
del artistas["Status"] #informação que deletei do dicionário
artistas["Integrantes"] = 4 #adicionando
artistas["Estilo musical"] = "Indie Pop" #alterando
del artistas["País"] #deletando


print("========== PERFIL DE ARTISTAS ==========") #vou mostrar as informações dicionário de forma organizada
print("Nome:", artistas["Nome"])
print("Estilo musical:", artistas["Estilo musical"])
print("Ano de início:", artistas["Ano de início"])
print("Cidade:", artistas["Cidade"])
print("Integrantes:", artistas["Integrantes"])