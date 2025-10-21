
<div align="center">
    <h1>⏰ yukaku</h1>
    <img height="20" alt="Python 3.9+" src="https://img.shields.io/badge/python-3.9+-blue">
    <img height="20" alt="License Apache 2.0" src="https://img.shields.io/badge/license-MIT-green">
    <img height="20" alt="Status" src="https://img.shields.io/badge/status-pet--project-orange">
    <p><strong>yukaku</strong> — это программа для автоматического входа в конференции <strong>Google Meet</strong></p>
    <blockquote>(─‿‿─)</blockquote>
</div>

---

## **📂 структура проекта**

```bash
yukaku-public/
│
├── scr/
│   ├── data/
│   │   ├── __init__.py
│   │   └── schedule.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── speaker.py
│   │   └── logger.py
│   ├── app.py
│   └── config.py
│
├── yukaku.py # --- entrypoint ---
│
├── .env # --- example ---
│
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## **🛠️ функциональность**
- автоматический вход в Google Meet конференции при помощи playwright.
- простая настройка расписания [src/data/schedule.py](src/data/schedule.py).
- озвучка названия урока/пары/конференции перед входом для напоминания, настраивается в [src/utils/speaker](src/utils/speaker.py).
- поддержка сохранения сессий для повторного использования.
- простое логирование при помощи [loguru](https://pypi.org/project/loguru) см. файл [src/utils/logger.py](src/utils/logger.py) для подробностей.
- [reID.py](reID.py) утилита для быстрого получения id конференции из ссылки (необязательно).

## **🔊 голосовые модели для спикера**

yukaku-public использует библиотеку [edge-tts](https://github.com/rany2/edge-tts) для озвучки текста. вот список доступных голосовых моделей:
[list of voices available in Edge TTS.txt](https://gist.github.com/BettyJJ/17cbaa1de96235a7f5773b8690a20462)

## **🌐 установка**

``` bash
git clone https://github.com/drawiks/yukaku-public.git
python -m venv venv
pip install -r requirements.txt
```

## **📝 создай расписание по шаблону: [src/data/schedule.py](src/data/schedule.py)**

``` bash
lessons = {
    "meet1":"<ваш ID конференции>",
    "meet2":"<ваш ID конференции>",
    "meet3":"<ваш ID конференции>",
}

#Monday, Tuesday...
schedule = {
    "Friday":{
            "09:55":lessons["meet1"],
            "12:00":lessons["meet3"],
            "13:05":lessons["meet1"],
            "05:22":lessons["meet2"],
        },
    #...
}
```

## **📝 создай .env по шаблону:**

``` bash
EMAIL="ваша_почта"
PASSWORD="ваш_пароль"
SESSION_FILE="путь/session.json"
LOG_PATH="logs/app.log"
```

## **📭 установи chromium для playwright (либо сам укажи нужный браузер в коде):**

``` bash
- playwright install
```
