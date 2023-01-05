# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection




class Apktool(HackingTool):
    TITLE = "Apktool"
    DESCRIPTION = "Apktool is a CLI tool for reverse engineering 3rd party,\n" \
                    "closed, binary Android apps."

    INSTALLED_SIZE = "68.10 MB"
    INSTALL_COMMANDS = [
        "sudo apt install apktool",
    ]
    PROJECT_URL = "https://www.kali.org/tools/apktool/"


    def run(self):
        os.system("apktool -h")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m Enter (.apk) File path >> \033[0m")
        os.system( "apktool d -f" + subinput)


class JDGui(HackingTool):
    TITLE = "JD-Gui"
    DESCRIPTION = "JD-Gui is a is a standalone graphical utility that displays\n" \
                    "Java source codes of “.class” files."
    INSTALLED_SIZE = "1.43 MB"
    INSTALL_COMMANDS = [
        "sudo apt install jd-gui",
    ]
    RUN_COMMANDS = ["sudo jd-gui"]
    PROJECT_URL = "https://www.kali.org/tools/jd-gui/"


class Dex2jar(HackingTool):
    TITLE = "Dex2jar"
    DESCRIPTION = "dex2jar is designed to read and translate\n" \
                    "the Dalvik Executable (.dex/.odex) format. \n" \
                        "It is recommended to visit the project url for guidance."
    INSTALLED_SIZE = "19.30 MB"
    INSTALL_COMMANDS = [
        "sudo apt install dex2jar",
    ]
    PROJECT_URL = "https://www.kali.org/tools/dex2jar/"
    
    def run(self):
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        print("Available command functions:\n"
        "e.g. < d2j-apk-sign | d2j-decrypt-string | d2j-asm-verify | d2j-baksmali | d2j-dex2jar >")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m Dex2jar => \033[0m")
        os.system(subinput)


class ReverseEngineeringTools(HackingToolsCollection):
    TITLE = "Reverse engineering tools"
    TOOLS = [
        Apktool(),
        JDGui(),
        Dex2jar()
    ]

