import flet as ft
import webbrowser

from .service import loadAnimes


class Anime(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.animes = loadAnimes()

    def build(self):
        images = []
        for anime in self.animes:
            images.append(
                ft.Card(
                    content=ft.Container(
                        width=300,
                        padding=10,
                        content=ft.Column(
                            [
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    content=ft.Text(anime['attributes']['titles']['en_jp'], style=ft.TextThemeStyle.BODY_MEDIUM, text_align=ft.TextAlign.CENTER)
                                ),
                                ft.Row([
                                    ft.Container(
                                        content=ft.Image(
                                            src=f"{anime['attributes']['posterImage']['tiny']}",
                                            fit=ft.ImageFit.NONE,
                                            repeat=ft.ImageRepeat.NO_REPEAT,
                                            border_radius=ft.border_radius.all(10),
                                        )
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text(anime['attributes']['ageRatingGuide'], style=ft.TextThemeStyle.BODY_SMALL, text_align=ft.TextAlign.START),
                                                ft.Text(
                                                    f"{anime['attributes']['subtype']} - {anime['attributes']['status']}",
                                                    style=ft.TextThemeStyle.BODY_SMALL,
                                                    text_align=ft.TextAlign.END
                                                ),
                                                ft.Row(
                                                    [
                                                        ft.Icon(name=ft.icons.PERSON, color=ft.colors.GREEN),
                                                        ft.Text(f"{anime['attributes']['userCount']}", style=ft.TextThemeStyle.BODY_SMALL,)
                                                    ],
                                                    spacing=1,
                                                    run_spacing=1,
                                                ),
                                                self.rating(anime['attributes']['favoritesCount']),
                                            ]
                                        )
                                    )
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.START
                                )
                            ],
                        )
                    ),
                )
            )

        return ft.Row(
            wrap=True,
            spacing=1,
            run_spacing=1,
            controls=images
        )

    def rating(self, favorites):
        return ft.Row(
            [
                ft.Icon(name=ft.icons.STAR, color=ft.colors.YELLOW),
                ft.Text(favorites, style=ft.TextThemeStyle.BODY_SMALL)
            ],
            spacing=1,
            run_spacing=1,
        )

