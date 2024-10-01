import flet as ft
from flet_route import Params, Basket
login = {"gabriel":"123" , "jorge": "333"}


def login_view(page: ft.Page, params:Params, basket:Basket):

    def verificar(e):
        try:
            value_gmail = gmail.value
            value_password = password.value
            if login.get(value_gmail) == value_password:
                page.go("/excluir")
            else:
                print("n conseguiu logar")
        except NameError as e:
            print(e)
            
    gmail = ft.TextField(label="email", )
    password = ft.TextField(label="senha",)
    send_button = ft.CupertinoFilledButton(content=ft.Text("enviar"), on_click=verificar )
    space  = ft.Text('\n\n\n\n\n\n\n\n')
    return ft.View("/",
        controls=[
            ft.Row(controls=[ft.Container(content=space)]),
            ft.Row(controls=[gmail],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[password],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[send_button],alignment=ft.MainAxisAlignment.CENTER),
    ]
    )



