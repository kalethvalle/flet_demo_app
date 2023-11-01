import flet as ft
from src.views.home.home import Home
from src.components.navigations.navigation import Navigation

class Routes(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.update()

    def route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        [
                            Navigation(self.page),
                            ft.VerticalDivider(width=1),
                            ft.Container(
                                expand=True,
                                content=ft.Column(
                                    [
                                        ft.Text('initial Home')
                                    ],
                                    expand=True
                                )
                            )
                        ],
                        expand=True,
                        vertical_alignment=ft.CrossAxisAlignment.START
                    )
                ],
            )
        )
        if self.page.route == "/store":
            self.page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.Row(
                            [
                                Navigation(self.page),
                                ft.VerticalDivider(width=1),
                                ft.Container(
                                    expand=True,
                                    content=ft.Column(
                                        [
                                            ft.Text('aqui ejemplo'),
                                            ft.Column(
                                                [
                                                    Home(self.page)
                                                ],
                                                scroll=ft.ScrollMode.AUTO,
                                                expand=True
                                            )
                                        ],
                                        expand=True
                                    ),
                                )
                            ],
                            expand=True,
                            vertical_alignment=ft.CrossAxisAlignment.START
                        )
                    ],
                )
            )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

