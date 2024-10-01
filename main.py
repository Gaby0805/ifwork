import flet as ft
from flet_route import Routing,path
from create import create_user
from delete import delete
from Index_view import login_view
def routes(page:ft.Page):
    try:
        app_routes = [
            path(
                url="/",
                clear=True,
                view=login_view
            ),
            path(
                url="/create",
                clear=False,
                view=create_user
            ),
            path(
                url="/excluir",
                clear=False,
                view=delete
            )
        ]
        Routing(
            page=page,
            app_routes=app_routes
        )
        page.go(page.route)
    except TabError as e:
        print(e)
ft.app(target=routes)

