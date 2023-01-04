# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class Sublist3r(HackingTool):
    TITLE = "Sublist3r - SubDomain Finder"
    DESCRIPTION = "Sublist3r is a python tool designed to enumerate " \
                  "subdomains of websites using OSINT \n " \
                  "Usage:\n\t" \
                  "[1] python3 sublist3r.py -d example.com \n" \
                  "[2] python3 sublist3r.py -d example.com -p 80,443"
    INSTALLED_SIZE = "10.51 MB"
    INSTALL_COMMANDS = [
        "sudo pip3 install requests argparse dnspython",
        "sudo git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && sudo pip3 install -r requirements.txt"
    ]
    #RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"

    def run(self):
        os.system("cd Sublist3r && python3 sublist3r.py -h")
        #os.system("echo '\033[1;32m---------------------------------------\033[m'")
        subinput = input("\033[33;5m Sublist3r >>\033[0m")
        os.system(["cd Sublist3r &&",subinput])


class CheckURL(HackingTool):
    TITLE = "CheckURL"
    DESCRIPTION = "Detect evil urls that uses IDN Homograph Attack.\n\t" \
                  "[!] python3 checkURL.py --url google.com"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/checkURL.git"]
    #RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"

    def run(self):
        os.system("cd checkURL && python3 checkURL.py --help")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m Enter Url >>\033[0m")
        os.system(["cd checkURL && sudo python3 checkURL.py --url", subinput])


class Dirb(HackingTool):
    TITLE = "Dirb"
    DESCRIPTION = "DIRB is a Web Content Scanner. It looks for existing " \
                  "(and/or hidden) Web Objects.\n" \
                  "It basically works by launching a dictionary based " \
                  "attack against \n a web server and analyzing the response."
    INSTALLED_SIZE = "1.43 MB"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo bash configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        os.system("sudo man dirb")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        uinput = input("\033[33;5m Enter Url >>  \033[0m")
        subprocess.run(["sudo", "dirb", uinput])


class Dirbuster(HackingTool):
    TITLE = "Dirbuster"
    DESCRIPTION = "DirBuster is a multi threaded java application designed" \
                  "to brute force directories and files names \n" \
                  "on web/application servers. " \
                  "attack against \n a web server and analizing the response."
    INSTALLED_SIZE = "10.75 MB"
    INSTALL_COMMANDS = [
        "sudo apt install dirbuster",
    ]
    RUN_COMMANDS = ["sudo dirbuster"]
    PROJECT_URL = "https://www.kali.org/tools/dirbuster/"


class WebAttackTools(HackingToolsCollection):
    TITLE = "Web Attack tools"
    DESCRIPTION = ""
    TOOLS = [
        Sublist3r(),
        CheckURL(),
        Dirb(),
        Dirbuster()
    ]
