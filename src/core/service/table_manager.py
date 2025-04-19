
from pathlib import Path

from .lesson import Lesson
from .schedule import Schedule

class TableManager:
    def __init__(self):
        self.lesson = Lesson(Path("src/data/lessons.json"))
        self.schedule = Schedule(Path("src/data/schedule.json"))

    async def init(self):
        await self.lesson.load()
        await self.schedule.load()

    async def add_lesson(self, name: str, conference_id: str):
        await self.lesson.add(name, conference_id)

    async def remove_lesson(self, name: str):
        await self.lesson.remove(name)
        
    def get_all_lessons(self) -> dict[str, str]:
        return self.lesson.all()

    async def set_schedule(self, day: str, time: str, lesson_name: str):
        await self.schedule.update(day, time, lesson_name)
        
    async def remove_from_schedule(self, day: str, time: str):
        await self.schedule.remove(day, time)

    def get_full_schedule(self) -> dict[str, dict[str, str]]:
        return self.schedule.all()

    def get_id(self, day: str, time: str) -> str | None:
        lesson_name = self.schedule.get_lesson_name(day, time)
        if lesson_name:
            return self.lesson.get_id(lesson_name)
        return None
    
    def get_lesson_name(self, day: str, time: str):
        return self.schedule.get_lesson_name(day, time)