usuario_correto = "Leticia" #usuário correto
senha_correta = "Leticia123" #senha correta

tentativas = 0 #contador de tentativas iniciando em 0
login_realizado = False

while tentativas < 3: #enquanto o nuemro de tentativas for menor que 3, continua repetindo
    print(f"Tentativa {tentativas + 1}/3")

    usuario = input("Digite seu usário: ") #solicitando o usuario 
    senha = input("Digite sua senha: ") #solicitando a senha

    if usuario == usuario_correto and senha == senha_correta: #verifica se o usuario digitado e a senha digitada são iguais aos dados cadastrados
        login_realizado = True
        break #interrompe p while imediatamente e sai do loop

    else: #senão, ele avisa que está incorreto 
        print("Usuário ou senha incorretos. Tente novamente.")
        tentativas += 1 #vai até a tentativa 3 depois para

if login_realizado:
    print("Login realizado com sucesso!")
else:
    print(f"Usuário bloqueado após {tentativas} tentantivas.")