# -*- coding: utf-8 -*-
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def send_email(server, port, ssl, user, password, to, subject, body):
    """Send html or text email.

    Args:
        server (str): SMTP server.
        port (int): Port.
        ssl (bool): True if use ssl and False if use tls.
        user (str): User address.
        password (str): Password to authenticate.
        to (str/list): Recipients.
        subject (str): Subject.
        body (str): Message, can be string or html.

    """
    if ssl:
        smtp_server = smtplib.SMTP_SSL(server, port)
    else:
        smtp_server = smtplib.SMTP(server, port)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
    smtp_server.login(user, password)
    types = 'plain'
    regex_html = '(?i)<\/?\w+((\s+\w+(\s*=\s*(?:".*?"|\'.*?\'|[^\'">\s]+))?)+\s*|\s*)\/?>'
    if re.match(regex_html, body):
        types = 'html'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(body, types, 'utf-8'))
    smtp_server.sendmail(user, to, msg.as_string())
    smtp_server.close()
