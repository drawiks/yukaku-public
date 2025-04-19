
from playwright.async_api import async_playwright
import asyncio, json, os

from .logger import LogManager

from config import EMAIL, PASSWORD, SESSION_FILE, LOG_PATH

class PlayWright:
    def __init__(self):
        self.log = LogManager(LOG_PATH).logger
        
    async def join(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context()

            await self.load_session(context)
            
            page = await context.new_page()
            
            await page.goto("https://accounts.google.com")
            
            if not await page.is_visible("input[type='email']"):
                self.log.info("cессия активна, пропускаем вход.")
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

            """ВРЕМЯ ПРИБЫВАНИЯ НА КОНФЕРЕНЦИИ"""
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