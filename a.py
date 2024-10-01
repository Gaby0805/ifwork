user_dict = {"gabriel": {"gmail": "g@gmail.com", "senha": "123"},"calebe": {"gmail": "j@gmail.com", "senha": "1232"}}

# Acessando o valor da senha
senha = user_dict["calebe"]["gmail"] 
print(senha)
senha = user_dict["calebe"]["gmail"] = "sexo1"
print(senha)