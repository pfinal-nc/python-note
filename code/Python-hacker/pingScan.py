# -*- coding:utf-8 -*-
from subprocess import Popen, PIPE

for ip in range(100, 255):
    ipAddress = '192.168.1.'+str(ip)
    print("Scanning %s " % (ipAddress))
    subprocess = Popen(['C:/Windows/System32/ping', '-c 1', ipAddress],
                       stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = subprocess.communicate(input=None)
    print(stdout)
    # if "bytes from ".encode("utf-8") in stdout:
    #     print("The Ip Address %s has responded with a ECHO_REPLY!" %
    #           (stdout.split()[1]))
    #     with open("ips.txt", "a") as myfile:
    #         myfile.write(stdout.split()[1]+'\n')
