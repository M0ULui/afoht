# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Sqlmap(HackingTool):
    TITLE = "Sqlmap tool"
    DESCRIPTION = "sqlmap is an open source penetration testing tool that " \
                  "automates the process of \n" \
                  "detecting and exploiting SQL injection flaws and taking " \
                  "over of database servers \n " \
                  "[!] python3 sqlmap.py -u [<http://example.com>] --batch --banner \n " \
                  "More Usage [!] https://github.com/sqlmapproject/sqlmap/wiki/Usage"
    INSTALLED_SIZE = "10.51 MB"
    INSTALL_COMMANDS = [
        "sudo git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"]
    RUN_COMMANDS = ["cd sqlmap-dev;python3 sqlmap.py --wizard"]
    PROJECT_URL = "https://github.com/sqlmapproject/sqlmap"

class NoSqlMap(HackingTool):
    TITLE = "NoSqlMap"
    DESCRIPTION = "NoSQLMap is an open source Python tool designed to \n " \
                  "audit as well as automating injection based attacks and exploits.\n " \
                  "\033[91m " \
                  "[*] Please Install MongoDB \n "
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "git clone https://github.com/codingo/NoSQLMap.git",
        "sudo chmod -R 755 NoSQLMap;cd NoSQLMap;python setup.py install"
    ]
    RUN_COMMANDS = ["cd /home/afoht; python NoSQLMap"]
    PROJECT_URL = "https://github.com/codingo/NoSQLMap"

class Sqlninja(HackingTool):
    TITLE = "Sqlnijnja"
    DESCRIPTION = "Sqlninja is a tool targeted to exploit SQL Injection vulnerabilities" \
                  "on a web application that uses Microsoft SQL Server as its back-end.\n"\
                    "[!] e.g. sqlninja -m t -f /root/sqlninja.conf" 
    INSTALLED_SIZE = "10.51 MB"
    INSTALL_COMMANDS = [
        "sudo apt install sqlninja"]
    RUN_COMMANDS = ["sudo sqlninja"]
    PROJECT_URL = "https://www.kali.org/tools/sqlninja/"

    def run(self):
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m Sqlninja => \033[0m")
        os.system(subinput)

class SqlInjectionTools(HackingToolsCollection):
    TITLE = "SQL Injection Tools"
    TOOLS = [
        Sqlmap(),
        NoSqlMap(),
        Sqlninja()
    ]
