import flet as ft
from flet_route import Params, Basket

user_dict = {}

def create_user(page:ft.Page, params:Params,basket:Basket ):
    
        
            
    def send(e):
        nome_v = nome.value
        gmail_v = gmail.value     
        senha_v = senha.value
        add_user(nome_v,gmail_v,senha_v)
        
    def add_user(nome,email,senha):
        user_dict[nome] = {"email": email, "senha": senha}
        print(user_dict)
            
            
    nome = ft.TextField(label="nome")
    gmail = ft.TextField(label='gmail' )
    senha = ft.TextField(label='senha' )
    send_button = ft.ElevatedButton("criar",on_click=send)
    excluir_item = ft.ElevatedButton("excluir", on_click=lambda e: page.go("/excluir"))
    ft.View(
            "/criacao",controls=[
            nome,
            gmail,
            senha,
            send_button,
            excluir_item ]
    )
    
    