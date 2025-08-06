import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    #password = os.getenv("PASSWORD") #AIXÒ NO EM FUNCIONA
    password = "ljrcoewoimvcbvqb"
    username = "andreusdinversions@gmail.com"
    receiver = "andreusolad@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

#ljrcoewoimvcbvqb
