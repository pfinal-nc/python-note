# -*- coding:utf-8 -*-
import os
import time
print('_!_!_!_!_!_!_!_!_!_!_!_!_!_')
print('!_!_!_!_!_!_!_!_!_!_!_!_!_!')
print('   ！——！——！——！')
print('!！——！——！')
print('1.进行一系列脚本扫描')
print('2.进行DDOS')
print('3.使用nmap 利用已知的漏洞入侵系统')
print('4.使用nmap 探测目标机是否感染了病毒、开启了后门等信息')
print('5.使用nmap 对系统进行安全检查')
print('6.更新nmap脚本数据库')
print('7.使用nmap检测MS-17-010')
print('8.生成metasploit自动攻击模块要用的rc')
print('9.安装nmap高级漏洞扫描模块')
print('10.调用高级漏洞扫描模块')
print('11.自己写的web信息收集器')
print('12.使用metasploit自动攻击模块')
gs = input('请输入你要执行的步骤:')


def namp():
    try:
        g = input("目标IP:")
        print('[+]一般枚举')
        nmap1 = os.system('nmap -vv -Pn -sC -sS -T4 -p {}'.format(g))
        print(nmap1)
        print('====================================================')
        nmap2 = os.system('nmap -v -sS -A -T4 {}'.format(g))
        print(nmap2)
        print('====================================================')
        print('[*]Verbose，SYN Stealth，版本信息和针对服务的脚本。')
        nmap3 = os.system(
            'nmap -v -p 445 --script=smb-check-vulns --script-args=unsafe=1 {}'.format(g))
        print(nmap3)
        print('====================================================')
        print('[*]进行信息挖掘')
        nmap4 = os.system('nmap -sS --script discovery {}'.format(g))
        print(nmap4)
    except:
        print('[-]出现了错误')
        exit()

if gs == "1":
    namp()
