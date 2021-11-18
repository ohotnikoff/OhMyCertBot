# OhMyCertBot

Простой телеграм-бот раздающий именные сертификаты, разработанный в учебных целях.
Проект для [Русской школы программирования](https://codeschool.it-edu.com)

## Что под капотом?

3 библиотеки: [PyPDF2](https://pypi.org/project/PyPDF2/), [reportlab](https://pypi.org/project/reportlab/) - для работы с pdf и [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) - для работы с api Telegram

Посмотрим на файлы
-------------------

      bot.py              для запуска бота
      pdf2cert.py         для создания сертификата
      requirements.txt    необходимые библиотеки
      config.py           конфигурация (создаете по примеру config.example.py)
      DejaVuSerif.ttf     файл шрифта поддерживающий кириллицу


## Установка

- Создаете бота в telegram с помощью @BotFather
- Создаете конфигурационный файл config.py с указанием токена
- Не забываем установить зависимости `pip install -r requirements.txt`
- Добавляете в проект шаблон pdf (см. название файла в настройках, можете переименовать)


**PS:**
Бот работает с учебным шаблоном pdf, который в репозиторий не загружен.
Для своего шаблона поэкспериментируйте с pdf2cert.py
