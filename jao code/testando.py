import flet as ft  # Importa a biblioteca Flet, que permite criar interfaces gráficas.

# Dicionário de usuários com emails e senhas
user_dict = {
    "gabriel": {"email": "gabriel111", "senha": "111"},
    "jorge": {"email": "jorge123", "senha": "123"}
}
login = {"joao": "123", "joabe": "456"}  # Dicionário para armazenar as credenciais de login

# Função principal que é chamada quando o aplicativo é iniciado
def main(page: ft.Page):  # Recebe um objeto `page` do tipo `ft.Page`, que representa a página da interface.

    # Função para verificar o login
    def verificar_login(e):  # Recebe um evento `e` como parâmetro.
        email = login_email.value  # Captura o valor do campo de entrada do email.
        senha = login_senha.value  # Captura o valor do campo de entrada da senha.

        # Verifica se o email está no dicionário de login e se a senha é correta
        if email in login and login[email] == senha:
            carregar_interface_usuario()  # Se o login for bem-sucedido, carrega a interface de criação/exclusão de usuários.
        else:
            print("Login inválido")  # Caso contrário, exibe uma mensagem de erro no console.

    # Função para carregar a interface de criação e exclusão de usuários
    def carregar_interface_usuario():
        # Limpa todos os controles da tela atual (login)
        page.controls.clear()

        # Cria campos de entrada para a criação de um novo usuário
        nome_field = ft.TextField(label="Nome")  # Campo para inserir o nome do usuário.
        gmail_field = ft.TextField(label="Email")  # Campo para inserir o email do usuário.
        senha_field = ft.TextField(label="Senha")  # Campo para inserir a senha do usuário.
        # Botão para criar um novo usuário, que chama a função `criar_usuario` ao ser clicado
        send_button = ft.ElevatedButton("Criar Usuário", on_click=lambda e: criar_usuario(nome_field, gmail_field, senha_field))

        # Cria um dropdown (menu suspenso) para selecionar um usuário para exclusão
        user_dropdown = ft.Dropdown(
            label="Usuário para deletar",  # Rótulo do dropdown
            options=[ft.dropdown.Option(user) for user in user_dict]  # Adiciona opções ao dropdown a partir do dicionário de usuários
        )
        # Botão para deletar o usuário selecionado no dropdown
        delete_button = ft.ElevatedButton("Deletar Usuário", on_click=lambda e: deletar_usuario(user_dropdown))
        
        # Adiciona novos controles à página (tela única de criação e exclusão)
        page.add(
            ft.Text("Criar Usuário"),  # Texto informativo para a seção de criação de usuário
            nome_field, gmail_field, senha_field, send_button,  # Adiciona campos de entrada e botão
            ft.Divider(),  # Adiciona uma linha divisória
            ft.Text("Excluir Usuário"),  # Texto informativo para a seção de exclusão de usuário
            user_dropdown, delete_button  # Adiciona dropdown e botão de exclusão
        )

    # Função para criar um novo usuário
    def criar_usuario(nome_field, gmail_field, senha_field):
        nome = nome_field.value  # Captura o nome do novo usuário.
        email = gmail_field.value  # Captura o email do novo usuário.
        senha = senha_field.value  # Captura a senha do novo usuário.
        user_dict[nome] = {"email": email, "senha": senha}  # Adiciona o novo usuário ao dicionário `user_dict`.
        print(user_dict)  # Exibe o dicionário atualizado no console.
        carregar_interface_usuario()  # Atualiza a interface com o novo usuário adicionado.

    # Função para deletar um usuário
    def deletar_usuario(user_dropdown):
        usuario = user_dropdown.value  # Captura o usuário selecionado no dropdown.
        if usuario in user_dict:  # Verifica se o usuário está no dicionário.
            user_dict.pop(usuario)  # Remove o usuário selecionado do dicionário.
            print(f"Usuário {usuario} excluído")  # Exibe mensagem de confirmação no console.
            carregar_interface_usuario()  # Atualiza a interface após a exclusão.

    # Tela de login inicial
    login_email = ft.TextField(label="Email")  # Campo de entrada para o email do usuário.
    login_senha = ft.TextField(label="Senha", password=True)  # Campo de entrada para a senha (oculta os caracteres).
    # Botão de login que chama a função `verificar_login` quando clicado
    login_button = ft.ElevatedButton("Login", on_click=verificar_login)

    # Adiciona os controles de login à página
    page.add(login_email, login_senha, login_button)  # Adiciona os campos de email, senha e o botão de login.
    page.update()  # Atualiza a página para mostrar os controles de login.

# Inicializa o aplicativo, chamando a função `main` quando a aplicação é iniciada.
ft.app(target=main)