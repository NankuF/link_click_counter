# Сокращатель ссылок и счетчик переходов по ссылке.

Скрипт позволяет сократить ссылку и посчитать, сколько раз был переход по короткой ссылке.

## Окружение
### Подготовка Linux:<br>

Скачать git:
```bash
sudo apt-get install git
```
Сделать fork репозитория:
```bash
git clone https://github.com/NankuF/link_click_counter.git
```
Перейти в директорию со скриптом:
```bash
cd ~ && cd link_click_counter/
```
Создать виртуальное окружение:
```bash
python -m venv venv
```
Активировать виртуальное окружение:
```bash
. ./venv/bin/activate
```
Установить зависимости:
```bash
pip install -r requirements.txt 
```

### Переменные окружения <br>
Зарегистрироваться на bit.ly:
```
https://bitly.com/
```
Получить токен:
```
https://app.bitly.com/settings/api/
```
Сохранить токен в .env:
```bash
echo 'BITLY_ACCESS_TOKEN=ваш_токен' > .env
```
Файл .env должен быть рядом с main.py
```
main.py
.env
```

## Запуск: <br>

Ввести в консоли код:
```bash
python main.py
```