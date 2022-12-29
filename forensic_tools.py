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
    RUN_COMMANDS = ["sudo autopsy"]

    def __init__(self):
        super(Autopsy, self).__init__(installable = False)


class Wireshark(HackingTool):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network capture and analyzer \n" \
                  "tool to see what’s happening in your network.\n " \
                  "And also investigate Network related incident"
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super(Wireshark, self).__init__(installable = False)



class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic tools"
    TOOLS = [
        Autopsy(),
        Wireshark()
    ]
