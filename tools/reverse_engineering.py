# coding=utf-8
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class AndroGuard(HackingTool):
    TITLE = "Androguard"
    DESCRIPTION = "Androguard is a Reverse engineering, Malware and goodware " \
                  "analysis of Android applications and more"
    INSTALL_COMMANDS = ["sudo pip3 install -U androguard"]
    PROJECT_URL = "https://github.com/androguard/androguard "

    def __init__(self):
        super(AndroGuard, self).__init__(runnable = False)


class Apk2Gold(HackingTool):
    TITLE = "Apk2Gold"
    DESCRIPTION = "Apk2Gold is a CLI tool for decompiling Android apps to Java"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/lxdvs/apk2gold.git",
        "cd apk2gold;sudo bash make.sh"
    ]
    PROJECT_URL = "https://github.com/lxdvs/apk2gold "

    def run(self):
        subinput = input("Enter (.apk) File Path >> ")
        subprocess.run(["sudo", "apk2gold", subinput])


class Jadx(HackingTool):
    TITLE = "JadX"
    DESCRIPTION = "Jadx is Dex to Java decompiler.\n" \
                  "[*] decompile Dalvik bytecode to java classes from APK, dex," \
                  " aar and zip files\n" \
                  "[*] decode AndroidManifest.xml and other resources from " \
                  "resources.arsc"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/skylot/jadx.git",
        "cd jadx;./gradlew dist"
    ]
    PROJECT_URL = "https://github.com/skylot/jadx"

    def __init__(self):
        super(Jadx, self).__init__(runnable = False)

class Apktool(HackingTool):
    TITLE = "Apktool"
    DESCRIPTION = "Apktool is a CLI tool for reverse engineering 3rd party,\n" \
                    "closed, binary Android apps."

    INSTALL_COMMANDS = [
        "sudo apt install apktool",
    ]
    PROJECT_URL = "https://www.kali.org/tools/apktool/"

    def run(self):
        subinput = input("Enter (.apk) File path >> ")
        subprocess.run(["sudo", "apktool d", subinput])

class JDGui(HackingTool):
    TITLE = "JD-Gui"
    DESCRIPTION = "JD-Gui is a is a standalone graphical utility that displays\n" \
                    "Java source codes of “.class” files."
    INSTALL_COMMANDS = [
        "sudo apt install jd-gui",
    ]
    RUN_COMMANDS = ["sudo jd-gui"]
    PROJECT_URL = "https://www.kali.org/tools/jd-gui/"

class dex2jar(HackingTool):
    TITLE = "dex2jar"
    DESCRIPTION = "dex2jar is designed to read and translate\n" \
                    "the Dalvik Executable (.dex/.odex) format. \n" \
                        "It is recommended to visit the project url for guidance."
    INSTALL_COMMANDS = [
        "sudo apt install dex2jar",
    ]
    PROJECT_URL = "https://www.kali.org/tools/dex2jar/"
    def run(self):
        print("Available command functions:\n"
        "e.g. < d2j-dex2jar | d2j-jar-remap | dex2jar | d2j-dex-dump | d2j-init-deobf >")
        subinput = input("dex2jar >> ")
        subprocess.run([subinput])

class ReverseEngineeringTools(HackingToolsCollection):
    TITLE = "Reverse engineering tools"
    TOOLS = [
        Apktool(),
        JDGui(),
        dex2jar(),
        AndroGuard(),
        Apk2Gold(),
        Jadx()
    ]
