# coding=utf-8
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

class Leviathan(HackingTool):
    TITLE = "Leviathan - Wide Range Mass Audit Toolkit"
    DESCRIPTION = "Leviathan is a mass audit toolkit which has wide range " \
                  "service discovery,\nbrute force, SQL injection detection " \
                  "and running custom exploit capabilities. \n " \
                  "[*] It Requires API Keys \n " \
                  "More Usage [!] https://github.com/utkusen/leviathan/wiki"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "git clone https://github.com/leviathan-framework/leviathan.git",
        "cd leviathan;sudo pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd leviathan;python leviathan.py"]
    PROJECT_URL = "https://github.com/leviathan-framework/leviathan"


class SqlInjectionTools(HackingToolsCollection):
    TITLE = "SQL Injection Tools"
    TOOLS = [
        Sqlmap(),
        Leviathan(),
        NoSqlMap()
    ]
