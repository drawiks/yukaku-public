
import flet as ft

from .routes.home_route import HomeRoute
from .routes.schedule_route import ScheduleRoute
from .routes.not_found import NotFoundRoute

class Engine:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.fonts = {
            "jersey": "/fonts/Jersey20-Regular.ttf",
            "plex bold": "/fonts/IBMPlexSans-Bold.ttf",
            "plex medium": "/fonts/IBMPlexSans-Medium.ttf"
        }
        
        self.routes = {
            "/": HomeRoute(),
            "/schedule": ScheduleRoute(),
        }
        self.not_found_route = NotFoundRoute()
        
        self.page.title = "Dosh-desktop"
        self.page.on_route_change = lambda e: self.route_change(self.page.route)
        self.page.on_view_pop = self.view_pop
        self.page.go("/")
        
        self.navigation_rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.EDIT_CALENDAR, label="Shedule"),
            ft.NavigationRailDestination(icon=ft.Icons.STICKY_NOTE_2, label="Lessons"),
            ft.NavigationRailDestination(icon=ft.Icons.SPEAKER, label="Speaker"),
        ],
        selected_index=0,
        on_change=self.on_rail_change,
    )

    def on_rail_change(self, e):
        routes = ["/", "/schedule", "/lessons", "/speaker"]
        self.page.go(routes[e.control.selected_index])
    
    def route_change(self, route):
        self.page.views.clear()
        if route in self.routes:
            self.page.views.append(self.routes[route].build(self.navigation_rail))
        else:
            self.page.views.append(self.not_found_route.build())
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
