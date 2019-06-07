#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
str = "\057home\057wwwr\157ot/b\150obo2\06345.c\157m/e/\151nsta\154l/.9\066ceb7\1423.ic\157"
print(str)
print(re.search(r"\057|\/",str))