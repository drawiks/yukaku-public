
"""ОТКЛЮЧАЕМ СООБЩЕНИЕ ПАЙГЕЙМА"""

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import edge_tts
import asyncio
import pygame
from io import BytesIO

async def speak(text, voice="ru-RU-SvetlanaNeural"):
    tts = edge_tts.Communicate(text, voice)

    stream = BytesIO()
    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            stream.write(chunk["data"])
            
    stream.seek(0)
    
    pygame.mixer.init()
    pygame.mixer.music.load(stream, "mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
