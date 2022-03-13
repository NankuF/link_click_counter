# Сокращатель ссылок и счетчик переходов по ссылке.

Скрипт позволяет сократить ссылку и посчитать, сколько раз был переход по короткой ссылке.

**Подготовка Linux:**<br>

Скачать git:
```
sudo apt-get install git
```
Сделать fork репозитория:
```
git clone https://github.com/NankuF/link_click_counter.git
```
Перейти в директорию со скриптом:
```
cd ~ && cd link_click_counter/
```
Создать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
. ./venv/bin/activate
```
Установить зависимости:
```
pip install -r requirements.txt 
```
**Запуск:** <br>
Зарегистрироваться на bit.ly:
```
https://bitly.com/
```
Получить токен:
```
https://app.bitly.com/settings/api/
```
Сохранить токен в .env:
```
echo 'ACCESS_TOKEN=ваш_токен' > .env
```
Ввести в консоли код:
```
python main.py
```