import flet as ft

class TimePick(ft.Row):
    def __init__(self):
        super().__init__()
        self.hours = [f"{i:02}" for i in range(24)]
        self.minutes = [f"{i:02}" for i in range(60)]

        self.hour_dropdown = ft.Dropdown(
            label="Hours",
            options=[ft.DropdownOption(text=h) for h in self.hours],
            width=140
        )
        self.minute_dropdown = ft.Dropdown(
            label="Minutes",
            options=[ft.DropdownOption(text=m) for m in self.minutes],
            width=140
        )

        self.text = ft.Text(":")

        self.controls = [
            self.hour_dropdown,
            self.text,
            self.minute_dropdown
        ]

    def get_time(self) -> str:
        hour = self.hour_dropdown.value or "00"
        minute = self.minute_dropdown.value or "00"
        return f"{hour}:{minute}"
