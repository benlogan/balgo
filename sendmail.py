import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
password = os.environ['MAIL_PASSWORD'] # needs to be a heroku config variable

# Create a secure SSL context
context = ssl.create_default_context()

balgoEmailAddress = "balgo.trader@gmail.com"

def sendMail(traded):
    print('Starting Email Summary')
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(balgoEmailAddress, password)

        sender_email = balgoEmailAddress
        receiver_email = os.environ['MAIL_RECEIVER']

        message = MIMEMultipart("alternative")
        message["Subject"] = "bAlgo Execution Summary"
        message["From"] = sender_email
        message["To"] = receiver_email

        executionSummary = ""
        for trade in traded:
            executionSummary += "<p>" + trade + ' ' + str(traded[trade]) + ' units' + "</p>"

        html = """\
        <html>
          <body>
            <p>Here is your daily bAlgo Execution Summary</p>
            """ + executionSummary + """
          </body>
        </html>
        """

        # Turn this into html MIMEText objects
        part = MIMEText(html, "html")

        # Add HTML part to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part)

        server.sendmail(sender_email, receiver_email, message.as_string())
    print('Ending Email Summary')

# testing...
#sendMail()