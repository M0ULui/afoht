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


class VeilFramework(HackingTool):
    TITLE = "Veil Framework"
    DESCRIPTION = "Veil is a tool designed to generate metasploit payloads\n" \
                  "that bypass common anti-virus solutions.\n"
    INSTALLED_SIZE = "767 MB"
    INSTALL_COMMANDS = [
        "apt -y install veil",
        "/usr/share/veil/config/setup.sh --force --silent"
    ]
    RUN_COMMANDS = ["sudo veil"]
    PROJECT_URL = "https://github.com/Veil-Framework/Veil"



class PayloadCreatorTools(HackingToolsCollection):
    TITLE = "Payload Creation Tools"
    TOOLS = [
        TheFatRat(),
        VeilFramework()
    ]
