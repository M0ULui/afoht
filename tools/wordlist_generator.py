# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Cupp(HackingTool):
    TITLE = "Cupp"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities of passwords,\n " \
                  "and you can choose Length, Lowercase, Capital, Numbers and Special Chars"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = ["git clone https://github.com/Mebus/cupp.git"]
    RUN_COMMANDS = ["cd cupp && python3 cupp.py -i"]
    PROJECT_URL = "https://github.com/Mebus/cupp"


class Pydictor(HackingTool):
    TITLE = "Pydictor"
    DESCRIPTION = "Pydictor can be used to generate a general blast wordlist," \
                  "\n a custom wordlist based on Web content, a social engineering wordlist" \
                  "\n and more!"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = ["git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git"]
    #RUN_COMMANDS = ["cd pydictor/ && chmod +x pydictor.py && python pydictor.py"]
    PROJECT_URL = "https://github.com/LandGrey/pydictor"

    def run(self):
        os.system("cd pydictor/ && chmod +x pydictor.py && python pydictor.py")
        subinput = input("Pydictor => ")
        os.system(subinput)

class WlCreator(HackingTool):
    TITLE = "WordlistCreator"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities" \
                  " of passwords,\n and you can choose Lenght, Lowercase, " \
                  "Capital, Numbers and Special Chars"
    INSTALLED_SIZE = "N/A"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Z4nzu/wlcreator.git"]
    RUN_COMMANDS = [
        "cd wlcreator && sudo gcc -o wlcreator wlcreator.c && ./wlcreator 5"]
    PROJECT_URL = "https://github.com/Z4nzu/wlcreator"


class WordlistGeneratorTools(HackingToolsCollection):
    TITLE = "Wordlist Generator"
    TOOLS = [
        Cupp(),
        Pydictor(),
        WlCreator()
    ]
