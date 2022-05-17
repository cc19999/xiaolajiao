#!/usr/bin/env python
# --*--coding: utf-8 --*--
from apscheduler.schedulers.blocking import BlockingScheduler
import time

sched = BlockingScheduler()

@sched.scheduled_job('interval',seconds=5)

def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))



# sched.add_job(my_job,'interval',seconds=5)
#
# sched.start()

sched.start()