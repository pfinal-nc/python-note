import os

g = input('目标IP:')
nmap1=os.system('nmap -vv -Pn -sC -sS -T4 -p {}'.format(g))
print(nmap1)