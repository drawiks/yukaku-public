
from pathlib import Path
import json

class Schedule:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.schedule: dict[str, dict[str, str]] = {}

    async def load(self):
        if self.file_path.exists():
            self.schedule = json.loads(self.file_path.read_text(encoding="utf-8"))
        else:
            await self.save()

    async def save(self):
        self.file_path.write_text(json.dumps(self.schedule, ensure_ascii=False, indent=2), encoding="utf-8")

    async def update(self, day: str, time: str, lesson_name: str):
        self.schedule.setdefault(day, {})[time] = lesson_name
        await self.save()
        
    async def remove(self, day: str, time: str):
        if day in self.schedule and time in self.schedule[day]:
            del self.schedule[day][time]
            if not self.schedule[day]:
                del self.schedule[day]
            await self.save()

    def get_lesson_name(self, day: str, time: str) -> str | None:
        return self.schedule.get(day, {}).get(time)
    
    def all(self) -> dict[str, dict[str, str]]:
        return self.schedule
