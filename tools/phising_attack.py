# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Setoolkit(HackingTool):
    TITLE = "Setoolkit"
    DESCRIPTION = "The Social-Engineer Toolkit is an open-source penetration\n" \
                  "testing framework designed for social engineering"
    INSTALLED_SIZE = "48.50 MB"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trustedsec/social-engineer-toolkit/",
        "cd social-engineer-toolkit && sudo python3 setup.py"
    ]
    RUN_COMMANDS = ["sudo setoolkit"]
    PROJECT_URL = "https://github.com/trustedsec/social-engineer-toolkit"
 

class SocialFish(HackingTool):
    TITLE = "SocialFish"
    DESCRIPTION = "Automated Phishing Tool & Information Collector NOTE: username is 'root' and password is 'pass'"
    INSTALLED_SIZE = "4 MB"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y",
        "cd SocialFish && sudo python3 -m pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SocialFish && sudo python3 SocialFish.py root pass"]
    PROJECT_URL = "https://github.com/UndeadSec/SocialFish"


class HiddenEye(HackingTool):
    TITLE = "HiddenEye"
    DESCRIPTION = "Modern Phishing Tool With Advanced Functionality And " \
                  "Multiple Tunnelling Services \n" \
                  "\t [!]https://github.com/Morsmalleo/HiddenEye"
    INSTALLED_SIZE = "45.48 MB"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Morsmalleo/HiddenEye.git ;sudo chmod 777 HiddenEye",
        "cd HiddenEye;sudo pip3 install -r requirements.txt;sudo pip3 install requests;pip3 install pyngrok"
    ]
    RUN_COMMANDS = ["cd HiddenEye;sudo python3 HiddenEye.py"]
    PROJECT_URL = "https://github.com/Morsmalleo/HiddenEye.git"


class ShellPhish(HackingTool):
    TITLE = "ShellPhish"
    DESCRIPTION = "Fhishing Tool for 18 social media"
    INSTALLED_SIZE = "12.44 MB"
    INSTALL_COMMANDS = ["git clone https://github.com/An0nUD4Y/shellphish.git"]
    RUN_COMMANDS = ["cd shellphish;sudo bash shellphish.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/shellphish"



class PhishingAttackTools(HackingToolsCollection):
    TITLE = "Phishing Attack Tools"
    TOOLS = [
        Setoolkit(),
        SocialFish(),
        HiddenEye(),
        ShellPhish()
    ]
