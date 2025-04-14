## yukaku-public

yukaku-public — это программа для автоматического входа в конференции Google Meet с использованием playwright. она позволяет автоматически подключаться к урокам или встречам по заданному расписанию, озвучивая название урока/пары/конференции.

## функциональность

- автоматический вход в Google Meet конференции при помощи playwright.
- простая настройка расписания.
- озвучка названия урока/пары/конференции перед входом для напоминания, настраивается в src/data/shedule.
- поддержка сохранения сессий для повторного использования.

## голосовые модели для спикера

yukaku-public использует библиотеку [edge-tts](https://github.com/rany2/edge-tts) для озвучивания текста. вот список доступных голосовых моделей:
[list of voices available in Edge TTS.txt](https://gist.github.com/BettyJJ/17cbaa1de96235a7f5773b8690a20462)

## установка

1. клонируй репозиторий:
- git clone https://github.com/drawiks/yukaku-public.git

2. создай виртуальную среду
- python -m venv myenv

3. установи зависимости:
- pip install -r requirements.txt

4. создай расписание по шаблону:
- [src/data/shedule.py](src/data/shedule.py)

5. создай файл `.env` и добавь свои данные (например, логин и пароль для Google):
- EMAIL=ваша_почта, PASSWORD=ваш_пароль, SESSION_FILE=путь/session.json

## лицензия

этот проект лицензирован под MIT лицензией. см. файл [LICENSE](LICENSE) для подробностей.
