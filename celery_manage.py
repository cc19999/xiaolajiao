#!/usr/bin/env python
# --*--coding: utf-8 --*--
from celery import Celery
from app01 import celeryconfig

celery_app = Celery('celery_worker', backend=celeryconfig.result_backend, broker=celeryconfig.broker_url, include=[
    "app01.sms.task01",
    "app01.sms.task02"
])
celery_app.config_from_object(celeryconfig)