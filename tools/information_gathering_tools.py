# coding=utf-8
import os
import socket
import subprocess
import webbrowser

from core import HackingTool
from core import HackingToolsCollection
from core import clear_screen


class Nmap(HackingTool):
    TITLE = "Network Map (nmap)"
    DESCRIPTION = "Free and open source utility for network discovery and security auditing"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super(Nmap, self).__init__(runnable = False)



class PortScan(HackingTool):
    TITLE = "Port scanning"

    def __init__(self):
        super(PortScan, self).__init__(installable = False)

    def run(self):
        clear_screen()
        target = input('Select a Target IP: ')
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])



class XeroSploit(HackingTool):
    TITLE = "Xerosploit"
    DESCRIPTION = "Xerosploit is a penetration testing toolkit whose goal is to perform\n" \
                  "man-in-the-middle attacks for testing purposes"
    INSTALL_COMMANDS = [
        "git clone https://github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"



class ReconSpider(HackingTool):
    TITLE = "ReconSpider(For All Scaning)"
    DESCRIPTION = "ReconSpider is most Advanced Open Source Intelligence (OSINT)" \
                  " Framework for scanning IP Address, Emails, \n" \
                  "Websites, Organizations and find out information from" \
                  " different sources.\n"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"

#    def __init__(self):
#        super(ReconSpider, self).__init__(runnable = False)


class PortScannerRanger(HackingTool):
    TITLE = "Port Scanner - rang3r"
    DESCRIPTION = "rang3r is a python script which scans in multi thread\n " \
                  "all alive hosts within your range that you specify."
    INSTALL_COMMANDS = [
        "git clone https://github.com/floriankunushevci/rang3r.git;"
        "sudo pip install termcolor"]
    PROJECT_URL = "https://github.com/floriankunushevci/rang3r"

    def run(self):
        ip = input("Enter Ip >> ")
        os.chdir("rang3r")
        subprocess.run(["sudo", "python", "rang3r.py", "--ip", ip])



class InformationGatheringTools(HackingToolsCollection):
    TITLE = "Information gathering tools"
    TOOLS = [
        Nmap(),
        PortScan(),
        XeroSploit(),
        ReconSpider(),
        PortScannerRanger()
    ]
