import smtplib
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


template_letter = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""


site_link = os.environ.get("SITE_LINK")

sender_name = os.environ.get("SENDER_NAME")
sender_email = os.environ.get("SENDER_EMAIL")
password = os.environ.get("PASSWORD")

recipient_name = os.environ.get("RECIPIENT_NAME")
recipient_email = os.environ.get("RECIPIENT_EMAIL")

letter = template_letter\
    .replace('%website%', site_link)\
    .replace('%friend_name%', recipient_name)\
    .replace('%my_name%', sender_name)


message = f"""
From: {sender_email}
To: {recipient_email}
Subject: Приглашение на dvmn.org
Content-Type: text/plain; charset="UTF-8";
{letter}
"""

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(sender_email, password)

server.sendmail(sender_email, recipient_email, message.encode('UTF-8'))
server.quit()

