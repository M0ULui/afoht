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
    INSTALL_COMMANDS = [
        "git clone https://github.com/codingo/NoSQLMap.git",
        "sudo chmod -R 755 NoSQLMap;cd NoSQLMap;python setup.py install"
    ]
    RUN_COMMANDS = ["python NoSQLMap"]
    PROJECT_URL = "https://github.com/codingo/NoSQLMap"



class SqlInjectionTools(HackingToolsCollection):
    TITLE = "SQL Injection Tools"
    TOOLS = [
        Sqlmap(),
        NoSqlMap()
    ]
