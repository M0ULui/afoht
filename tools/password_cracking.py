# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class JohnTheRipper(HackingTool):
    TITLE = "JohnTheRipper"
    DESCRIPTION = "John the Ripper is a tool that can be used to crack passwords.\n" \
                  "[!] It supports cracking of various types of hashes and ciphers\n" \
                  "e.g. <john --wordlist=/usr/share/john/password.lst --rules unshadowed.txt>"
    INSTALLED_SIZE = "77.31 MB"
    INSTALL_COMMANDS = ["sudo apt-get install john -y"]
    PROJECT_URL = "https://www.kali.org/tools/john/"

    def run(self):
        os.system("cd /; sudo john")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m JohnTheRipper => \033[0m")
        os.system(subinput)


class Hydra(HackingTool):
    TITLE = "Hydra"
    DESCRIPTION = "Hydra is a tool that can be used to crack passwords.\n" \
                  "[!] It supports cracking of various types of hashes and ciphers\n"
    INSTALLED_SIZE = "956 KB" 
    INSTALL_COMMANDS = ["sudo apt install hydra -y"]
    PROJECT_URL = "https://www.kali.org/tools/hydra/"
    
    def run(self):
        os.system("cd /; sudo hydra; sudo hydra -h")
        os.system ("echo '\033[1;32m---------------------------------------\033[m';")
        subinput = input("\033[33;5m Hydra => \033[0m")
        os.system(subinput)


class PasswordCrackingTools(HackingToolsCollection):
    TITLE = "Password Cracking Tools"
    TOOLS = [
        JohnTheRipper(),
        Hydra()
    ]
