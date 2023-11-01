import flet as ft

class Navigation(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.update()

    def build(self):
        if self.page.route == "/":
            iconHome = ft.icons.HOME_OUTLINED
            iconAnime = ft.icons.SMART_DISPLAY
        elif self.page.route == "/store":
            iconHome = ft.icons.HOME
            iconAnime = ft.icons.SMART_DISPLAY_OUTLINED

        return ft.Column(
            [
                ft.TextButton(
                    on_click=lambda _: self.page.go("/"),
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(name=iconHome),
                                ft.Text('Home', style=ft.TextThemeStyle.BODY_SMALL)
                            ],
                            spacing=5,
                            run_spacing=5,
                        )
                    )
                ),
                ft.TextButton(
                    on_click=lambda _: self.page.go("/store"),
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(name=iconAnime),
                                ft.Text('Animes', style=ft.TextThemeStyle.BODY_SMALL)
                            ],
                            spacing=5,
                            run_spacing=5,
                        )
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START
        )
