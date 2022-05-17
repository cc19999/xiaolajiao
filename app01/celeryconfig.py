#!/usr/bin/env python
# --*--coding: utf-8 --*--


broker_url = 'redis://127.0.0.1:6379/1'
result_backend = 'redis://127.0.0.1:6379/2'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'  # 时区
enable_utc = True