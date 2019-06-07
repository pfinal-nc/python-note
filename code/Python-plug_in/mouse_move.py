#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import autopy
import random
import time

for i in range(1000):
    # x = random.randint(1,1000)
    # y = random.randint(1,1000)
    autopy.mouse.move(i*100, i*100)
    # time.sleep(1)
    