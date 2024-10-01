import flet as ft
from  create import user_dict
from flet_route import Basket, Params

def delete(page: ft.Page, basket: Basket, params:Params):
    def pop_item(user):
        user_dict.pop(user)
        
    def delete_user(e):
        value =lista_user.value
        pop_item(value)
        page.update()
        
    lista_user = ft.Dropdown(label="usuario para deletar", options=[ft.dropdown.Option(i) for i in user_dict])
    delete_user_button = ft.ElevatedButton("deletar usuario", on_click=delete_user)
    voltar = ft.ElevatedButton("voltar", on_click=lambda e: page.go("/create"))
    return ft.View(
        "/excluir",
        controls=[
            lista_user,
            delete_user_button,
            voltar
            
            
        ]
        
    )
        
