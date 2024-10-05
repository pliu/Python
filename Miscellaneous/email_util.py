import smtplib
from email.mime.multipart import MIMEMultipart


class EmailClient(object):
    def __init__(self, user, password, host, port):
        '''
        Initializes an EmailClient
        :param user: The email account from which to send the email (e.g.: xyz@gmail.com)
        :param password: The password for the email account
        :param host: The email provider's SMTP endpoint
        :param port: The email provider's SMTP port
        '''
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        try:
            self.server = smtplib.SMTP(self.host, self.port)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.user, self.password)
        except:
            raise RuntimeError

    def send_message(self, to, subject, message):
        '''
        Sends the given message
        :param to: The recipient's email
        :param subject: The subject line
        :param message: The message being sent as a MIMEText object
        :return:
        '''
        try:
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = self.user
            msg['To'] = to
            msg.attach(message)
            self.server.sendmail(self.user, [to], msg.as_string())
        except:
            print 'Failed to send mail to ' + to

    def __del__(self):
        self.server.close()


class GmailClient(EmailClient):
    def __init__(self, user, password):
        super(GmailClient, self).__init__(user, password, 'smtp.gmail.com', 587)
