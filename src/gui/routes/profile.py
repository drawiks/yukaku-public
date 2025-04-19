import flet as ft

class ProfileRoute:
    def build(self, navigation_rail):
        return ft.View(
            "/",
            [
                ft.Container(
                    content=
                        ft.Row(
                            [
                                navigation_rail,
                                ft.Column(
                                    [
                                        ft.Text("профиль", size=30),
                                        ft.ElevatedButton("Перейти на страницу профиля", on_click=lambda e: e.page.go("/")),
                                    ]
                                )
                            ],
                        ),
                        expand=True
                ),
                
            ]
        )
