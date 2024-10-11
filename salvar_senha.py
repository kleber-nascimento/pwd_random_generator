from datetime import datetime

def salvar_senha(senha):
    with open("senhas.txt", "a") as arquivo:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"{data_hora} - {senha}\n")
    print("Senha salva no arquivo senhas.txt")