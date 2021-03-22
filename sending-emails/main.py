import smtplib
from getpass import getpass


template_letter = """
From: {recipient_email}
To: {sender_email}
Subject: Приглашение на dvmn.org
Content-Type: text/plain; charset="UTF-8";

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

site_link = 'dvmn.org'
recipient_name = input('Введите Ваше имя: ')
recipient_email = input('Введите Ваш email: ')
password = getpass('Введите пароль от Вашего почтового ящика: ')

sender_name = input('Введите имя получателя: ')
sender_email = input('Введите email поулчателя: ')


template_letter = template_letter.replace('%website%', site_link)
template_letter = template_letter.replace('%friend_name%', sender_name)
template_letter = template_letter.replace('%my_name%', recipient_name)
template_letter = template_letter.format(recipient_email=recipient_email, sender_email=sender_email)

message = template_letter.encode('UTF-8')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(recipient_email, password)

server.sendmail(recipient_email, sender_email, message)
server.quit()
print('Ваше письмо отправлено')

