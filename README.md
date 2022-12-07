# Telegram bot по поиску объявлений на Авито и Циан (в разрабокте)

Бот при помощи selenium парсит авито по ссылке[https://www.avito.ru/samara/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?f=ASgBAQECAkSSA8gQ8AeQUgFAzAg0kFmOWYxZAUXGmgwVeyJmcm9tIjowLCJ0byI6MjAwMDB9&i=1&s=104&user=1] и достает новые объявления.

В ссылке заложен фильтр:
Город: Самара
Комнаты: Студия, 1, 2
Цена: до 20.000 р

Для запуска кода:
* Инициализируйте репозиторий
```
$ git clone https://github.com/k0dim/rent_bot_tg.git
```
* Активируйте виртуальное окружение
```
$ source pyrent/bin/activate
```
* Установите модули
```
$ pip3 install -r requirements.txt
```
* Запустите код, если запускаете через cmd:
```
$ python3 main.py
```