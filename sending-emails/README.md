>[назад](../README.md)

## Урок 3. Рассылаем имейлы

### Описание
Код к 3 уроку курса [Знакомство с Python. 3 урок](https://dvmn.org/modules/meeting-python/lesson/friend-invitation/)

### Установка
1. Склонировать репозиторий
2. Создать виртуальное окружение. Версия Python >= 3.7. В проекте использовался Python 3.9.1. Файл .python-version, если устанавливаете через pyenv. Активировать виртуальное окружение
3. Перейти в католог с кодом урока 
```shell script
cd sending-emails
```
4. Установить все зависимости: 
```shell script
pip install -r req.txt
```

### Использование
1. Чтобы использовать скрипт, cоздайте файл .env и добавьте соответствующие переменные: 
```.env
SITE_LINK='put_here_site_link'
SENDER_NAME='put_here_your_name'
SENDER_EMAIL='put_here_your_mailbox_email'
PASSWORD='put_here_your_mailbox_password'
RECIPIENT_NAME='put_here_recipient_name'
RECIPIENT_EMAIL='put_here_recipient_name'
```

2. Запустить скрипт: 
```python
python main.py
```
