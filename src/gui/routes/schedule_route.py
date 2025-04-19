
import flet as ft
from gui.widgets._icontext import IconText
from gui.widgets._timepick import TimePick
from core.service.table_manager import TableManager

class ScheduleRoute:
    def __init__(self):
        #self.yukaku = IconText(text="YUKAKU", icon=ft.Icons.AUTO_AWESOME, size=72, font="jersey")
        self.weekday_dropdown = ft.Dropdown(
            label="Weekday", 
            options=[
                    ft.DropdownOption(text="Monday"),
                    ft.DropdownOption(text="Tuesday"),
                    ft.DropdownOption(text="Wednesday"),
                    ft.DropdownOption(text="Thursday"),
                    ft.DropdownOption(text="Friday"),
                    ft.DropdownOption(text="Saturday"),
                    ft.DropdownOption(text="Sunday"),
                ],
            width=140
        )
        
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
                                        IconText(text="It`s your weekday schedule", font="plex medium", icon=ft.Icons.EDIT_CALENDAR, size=34),
                                        ft.Row(
                                            [
                                                self.weekday_dropdown,
                                                TimePick(),
                                                ft.IconButton(icon=ft.Icons.ADD_OUTLINED)
                                            ]
                                        ),
                                    ]
                                )
                            ],
                        ),
                        expand=True
                ),
                
            ]
        )
