from smtplib import SMTP
from email.message import EmailMessage
from config import settings

message = EmailMessage()

message['Subject'] = 'Este es el asunto'
message['From'] = 'jacalvached17m@itp.edu.co'
message['To'] = 'jeison130@yopmail.com'
message.set_content("""
                    <h1>Prueba</h1>
                    <br>
                    <a href="http://localhost:5000">Ingresa a la app</a>
                    """)

username = settings.SMPT_USERNAME
password = settings.SMPT_PASSWORD

server = SMTP(settings.SMPT_HOSTNAME)
server.starttls()
server.login(username, password)
server.send_message(message)

server.quit()