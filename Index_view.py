import flet as ft
from flet_route import Params, Basket


login = {"gabriel":"123" , "jorge": "333"}


def login_view(page: ft.Page):
    
    gmail = ft.TextField(label="email", hint_text="use @gmail.com" , width=400 )
    password = ft.TextField(label="senha", password=True, can_reveal_password=True, max_length=20, width=400)
    
    
    page.add(gmail,password)
ft.app(login_view)