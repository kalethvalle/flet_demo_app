import flet as ft
from src.components.animes.anime import Anime

class Home(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.update()

    def build(self):
        animes = Anime()
        return animes
