# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class TheFatRat(HackingTool):
    TITLE = "TheFatRat"
    DESCRIPTION = "TheFatRat Provides An Easy way to create Backdoors and \n" \
                  "Payload which can bypass most anti-virus"
    INSTALLED_SIZE = "476.11 MB"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && sudo chmod +x setup.sh && sudo bash setup.sh",
    ]
    RUN_COMMANDS = ["sudo fatrat"]
    PROJECT_URL = "https://github.com/Screetsec/TheFatRat"

    def __init__(self):
        super(TheFatRat, self).__init__([
            ('Update', self.update),
            ('Troubleshoot', self.troubleshoot)
        ])

    def update(self):
        os.system(
            "cd TheFatRat && bash update && chmod +x setup.sh && bash setup.sh")

    def troubleshoot(self):
        os.system("cd TheFatRat && sudo chmod +x chk_tools && ./chk_tools")



class MSFVenom(HackingTool):
    TITLE = "MSFvenom Payload Creator"
    DESCRIPTION = "MSFvenom Payload Creator (MSFPC) is a wrapper to generate \n" \
                  "multiple types of payloads, based on users choice.\n" \
                  "The idea is to be as simple as possible (only requiring " \
                  "one input) \nto produce their payload."
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/g0tmi1k/msfpc.git",
        "cd msfpc;sudo chmod +x msfpc.sh"
    ]
    PROJECT_URL = "https://github.com/g0tmi1k/msfpc"

    def run(self):
        os.system("cd msfpc; sudo bash msfpc.sh -h -v")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m MSFVenom => \033[0m")
        os.system(subinput)

class VeilFramework(HackingTool):
    TITLE = "VeilFramework"
    DESCRIPTION = "Veil is a tool designed to generate metasploit payloads\n" \
                  "that bypass common anti-virus solutions.\n"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = [
        "apt -y install veil",
        "/usr/share/veil/config/setup.sh --force --silent"
    ]
    RUN_COMMANDS = ["./Veil.py"]
    PROJECT_URL = "https://github.com/Veil-Framework/Veil"



class PayloadCreatorTools(HackingToolsCollection):
    TITLE = "Payload Creation Tools"
    TOOLS = [
        TheFatRat(),
        MSFVenom(),
        VeilFramework()
    ]
