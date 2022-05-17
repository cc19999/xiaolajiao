#!/usr/bin/env python
# --*--coding: utf-8 --*--

from celery_manage import celery_app
from flask_mail import Mail,Message
from flask import current_app

import time

@celery_app.task
def send_email(data):
    mail = Mail(current_app)
    addr = data.get('addr')
    title = data.get('title')
    content = data.get('content')
    msg = Message(title, recipients=[addr], body=content)
    mail.send(msg)
    print('ok')
