import os
import sys
import re
import math
import random
import zlib
from datetime import date


print(os.getcwd())
# print(dir(os))
sys.stderr.write('Warning, log file not found starting a new one\n')
print(sys.argv)

x = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

print(x)

print('tea for too'.replace('too', 'two'))

print(math.cos(math.pi / 4))

print(math.log(1024, 2))

print(random.choice(['apple', 'pear', 'banana']))

now = date.today()

print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

s = b'witch which has which witches wrist watch'

print(len(s))
t = zlib.compress(s)
zlib.decompress(t)

print(zlib.crc32(s))