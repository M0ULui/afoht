# coding=utf-8
import os
from time import sleep

from core import HackingTool
from core import HackingToolsCollection


class UpdateTool(HackingTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update AFOHT", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/afoht/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/afoht/;"
                  "mkdir afoht;"
                  "cd afoht;"
                  "git clone https://github.com/M0ULui/afoht.git;"
                  "cd afoht;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(HackingTool):
    TITLE = "Uninstall AFOHT"
    DESCRIPTION = "Uninstall AFOHT"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("Uninstall process has been Initiated...\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/afoht/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/afoht/;")
        print("\nAFOHT Successfully Uninstalled..")
        print("Thank You, See You Again!")
        sleep(1)


class Management(HackingToolsCollection):
    TITLE = "Update or Uninstall | AFOHT"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]