#!/usr/bin/env python
# --*--coding: utf-8 --*--
from manage import my_celrey


@my_celrey.task
def send_email(data):
    print('come in task================')
    return 'success'