import flet as ft
from flet_route import Params, Basket
import time
from flet import *
login = {"gabriel":"123" , "jorge": "333"}


def login_view(page: ft.Page):
    page.window.resizable = False
    page.window.width = 500
    page.window.height = 660
    page.window.minimizable = False
    page.window.always_on_top = True
    page.window.center()
    page.bgcolor = colors.BLUE_600

    
    def verificar(e):
        value_gmail = gmail.value
        value_password = password.value
        if login.get(value_gmail) == value_password:
            print("tudo certo")
        else:
            print("n conseguiu logar")
    
    gmail = ft.TextField(label="email", hint_text="use @gmail.com" , width=400 )
    password = ft.TextField(label="senha", password=True, can_reveal_password=True, max_length=20, width=400)
    send_button = ft.CupertinoFilledButton(content=ft.Text("enviar"),opacity_on_click=0.7, on_click=verificar )
    space  = ft.Text('\n\n\n\n\n\n\n\n')
    page.add(
        ft.Row(controls=[ft.Container(content=space)]),
        ft.Row(controls=[gmail],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[password],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[send_button],alignment=ft.MainAxisAlignment.CENTER),

    )



ft.app(target=login_view)