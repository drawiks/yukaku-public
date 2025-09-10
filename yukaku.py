
from src.app import App

if __name__ == "__main__":
    from asyncio import run
    
    app = App()
    run(app.start())