# Счетчик переходов по ссылке.

Скрипт позволяет посчитать, сколько раз был переход по ссылке

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

Ввести в консоли код:
```
python main.py
```