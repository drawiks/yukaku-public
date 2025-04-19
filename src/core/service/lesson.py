
from pathlib import Path
import json

class Lesson:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.lessons: dict[str, str] = {}

    async def load(self):
        if self.file_path.exists():
            self.lessons = json.loads(self.file_path.read_text(encoding="utf-8"))
        else:
            await self.save()

    async def save(self):
        self.file_path.write_text(json.dumps(self.lessons, ensure_ascii=False, indent=2), encoding="utf-8")

    async def add(self, name: str, conference_id: str):
        self.lessons[name] = conference_id
        await self.save()

    async def remove(self, name: str):
        if name in self.lessons:
            del self.lessons[name]
            await self.save()

    def get_id(self, name: str) -> str | None:
        return self.lessons.get(name)
    
    def all(self) -> dict[str, str]:
        return self.lessons