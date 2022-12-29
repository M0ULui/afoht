echo "    _    _     _          _____ ___  ____        ___  _   _ _____ ";
echo "   / \  | |   | |        |  ___/ _ \|  _ \      / _ \| \ | | ____|";
echo "  / _ \ | |   | |   _____| |_ | | | | |_) |____| | | |  \| |  _|  ";
echo " / ___ \| |___| |__|_____|  _|| |_| |  _ <_____| |_| | |\  | |___ ";
echo "/_/   \_\_____|_____|    |_|   \___/|_| \_\     \___/|_| \_|_____|";
echo "";
echo " _   _    _    ____ _  _____ _   _  ____    _____ ___   ___  _ ";
echo "| | | |  / \  / ___| |/ /_ _| \ | |/ ___|  |_   _/ _ \ / _ \| |    ";
echo "| |_| | / _ \| |   | ' / | ||  \| | |  _     | || | | | | | | |    ";
echo "|  _  |/ ___ \ |___| . \ | || |\  | |_| |    | || |_| | |_| | |___ ";
echo "|_| |_/_/   \_\____|_|\_\___|_| \_|\____|    |_| \___/ \___/|_____|";

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/afoht/

clear

cd /etc/

clear

sudo rm -rf /etc/afoht

clear

mkdir hackingtool

clear

cd hackingtool

clear

git clone https://github.com/M0ULui/afoht.git

clear

cd afoht

clear

sudo chmod +x install.sh

clear

./install.sh

clear
