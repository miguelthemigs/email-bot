
import os
import smtplib
import time
from email.message import EmailMessage

email_address = os.environ.get('DB_USER')
email_password = os.environ.get('DB_PASS')

msg = EmailMessage()
msg['Subject'] = 'BOM DIA'
msg['From'] = email_address
msg['To'] = 'email@gmail.com'
msg.set_content('bom dia linda')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)

    smtp.send_message(msg)

    message_loop = 0

    for message_loop in range(1, 100):
        message_loop = message_loop + 1
        smtp.send_message(msg)
        time.sleep(1)

        if message_loop == 100:
            break











