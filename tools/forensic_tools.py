# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Autopsy(HackingTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a platform that is used by Cyber Investigators.\n" \
                  "[!] Works in any OS\n" \
                  "[!] Recover Deleted Files from any OS & Media \n" \
                  "[!] Extract Image Metadata"
    INSTALLED_SIZE = "1 MB"
    INSTALL_COMMANDS = ["sudo apt install autopsy"]
    RUN_COMMANDS = ["sudo autopsy"]



class Wireshark(HackingTool):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network capture and analyzer \n" \
                  "tool to see what is happening in your network.\n " \
                  "And also investigate Network related incident"
    INSTALLED_SIZE = "200 MB"
    INSTALL_COMMANDS = ["sudo apt install wireshark"]
    RUN_COMMANDS = ["sudo wireshark"]



class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic Tools"
    TOOLS = [
        Autopsy(),
        Wireshark()
    ]
