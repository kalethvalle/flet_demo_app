import flet as ft
from src.views.home.home import Home
from src.routes.routes import Routes

def main(page: ft.Page):
    page.title = "Routes Example"
    routes = Routes(page)

    page.on_route_change = routes.route_change
    page.on_view_pop = routes.view_pop
    page.go(page.route)


ft.app(main)
