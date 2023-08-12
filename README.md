# Скрипт резервного копирования БД 
Скрипт для резервного копирования базы данных postgres в Docker контейнере и отправки backup в облако YandexDisk.

Скрипт выполняется по расписанию. Сам Бэкап и отправка на облако.

### Установка и запуск
1. Скачать репо `git clone https://github.com/Jagernau/backup_bd`
2. Создать песочницу python в папке `python3.10 -m virtualenv env`
3. Активировать песочницу `source env/bin/activate`
4. Установить зависимости `pip install -r requirements.txt`
5. создать .env в котором нужно прописать токен yandex облака `echo "DISK_TOKEN=" > .env`

