# Dicionário para armazenar os dados dos usuários
user_dict = {}

# Função para adicionar usuários
def adicionar_usuario(user_dict, nome, email, senha):
    # Verificar se o usuário já existe 
    if nome in user_dict:
        print(f"Usuário {nome} já existe!")
        return
    
    # Adicionar o novo usuário ao dicionário
    user_dict[nome] = {"gmail": email, "senha": senha}
    print(f"Usuário {nome} adicionado com sucesso.")

# Exemplo de uso da função
adicionar_usuario(user_dict, "gabriel", "g@gmail.com", "123")
adicionar_usuario(user_dict, "joao", "joao@gmail.com", "456")
adicionar_usuario(user_dict, "maria", "maria@gmail.com", "789")

# Exibindo o dicionário atualizado
print(user_dict)
