#!/bin/bash
clear
echo -e "\033[1;91m[+] Installation d'OSINTKILLER en cours...\033[0m"
pkg update -y && pkg install git python -y
pip install requests
mkdir -p ~/osintkiller/data
cd ~
echo -e "\033[1;92m[✓] Terminé. Lance le script avec : python3 osintkiller.py\033[0m"
