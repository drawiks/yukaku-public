
from datetime import datetime
import asyncio

from .table_manager import TableManager

from core.utils.playwright import PlayWright
from core.utils.speaker import Speaker

class Loop:
    def __init__(self):
        self.table_manager = TableManager()
        self.speaker = Speaker()
        self.playwright = PlayWright()
        
    async def main_loop(self):
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_day = now.strftime("%A")

            lesson_id = self.table_manager.get_id(current_day, current_time)
            
            if lesson_id:
                lesson_name = self.table_manager.get_lesson_name(current_day, current_time)
                url = f"https://meet.google.com/{lesson_id}"

                self.log.info(f"({current_day} {current_time}) — {lesson_name} ID: {lesson_id}")

                await self.speaker.speak(lesson_name)
                
                join = asyncio.create_task(self.playwright.join(url))
                await join
                
            else:
                await asyncio.sleep(15)