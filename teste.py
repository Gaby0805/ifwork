import math
import flet as ft

login = {"gabriel": "123", "jorge": "333"}

def main(page: ft.Page):
    width = 500
    height = 660

    def verificar(e):
        value_gmail = gmail.value
        value_password = password.value
        if login.get(value_gmail) == value_password:
            print("tudo certo")
        else:
            print("n conseguiu logar")

    gmail = ft.TextField(label="email", hint_text="use @gmail.com", width=400)
    password = ft.TextField(label="senha", password=True, can_reveal_password=True, max_length=20, width=400)
    send_button = ft.CupertinoFilledButton(content=ft.Text("enviar"), opacity_on_click=0.7, on_click=verificar)

    def page_return():
        return ft.Column(
            controls=[
                ft.Container(height=100),  # Espaço acima para centralizar melhor
                ft.Row(controls=[gmail], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=[password], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=[send_button], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER  # Centraliza os itens dentro da coluna
        )

    page.add(
        ft.Container(
            content=page_return(),
            alignment=ft.alignment.center,  # Alinha o conteúdo dentro do container
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(0.8, 1),
                colors=[
                    "0xff1f005c",
                    "0xff5b0060",
                    "0xff870160",
                    "0xffac255e",
                    "0xffca485c",
                    "0xffe16b5c",
                    "0xfff39060",
                    "0xffffb56b",
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
            ),
            width=width,
            height=height,
            border_radius=5,  # Definindo diretamente o valor para o border_radius
        )
    )

ft.app(target=main)
