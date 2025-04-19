
import flet as ft
import asyncio

from gui.engine import Engine

from core.service.loop import Loop

from core.utils.logger import LogManager

from config import EMAIL, PASSWORD, SESSION_FILE, LOG_PATH

class App:
    def __init__(self):
        self.log = LogManager(LOG_PATH).logger
        self.loop = Loop()
        
        self.tasks = []
        
    async def start(self):
        loop_task = asyncio.create_task(self.loop.main_loop())
        engine_task = asyncio.create_task(ft.app_async(target=Engine, assets_dir="gui/assets"))
        
        self.tasks.append(loop_task)
        self.tasks.append(engine_task)
        
        await asyncio.gather(*self.tasks)

if __name__ == "__main__":
    app = App()
    asyncio.run(app.start())
