import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
password = os.environ['MAIL_PASSWORD'] # needs to be a heroku config variable

# Create a secure SSL context
context = ssl.create_default_context()

balgoEmailAddress = "balgo.trader@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(balgoEmailAddress, password)

    sender_email = balgoEmailAddress
    receiver_email = os.environ['MAIL_RECEIVER']

    message = MIMEMultipart("alternative")
    message["Subject"] = "bAlgo Daily Update"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a> 
           has many great tutorials.
        </p>
      </body>
    </html>
    """

    # Turn this into html MIMEText objects
    part = MIMEText(html, "html")

    # Add HTML part to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)

    server.sendmail(sender_email, receiver_email, message.as_string())