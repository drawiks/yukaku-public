
import flet as ft
from gui.widgets._icontext import IconText

class HomeRoute:
    def __init__(self):
        #post
        self.yukaku = IconText(text="YUKAKU", icon=ft.Icons.AUTO_AWESOME, size=72, font="jersey")
        self.post_column = ft.Column(spacing=20)
        self.post_field = ft.TextField(label="Что у вас нового?", multiline=True, max_lines=10, width=750)
    
    def build(self, navigation_rail):
        return ft.View(
            "/",
            [
                ft.Container(
                    content=ft.Row(
                        [
                            navigation_rail,
                            ft.Column(
                                [
                                    self.yukaku,
                                ]
                            )
                        ],
                    ),
                    expand=True
                ),
                
            ]
        )
