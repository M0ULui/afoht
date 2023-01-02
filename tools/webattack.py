# coding=utf-8
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class Web2Attack(HackingTool):
    TITLE = "Web2Attack"
    DESCRIPTION = "Web hacking framework with tools, exploits by python"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/santatic/web2attack.git"]
    RUN_COMMANDS = ["cd web2attack && sudo python3 w2aconsole"]
    PROJECT_URL = "https://github.com/santatic/web2attack"



class SubDomainFinder(HackingTool):
    TITLE = "SubDomain Finder"
    DESCRIPTION = "Sublist3r is a python tool designed to enumerate " \
                  "subdomains of websites using OSINT \n " \
                  "Usage:\n\t" \
                  "[1] python3 sublist3r.py -d example.com \n" \
                  "[2] python3 sublist3r.py -d example.com -p 80,443"
    INSTALL_COMMANDS = [
        "sudo pip3 install requests argparse dnspython",
        "sudo git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class CheckURL(HackingTool):
    TITLE = "CheckURL"
    DESCRIPTION = "Detect evil urls that uses IDN Homograph Attack.\n\t" \
                  "[!] python3 checkURL.py --url google.com"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"


class Blazy(HackingTool):
    TITLE = "Blazy(Also Find ClickJacking)"
    DESCRIPTION = "Blazy is a modern login page bruteforcer"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UltimateHackers/Blazy.git",
        "cd Blazy && sudo pip2.7 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Blazy && sudo python2.7 blazy.py"]
    PROJECT_URL = "https://github.com/UltimateHackers/Blazy"


class Dirb(HackingTool):
    TITLE = "Dirb"
    DESCRIPTION = "DIRB is a Web Content Scanner. It looks for existing " \
                  "(and/or hidden) Web Objects.\n" \
                  "It basically works by launching a dictionary based " \
                  "attack against \n a web server and analizing the response."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo bash configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        uinput = input("Enter Url >> ")
        subprocess.run(["sudo", "dirb", uinput])

class Dirbuster(HackingTool):
    TITLE = "Dirbuster"
    DESCRIPTION = "DirBuster is a multi threaded java application designed" \
                  "to brute force directories and files names \n" \
                  "on web/application servers. " \
                  "attack against \n a web server and analizing the response."
    INSTALL_COMMANDS = [
        "sudo apt install dirbuster",
    ]
    RUN_COMMANDS = [""]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"


class WebAttackTools(HackingToolsCollection):
    TITLE = "Web Attack tools"
    DESCRIPTION = ""
    TOOLS = [
        Web2Attack(),
        SubDomainFinder(),
        CheckURL(),
        Blazy(),
        Dirb()
    ]
