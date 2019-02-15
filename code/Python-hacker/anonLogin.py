#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'what')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
    except Exception:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.')
def main():
    while True:
        hostname = input("Please enter the hostname: ")
        anonLogin(hostname)
        print

if __name__ == '__main__':
    main()