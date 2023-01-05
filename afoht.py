##!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Version 1.1.0
import os
import webbrowser
from platform import system
from time import sleep

from core import HackingToolsCollection
from tools.ddos import DDOSTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.webattack import WebAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.password_cracking import PasswordCrackingTools
from tools.management import *

logo = """\033[36m 
    _    _     _          _____ ___  ____        ___  _   _ _____ 
   / \  | |   | |        |  ___/ _ \|  _ \      / _ \| \ | | ____|
  / _ \ | |   | |   _____| |_ | | | | |_) |____| | | |  \| |  _|  
 / ___ \| |___| |__|_____|  _|| |_| |  _ <_____| |_| | |\  | |___ 
/_/   \_\_____|_____|    |_|   \___/|_| \_\     \___/|_| \_|_____|
\033[35m
 _   _    _    ____ _  _____ _   _  ____    _____ ___   ___  _     
| | | |  / \  / ___| |/ /_ _| \ | |/ ___|  |_   _/ _ \ / _ \| |    
| |_| | / _ \| |   | ' / | ||  \| | |  _     | || | | | | | | |    
|  _  |/ ___ \ |___| . \ | || |\  | |_| |    | || |_| | |_| | |___ 
|_| |_/_/   \_\____|_|\_\___|_| \_|\____|    |_| \___/ \___/|_____
|                  
    \033[34m[✔]    https://github.com/M0ULui/afoht     [✔]
    \033[34m[✔]            Version 1.3               [✔]
    \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[97m """

all_tools = [
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    PasswordCrackingTools(),
    Management()
]




class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(logo + '\033[0m \033[97m')


if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = "/home/AFOHTpath.txt"
            if not os.path.exists(fpath):
                os.system('clear')
                # run.menu()
                print("""
                        [@] Set Path (All your tools will be installed in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("AFOHT =>> ")

                if choice == "1":
                    print("Manual Path will be available in the near future!")
                    Manpath = "/home/afoht/"
                    with open(fpath, "w") as f:
                        f.write(Manpath)
                    print(f"Successfully Set to Default Path: {Manpath}")
                elif choice == "2":
                    autopath = "/home/afoht/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print(f"Your Default Path Is: {autopath}")
                    sleep(3)
                else:
                    print("Try Again..!!")
                    exit(0)

            with open(fpath) as f:
                archive = f.readline()
                if not os.path.exists(archive):
                    os.mkdir(archive)
                os.chdir(archive)
                AllTools().show_options()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print(
                r"\033[91m Please Run This Tool On A Debian System For Best Results\e[00m"
            )
            sleep(2)
        else:
            print("Please Check Your System and Try Again ...")

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)
