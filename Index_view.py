import flet as ft
from flet_route import Params, Basket
import time
from flet import *
login = {"gabriel":"123" , "jorge": "333"}


def login_view(page: ft.Page, params:Params, basket:Basket):

    def verificar(e):
        value_gmail = gmail.value
        value_password = password.value
        if login.get(value_gmail) == value_password:
            page
        else:
            print("n conseguiu logar")
    
    gmail = ft.TextField(label="email", )
    password = ft.TextField(label="senha",)
    send_button = ft.CupertinoFilledButton(content=ft.Text("enviar"),opacity_on_click=0.7, on_click=verificar )
    space  = ft.Text('\n\n\n\n\n\n\n\n')
    return ft.View("/", controls=[
                   
        ft.Row(controls=[ft.Container(content=space)]),
        ft.Row(controls=[gmail],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[password],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[send_button],alignment=ft.MainAxisAlignment.CENTER),
    ]
    )


