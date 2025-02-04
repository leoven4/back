from twilio.rest import Client
from constants_notifier import constants
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path    # similar to os.path

def notify_via_email(email_to, title):

    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = ''
    email['to'] = email_to
    email['subject'] = title

    # email.set_content(html.substitute({'name' : 'TinTin'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(constants['email'],constants['pass'])
        smtp.send_message(email)
        print('email sent')

def notify():
    client = Client(constants['account_sid'], constants['auth_token'])

    message = client.messages.create(
    from_='',
    body='Il portale permette la cessazione dei crediti',
    to=''
    )
    print('MESSAGE SENT')
    print(message.sid)


def notify_error():
    client = Client(constants['account_sid'], constants['auth_token'])

    message = client.messages.create(
    from_='',
    body='Error in Python code',
    to=''
    )
    print('MESSAGE SENT')
    print(message.sid)
