
import flet as ft

class IconText(ft.Row):
    def __init__(self, text: str, icon: any, size: int, font: str, text_align: ft.TextAlign = ft.TextAlign.CENTER, row_alignment: ft.MainAxisAlignment = ft.MainAxisAlignment.CENTER, position: bool = True):
        super().__init__()
        self.text_view = ft.Text(text, size=size, text_align=text_align, font_family=font)
        self.icon = ft.Icon(icon)
        self.alignment = row_alignment
        if position:
            self.controls = [
                self.icon,
                self.text_view,
            ]
        else:
            self.controls = [
                self.text_view,
                self.icon,
            ]