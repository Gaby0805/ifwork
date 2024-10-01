import flet as ft
from flet_route import Params, Basket

user_dict = {"gabriel":{"gmail: g@gmail.com ","senha: 123"}}

def create_user(page: ft.Page, params:Params, basket: Basket):
    
    def send(e):
        gmail_v = gmail.value     
        senha_v = senha.value

    
    
    gmail = ft.TextField(label='gmail' )
    senha = ft.TextField(label='senha' )
    send_button = ft.ElevatedButton("criar",on_click=send)
    
    
    
    