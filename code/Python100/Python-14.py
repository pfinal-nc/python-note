# -*- coding: UTF-8 -*-
import datetime
import time

print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))

print(datetime.date.today() + datetime.timedelta(days=1))
print(datetime.date.today().replace(year=1990))

print(time.time())
print(time.localtime())
