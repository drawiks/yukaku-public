import flet as ft

class NotFoundRoute:
    def build(self):
        return ft.View(
            "/404",
            [
                ft.Text("Страница не найдена", size=30, color=ft.Colors.RED),
                ft.ElevatedButton("Вернуться на главную", on_click=lambda e: e.page.go("/")),
            ]
        )
