
from datetime import datetime
from playwright.async_api import async_playwright
import asyncio
import json
import os

from utils.speaker import *
from data.shedule import *

from config import EMAIL, PASSWORD, SESSION_FILE

class App:
    def __init__(self):
        pass
    
    async def main_loop(self):
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_day = now.strftime("%A")

            lesson_id = shedule.get(current_day, {}).get(current_time)

            print(current_time)
            
            if lesson_id:
                lesson_name = next((name for name, id_ in lessons.items() if id_ == lesson_id), "неизвестный урок")
                url = f"https://meet.google.com/{lesson_id}?pli=1&authuser=2"

                print(f"({current_time} {current_day}) — ({lesson_name} ID: {lesson_id})")
                print(f"открываю meet: ({url})")

                await speak(lesson_name)
                task = asyncio.create_task(self.join_google_meet(url))
                await task
                
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(15)
    
    async def join_google_meet(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context()

            await self.load_session(context)
            
            page = await context.new_page()
            
            await page.goto("https://accounts.google.com")
            
            if not await page.is_visible("input[type='email']"):
                print("cессия активна, пропускаем вход.")
            else:
                """ВХОДИМ В АККАУНТ"""
                await page.fill("input[type='email']", EMAIL)
                await page.click("button:has-text('Далее')")
                await page.wait_for_timeout(2000)

                await page.fill("input[type='password']", PASSWORD)
                await page.click("button:has-text('Далее')")
                await page.wait_for_timeout(5000)

            """ВХОДИМ НА КОНФЕРЕНЦИЮ"""
            await page.goto(url)
            await page.wait_for_selector("button:has-text('Не надавати доступ до мікрофона й камери')")
            await page.click("button:has-text('Не надавати доступ до мікрофона й камери')")
            await page.wait_for_timeout(2000)
            await page.wait_for_selector("button:has-text('Приєднатися зараз')")
            await page.click("button:has-text('Приєднатися зараз')")

            await asyncio.sleep(1500)

            await self.save_session(context)
            await browser.close()
    
    async def save_session(self, context):
        cookies = await context.cookies()
        with open(SESSION_FILE, 'w') as f:
            json.dump(cookies, f)

    async def load_session(self, context):
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, 'r') as f:
                cookies = json.load(f)
                await context.add_cookies(cookies)
        
    async def start(self):
        task = asyncio.create_task(self.main_loop())
        await task

if __name__ == "__main__":
    app = App()
    asyncio.run(app.start())