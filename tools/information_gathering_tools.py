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
    INSTALLED_SIZE = "4.86 MB"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def run(self):
        os.system ("nmap -h")
        os.system ("echo '\033[1;32m---------------------------\033[m';")
        subinput = input("'\033[1;32m[33m Nmap => \033[m';'")
        os.system(subinput)

#    def __init__(self):
 #       super(Nmap, self).__init__(runnable = False)

class DNSRecon(HackingTool):
    TITLE = "DNSRecon"
    DESCRIPTION = "DNSRecon is a Python script that provides the ability to perform \n" \
                    "Multiple Enumeration and lookup tasks"
    INSTALLED_SIZE = "1.4 MB"
    INSTALL_COMMANDS = ["sudo apt install dnsrecon"]
    RUN_COMMANDS = ["sudo dnsrecon -h"]
    PROJECT_URL = "https://www.kali.org/tools/dnsrecon/"

    def run(self):
        os.system ("sudo dnsrecon -h")
        os.system ("echo -e  '\033[1;32m---------------------------\033[m';")
        subinput = input('DNSRecon =>')
        os.system (subinput)


class PortScan(HackingTool):
    TITLE = "Port Scan"
    DESCRIPTION = "Perform Simple Port Scanning with Nmap"

    def __init__(self):
        super(PortScan, self).__init__(installable = False)

    def run(self):
        target = input('Select a Target IP: ')
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])


class ReconSpider(HackingTool):
    TITLE = "ReconSpider(For All Scaning)"
    DESCRIPTION = "ReconSpider is most Advanced Open Source Intelligence (OSINT)" \
                  " Framework for scanning IP Address, Emails, \n" \
                  "Websites, Organizations and find out information from" \
                  " different sources.\n"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip; cd reconspider; sudo python3 setup.py install",
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"

#    def __init__(self):
#        super(ReconSpider, self).__init__(runnable = False)


class InformationGatheringTools(HackingToolsCollection):
    TITLE = "Information gathering tools"
    TOOLS = [
        Nmap(),
        PortScan(),
        DNSRecon(),
        ReconSpider()
    ]
