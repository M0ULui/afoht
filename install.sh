#!/bin/bash

set -e

clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'

echo -e "${CYAN} "
echo ""
echo "    _    _     _          _____ ___  ____        ___  _   _ _____ ";
echo "   / \  | |   | |        |  ___/ _ \|  _ \      / _ \| \ | | ____|";
echo "  / _ \ | |   | |   _____| |_ | | | | |_) |____| | | |  \| |  _|  ";
echo " / ___ \| |___| |__|_____|  _|| |_| |  _ <_____| |_| | |\  | |___ ";
echo "/_/   \_\_____|_____|    |_|   \___/|_| \_\     \___/|_| \_|_____|";
echo "";
echo -e "${PURPLE}"
echo " _   _    _    ____ _  _____ _   _  ____    _____ ___   ___  _ ";
echo "| | | |  / \  / ___| |/ /_ _| \ | |/ ___|  |_   _/ _ \ / _ \| |    ";
echo "| |_| | / _ \| |   | ' / | ||  \| | |  _     | || | | | | | | |    ";
echo "|  _  |/ ___ \ |___| . \ | || |\  | |_| |    | || |_| | |_| | |___ ";
echo "|_| |_/_/   \_\____|_|\_\___|_| \_|\____|    |_| \___/ \___/|_____|";
echo -e "${WHITE}----------------------------------------------------------------------"
echo -e "${BLUE}     https://github.com/M0ULui/afoht ${NC}"
echo -e "${RED}      [!] This Tool Must Run As ROOT [!]${NC}\n"
echo -e "${WHITE}----------------------------------------------------------------------"
echo -e ${ORANGE}                "Available OS Options : \n"
echo -e "${WHITE}              [1] Kali Linux"
echo -e "${WHITE}              [0] Exit "
echo -n -e "${YELLOW}AFOHT >> "
read choice
INSTALL_DIR="/usr/share/doc/afoht"
BIN_DIR="/usr/bin/"
if [ $choice == 1 ]; then
	echo "[*] Ensuring Internet Connection is Fine.."
	wget -q --tries=10 --timeout=20 --spider https://google.com
	if [ $? == 0 ]; then
        echo -e ${BLUE}"[✔] Initializing ... "
        if [ $choice == 1 ]; then
            sudo apt-get update -y && apt-get upgrade -y
            sudo apt-get install python3-pip -y
        fi

	    echo "[✔] Checking directories..."
	    if [ -d "$INSTALL_DIR" ]; then
	        echo "[!] A Directory for All-For-One Hacking Tool Was Found. Do You Want To Replace It ? [y/n]:" ;
	        read input
	        if [ "$input" = "y" ]; then
	            sudo rm -R "$INSTALL_DIR"
	        else
	            exit
	        fi
	    fi

        echo "[✔] Installing ...\n";
        sudo git clone https://github.com/M0ULui/afoht.git "$INSTALL_DIR";
        echo "#!/bin/bash
        python3 $INSTALL_DIR/afoht.py" '${1+"$@"}' > afoht;
        sudo chmod +x afoht;
        sudo cp afoht /usr/bin/ && rm afoht;

        echo "\n[+] Trying to install The Prerequisites ..."
        if [ $choice == 1 ]; then
            sudo pip3 install lolcat flask requests
            sudo apt-get install -y figlet
            apt-get install -y boxes
        fi

	else
		  echo -e $RED "!! Unable To Proceed, Internet Connection is Weak !!"
	fi

    if [ -d "$INSTALL_DIR" ]; then
        echo "";
        echo "[✔] Successfuly Installed !!!";
        echo -e $ORANGE "       [✔]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[✔]"
        echo            "       [✔]                                                             [✔]"
        echo -e $ORANGE "       [✔]    ✔✔✔ Proceed by Typing (afoht) in the Terminal ✔✔✔     [✔]"
        echo            "       [✔]                                                             [✔]"
        echo -e $ORANGE "       [✔]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[✔]"
    else
        echo "[✘] Installation Failed, Please Try Again. [✘]";
        exit
    fi

elif [ $choice == 0] && [ $choice != 1 ] ; then
    echo -e $RED "[+] Thank You! [+] "
    exit
else
    echo -e $RED "[!] Please Select A Valid Option [!]"
fi
